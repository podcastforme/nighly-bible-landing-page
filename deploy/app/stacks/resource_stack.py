from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3_deployment as s3deploy,
    aws_certificatemanager as acm,
    CfnOutput,
    RemovalPolicy
)
from constructs import Construct
import json
import os

class ResourceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, env_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define domain names based on environment
        if env_name == "prod":
            domain_name = "resource.podcastforme.com"
        else:
            domain_name = f"staging-resource.podcastforme.com"

        # Create S3 bucket
        bucket = s3.Bucket(
            self, f"{env_name}-resource-bucket",
            bucket_name=f"podcastforme-{env_name}-resources",
            removal_policy=RemovalPolicy.RETAIN,
            auto_delete_objects=False,
            versioned=True,
        )

        # Create ACM certificate
        certificate = acm.Certificate(
            self, f"{env_name}-certificate",
            domain_name=domain_name,
            validation=acm.CertificateValidation.from_email()
        )

        # Create CloudFront distribution
        distribution = cloudfront.Distribution(
            self, f"{env_name}-distribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin(bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                allowed_methods=cloudfront.AllowedMethods.ALLOW_GET_HEAD,
                cached_methods=cloudfront.CachedMethods.CACHE_GET_HEAD
            ),
            domain_names=[domain_name],
            certificate=certificate,
            price_class=cloudfront.PriceClass.PRICE_CLASS_100
        )

        # Create well-known directory for app associations
        well_known_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'well-known')
        os.makedirs(well_known_dir, exist_ok=True)

        # Create apple-app-site-association file
        apple_config = {
            "applinks": {
                "apps": [],
                "details": [
                    {
                        "appID": "com.podcastforme.mobileBible",
                        "paths": ["*"]
                    },
                    {
                        "appID": "com.podcastforme.mobileBible.RunnerTest",
                        "paths": ["*"]
                    }
                ]
            }
        }
        
        with open(os.path.join(well_known_dir, 'apple-app-site-association'), 'w') as f:
            json.dump(apple_config, f, indent=2)

        # Create assetlinks.json file
        android_config = [{
            "relation": ["delegate_permission/common.handle_all_urls"],
            "target": {
                "namespace": "android_app",
                "package_name": "com.podcastforme.bedtime_bible",
                "sha256_cert_fingerprints": ["*"]
            }
        }]
        
        with open(os.path.join(well_known_dir, 'assetlinks.json'), 'w') as f:
            json.dump(android_config, f, indent=2)

        # Deploy well-known files to S3
        s3deploy.BucketDeployment(
            self, f"{env_name}-well-known-deployment",
            sources=[s3deploy.Source.asset(well_known_dir)],
            destination_bucket=bucket,
            destination_key_prefix=".well-known",
            retain_on_delete=False,
        )

        # Output the CloudFront URL, S3 bucket name, and DNS instructions
        CfnOutput(
            self, f"{env_name}-cf-url",
            value=distribution.distribution_domain_name,
            description="CloudFront Distribution URL"
        )
        CfnOutput(
            self, f"{env_name}-bucket-name",
            value=bucket.bucket_name,
            description="S3 Bucket Name"
        )
        CfnOutput(
            self, f"{env_name}-domain-name",
            value=domain_name,
            description="Custom Domain Name"
        )
        CfnOutput(
            self, f"{env_name}-dns-instructions",
            value=f"""
DNS Configuration Instructions for CloudFlare:
1. Add a CNAME record in CloudFlare:
   - Name: {domain_name}
   - Target: {distribution.distribution_domain_name}
   - Proxy status: Proxied (orange cloud)
   - TTL: Auto

2. SSL/TLS Settings in CloudFlare:
   - Set SSL/TLS encryption mode to "Full (strict)"
   - Enable "Always Use HTTPS"

3. Page Rules (Optional):
   - Create a page rule for {domain_name}/*
   - Enable "Cache Everything"
   - Edge Cache TTL: 2 hours (or as needed)
""",
            description="DNS Configuration Instructions"
        )
