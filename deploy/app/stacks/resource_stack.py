from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3_deployment as s3deploy,
    aws_certificatemanager as acm,
    CfnOutput,
    RemovalPolicy,
    Duration
)
from constructs import Construct
import json
import os


class ResourceStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, env_name: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # Define domain names based on environment

    domain_name = scope.node.try_get_context("domain_name")

    # Create S3 bucket
    bucket = s3.Bucket(
        self, f"{env_name}-resource-bucket",
        bucket_name=scope.node.try_get_context("bucket_name"),
        removal_policy=RemovalPolicy.RETAIN,
        auto_delete_objects=False,
        versioned=False,
        block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
    )

    # Create Origin Access Identity
    origin_identity = cloudfront.OriginAccessIdentity(
        self, f"{env_name}-origin-identity",
        comment=f"Origin Access Identity for {env_name} environment"
    )

    # Grant read permissions to CloudFront
    bucket.grant_read(origin_identity)

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
            origin=origins.S3Origin(
                bucket,
                origin_access_identity=origin_identity
            ),
            viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            allowed_methods=cloudfront.AllowedMethods.ALLOW_GET_HEAD,
            cached_methods=cloudfront.CachedMethods.CACHE_GET_HEAD,
            cache_policy=cloudfront.CachePolicy(
                self, f"{env_name}-cache-policy",
                cache_policy_name=f"NightlyBible-{env_name}-cache-policy",
                min_ttl=Duration.seconds(0),
                max_ttl=Duration.seconds(1 if env_name == "staging" else 31536000),  # 1 year for prod
                default_ttl=Duration.seconds(1 if env_name == "staging" else 86400),  # 1 day for prod
                enable_accept_encoding_brotli=True,
                enable_accept_encoding_gzip=True,
            ) if env_name == "staging" else None
        ),
        domain_names=[domain_name],
        certificate=certificate,
        price_class=cloudfront.PriceClass.PRICE_CLASS_100,
        default_root_object="index.html",
        error_responses=[
            cloudfront.ErrorResponse(
                http_status=403,
                response_http_status=200,
                response_page_path="/index.html",
                ttl=Duration.seconds(0)
            ),
            cloudfront.ErrorResponse(
                http_status=404,
                response_http_status=200,
                response_page_path="/index.html",
                ttl=Duration.seconds(0)
            )
        ]
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
                    "appID": "com.nightlybible.bible",
                    "paths": ["*"]
                },
                {
                    "appID": "com.nightlybible.bible.RunnerTest",
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
            "package_name": "com.nightlybible.bible",
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
