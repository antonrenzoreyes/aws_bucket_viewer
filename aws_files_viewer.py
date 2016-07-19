#!/usr/bin/python
import sys
import boto3

s3 = boto3.resource(
    's3',
    aws_access_key_id=sys.argv[1],
    aws_secret_access_key=sys.argv[2]
)
s3Client = boto3.client(
    's3',
    aws_access_key_id=sys.argv[1],
    aws_secret_access_key=sys.argv[2]
)
bucket = s3.Bucket(sys.argv[3])

fileList = open(sys.argv[4], 'w')

fileList.write("Bucket Name: " + sys.argv[3] + "\n")
for obj in bucket.objects.all():
        if obj.size > 8:
                url = s3Client.generate_presigned_url('get_object', Params = { 'Bucket': sys.argv[3], 'Key': obj.key, }, ExpiresIn = 86400, )
                fileList.write(obj.key + " " + "Size: " + str(obj.size) + " Bytes" + "\n\t|->URL: " + url + "\n\n")
        
