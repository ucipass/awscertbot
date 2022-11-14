import boto3
import os

def create_record(config):
    config["method"] = "UPSERT"
    change(config)

def delete_record(config):
    config["method"] = "DELETE"
    change(config)

##
## DEPENDENCIES
##
## dependencies: aws_access_key_id, aws_secret_access_key, aws_region, aws_route53_zone, aws_record_name, aws_record_type, aws_record_ttl, aws_record_value
##

def change(config):

    aws_access_key_id     = config["aws_access_key_id"] 
    aws_secret_access_key = config["aws_secret_access_key"] 
    aws_region            = config["aws_region"] 
    aws_route53_zone      = config["aws_route53_zone"] 
    aws_record_name       = config["aws_record_name"] 
    aws_record_type       = config["aws_record_type"] 
    aws_record_ttl        = config["aws_record_ttl"] 
    aws_record_value      = config["aws_record_value"]
    method                = config["method"]   

    client = boto3.client('route53',
                        aws_access_key_id= aws_access_key_id,
                        aws_secret_access_key= aws_secret_access_key,
                        region_name= aws_region
                        )
    if ( os.environ.get('DEBUG', False ) ):
        print(config)

    zones = client.list_hosted_zones_by_name()
    zone = next(zone for zone in zones['HostedZones'] if zone['Name'] == aws_route53_zone+'.' or zone['Name'] == aws_route53_zone+'.')
    aws_zoneid = zone['Id']


    # DELETE OR UPSERT AWS record
    
    response = client.change_resource_record_sets(
        HostedZoneId= aws_zoneid,
        ChangeBatch={
            'Changes': [
                {
                    'Action': method,
                    'ResourceRecordSet': {
                        'Name': aws_record_name,
                        'Type': aws_record_type,
                        'TTL': aws_record_ttl,
                        'ResourceRecords': [
                            {
                                'Value': aws_record_value
                            }
                        ]
                    }
                }
            ]
        }
    )
