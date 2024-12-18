.PHONY: init deploy-staging deploy-prod diff-staging diff-prod

SLUG?=nightlybible
TARGET?=staging

ifeq ($(TARGET),staging)
	DOMAIN_NAME=www2.nightlybible.com
else
	DOMAIN_NAME=www.nightlybible.com
endif

BUCKET_NAME=$(SLUG)-$(TARGET)-resource

init:
	pip install -r requirements.txt
	

deploy:
	cdk deploy --context domain_name=$(DOMAIN_NAME) --context bucket_name=$(BUCKET_NAME) --context env_name=$(TARGET)
	cd ../web && aws s3 sync dist s3://$(BUCKET_NAME)

diff:
	cdk diff --context domain_name=$(DOMAIN_NAME) --context bucket_name=$(BUCKET_NAME) --context env_name=$(TARGET)