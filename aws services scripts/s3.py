# source: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html
# some of the code included here is taken or adapted from the Amazon S3 examples available on Boto3 documentation

import logging
import boto3
from botocore.exceptions import ClientError
import json

def create_bucket(bucket_name, region='eu-west-1'):

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location,)
        # Enable Block Public Access settings
        s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True
    
def main():
    bucket_name= "x23196505ashc"
    create_bucket("x23196505ashc")
    # Create a bucket policy
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': [
                "s3:GetObject",
                "s3:PutObject"
            ],
            'Resource': f'arn:aws:s3:::{bucket_name}/*'
        }]
    }
    
    
    # Convert the policy from JSON dict to string
    bucket_policy = json.dumps(bucket_policy)
    
    # Set the new policy
    s3 = boto3.client('s3')
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)

if __name__ == '__main__':
 main()
