import time
import boto3


class AmazonS3():
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name='ap-south-1'):
        self.client = boto3.client(
            's3',
            aws_access_key_id = aws_access_key_id,
            aws_secret_access_key = aws_secret_access_key,
            region_name = region_name
        )

        self.s3_resource = boto3.resource(
            's3',
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        print (self.s3_resource)

    def list_bucket(self):
        """
        Returns list of all bucket.
        [
            {'Name': 'ask-jennie-assets-1', 'CreationDate': datetime.datetime(2021, 3, 18, 19, 23, 59, tzinfo=tzutc())}
            {'Name': 'ask-jennie-assets-2', 'CreationDate': datetime.datetime(2021, 11, 12, 19, 23, 59, tzinfo=tzutc())}
            {'Name': 'ask-jennie-assets-3', 'CreationDate': datetime.datetime(2021, 7, 18, 19, 23, 59, tzinfo=tzutc())}
        ]
        """
        client_response = self.client.list_buckets()
        return client_response

    def upload_file(self, bucket, upload_file_path, bucket_file_path):
        """

        :param bucket: bucket name
        :param upload_file_path: uploading file path ( /home/usr/something.txt )
        :param bucket_file_path: path/on/bucket/something.txt
        :return: Upload Status
        """
        response = self.s3_resource.Bucket(bucket).put_object(
            Key=bucket_file_path,
            Body=open(upload_file_path, 'rb')
        )
        return response

    def upload_text(self, bucket, text_to_upload, bucket_file_path):
        """

        :param bucket: bucket name
        :param text_to_upload: String or text that has to be uploaded on s3.
        :param bucket_file_path: path/on/bucket/something.txt
        :return: Upload Status
        """
        response = self.s3_resource.Bucket(bucket).put_object(
            Key=bucket_file_path,
            Body=text_to_upload
        )
        return response


aws_access_key_id = "AKIA3B7555HI7NOZLXL4"
aws_secret_access_key = "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"
ap_region = "ap-south-1"
bucket = "cdn.jennie"
import os
from os import listdir
from os.path import isfile, join

def get_aws_instance():
    aws = AmazonS3(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=ap_region
    )
    return aws

def upload_file_to_s3():
    file_to_upload_path = os.path.join(os.getcwd(), "dist/ask_jennie-0.0.1-py3-none-any.whl")
    filename = "ask_jennie-0.0.1-py3-none-any.whl"
    aws = get_aws_instance()
    resp = aws.upload_file(
        bucket=bucket,
        upload_file_path=file_to_upload_path,
        bucket_file_path=filename
    )
    print (resp)
    print (file_to_upload_path)
    print ("https://s3.ap-south-1.amazonaws.com/cdn.jennie/" + filename)


if __name__ == '__main__':
    import os
    os.system("./build.sh")
    upload_file_to_s3()