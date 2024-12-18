#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.resource_stack import ResourceStack

app = cdk.App()

# Get environment from context
env_name = app.node.try_get_context("env")
if env_name not in ["prod", "staging"]:
    raise ValueError("env must be either 'prod' or 'staging'")

env = cdk.Environment(
    account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
    region=os.environ.get("CDK_DEFAULT_REGION", "ap-southeast-2")
)

ResourceStack(
    app,
    f"PodcastForMeResourceStack-{env_name}",
    env_name=env_name,
    env=env
)

app.synth()
