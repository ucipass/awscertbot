#!/usr/bin/env /usr/local/bin/python

from dotenv import load_dotenv
import os
import sys
import boto3
import time
from awslib import delete_record 

##
## LOAD ENVIRONEMNT VARIABLES FROM .env FILE
##
load_dotenv()
aws_access_key_id     = os.environ.get('AWS_ACCESS_KEY_ID', False )
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', False)
aws_region            = os.environ.get('AWS_REGION', "us-east-1" )
aws_route53_zone      = os.environ.get('AWS_ROUTE53_ZONE', False)
certbot_domain        = os.environ.get('CERTBOT_DOMAIN', "NO_CERTBOT_DOMAIN")
certbot_validation    = os.environ.get('CERTBOT_VALIDATION', "NO_CERTBOT_VALIDATION")

##
## CHECK FOR MANDATORY VARIABLES
##
if not aws_access_key_id:
    sys.exit(f'AWS_ACCESS_KEY_ID environment variable is not set or in .env file')
if not aws_secret_access_key:
    sys.exit(f'AWS_SECRET_ACCESS_KEY environment variable is not set or in .env file')
if not aws_route53_zone:
    sys.exit(f'AWS_ROUTE53_ZONE environment variable is not set or in .env file')

if not certbot_domain:
    sys.exit(f'CERTBOT_DOMAIN environment variable provided by certbot')
else:
    print(f'CERTBOT_DOMAIN {certbot_domain}')
if not certbot_validation:
    sys.exit(f'CERTBOT_VALIDATION environment variable provided by certbot')
else:
    print(f'CERTBOT_VALIDATION {certbot_validation}')

##
## CREATE RECORD
##
config = {}
config["aws_access_key_id"]  = aws_access_key_id
config["aws_secret_access_key"] = aws_secret_access_key
config["aws_region"] = aws_region
config["aws_route53_zone"] = aws_route53_zone
config["aws_record_name"] = "_acme-challenge."+certbot_domain
config["aws_record_type"] = "TXT"
config["aws_record_ttl"] = 60
config["aws_record_value"] = '"'+certbot_validation+'"'

delete_record(config)
