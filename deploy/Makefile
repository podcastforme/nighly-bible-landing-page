.PHONY: init deploy-staging deploy-prod diff-staging diff-prod

init:
	pip install -r requirements.txt
	

deploy-staging:
	cdk deploy --context env=staging

deploy-prod:
	cdk deploy --context env=prod

diff-staging:
	cdk diff --context env=staging

diff-prod:
	cdk diff --context env=prod
