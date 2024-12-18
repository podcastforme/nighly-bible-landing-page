# PodcastForMe Resources CDK

This CDK project creates CloudFront distributions backed by S3 buckets for both production and staging environments.

## Prerequisites

- Python 3.7 or later
- AWS CLI configured with appropriate credentials
- AWS CDK CLI installed

## Project Structure

```
cdk/
├── app/
│   ├── app.py              # Main CDK app
│   └── stacks/
│       └── resource_stack.py  # Stack definition
├── requirements.txt        # Python dependencies
└── Makefile              # Deployment commands
```

## Domains

- Production: resource.podcastforme.com
- Staging: staging-resource.podcastforme.com

## Setup

1. Initialize the project:
```bash
make init
```

2. Deploy to staging:
```bash
make deploy-staging
```

3. Deploy to production:
```bash
make deploy-prod
```

## Preview Changes

To see what changes will be applied:

- For staging:
```bash
make diff-staging
```

- For production:
```bash
make diff-prod
```

## Notes

- The S3 buckets are created with versioning enabled
- CloudFront distributions use HTTPS only
- ACM certificates are automatically created and validated through Route53
- The stack uses Price Class 100 for CloudFront (US, Canada, Europe, & Israel)
