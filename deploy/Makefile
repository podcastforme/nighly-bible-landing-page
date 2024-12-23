.PHONY: init deploy-staging deploy-prod diff-staging diff-prod

SLUG?=nightlybible
TARGET?=staging
CLOUDFLARE_TOKEN?=GK6wG_SEzFlGILFQSeS-eFlWRga-IgeZbE3vjU6b
CLOUDFLARE_ZONE_ID?=f695ea0e93ec1abf24947ef104446975

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
	aws cloudfront create-invalidation --distribution-id $$(aws cloudformation describe-stacks --stack-name NightlyBibleResourceStack-$(TARGET) --region us-east-1 --query 'Stacks[0].Outputs[?ExportName==`distribution-id`].OutputValue' --output text) --paths "/*"
	curl -X POST "https://api.cloudflare.com/client/v4/zones/$(CLOUDFLARE_ZONE_ID)/purge_cache" \
		-H "Authorization: Bearer $(CLOUDFLARE_TOKEN)" \
		-H "Content-Type: application/json" \
		--data '{"purge_everything":true}' --silent 
	
	
diff:
	cdk diff --context domain_name=$(DOMAIN_NAME) --context bucket_name=$(BUCKET_NAME) --context env_name=$(TARGET)