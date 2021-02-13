import boto3
import botocore
import json
import decimal

class S3Manager:
    
    def __init__(self, bucket_name, region):
        self.bucket_name=bucket_name
        self.region=region
    
    
    def write(self, sufix, document):
        try:
            s3 = boto3.resource('s3', region_name=self.region)
            s3.Object(self.bucket_name, sufix + ".json").put(
            Body=document,
            Tagging="temporal=1")
        except botocore.exceptions.ClientError as error:
            raise error
        except botocore.exceptions.ParamValidationError as error:
            raise ValueError('The parameters you provided are incorrect: {}'.format(error))
        return "OK"