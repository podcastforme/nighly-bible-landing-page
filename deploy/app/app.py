#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.resource_stack import ResourceStack

app = cdk.App()

env_name = app.node.try_get_context("env_name")

env = cdk.Environment(
    account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
    region="us-east-1",
)

ResourceStack(
    app,
    f"NightlyBibleResourceStack-{env_name}",
    env_name=env_name,
    env=env
)

app.synth()
