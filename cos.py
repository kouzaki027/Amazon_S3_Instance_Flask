import boto3
import uuid

#boto3.set_stream_logger('botocore', level='DEBUG')
#s3_resource = boto3.resource('s3',
#         aws_access_key_id='xxxxxxxxx',
#         aws_secret_access_key='yyyyyyyyyyyyyy')
#s3_client = boto3.client('s3',
#         aws_access_key_id='xxxxxxxxx',
#         aws_secret_access_key='yyyyyyyyyyyyyyyyyyyyyyy')
#s3_client = boto3.client('s3')
#s3_resource = boto3.resource('s3')
# retrieve the list of existing buckets
response = s3_client.list_buckets()
count = 1 
# output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print ( count ) 
    print(f'  {bucket["Name"]}')
    count = count+1                         
def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])
bucket_prefix='jrd'
BN = ''.join([bucket_prefix, str(uuid.uuid4())])
print ( "New Bucket about to be created:   " ,BN)
print(' ')




# create a new unique bucket -- bucket names must be unique
s3_resource.create_bucket(Bucket=BN,
                          CreateBucketConfiguration={
                              'LocationConstraint': 'us-east-2'})





# retrieve the list of existing buckets
response = s3_client.list_buckets()
# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')





# upload the file
first_file_name='data.txt'
s3_resource.Object(BN, first_file_name).upload_file(
    Filename=first_file_name)
# download the file
s3_resource.Object(BN, first_file_name).download_file(
    f'abc{first_file_name}')
print ("  use a  dictionary with resource object just as another way  ")
for bucket_dict in s3_resource.meta.client.list_buckets().get('Buckets'):
    print(bucket_dict['Name'])

                         



# delete objects
def delete_all_objects(bucket_name):
    res = []
    bucket=s3_resource.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        res.append({'Key': obj_version.object_key,
                    'VersionId': obj_version.id})
    print(res)
    bucket.delete_objects(Delete={'Objects': res})
delete_all_objects(BN)                  
# delete bucket, however it must be empty first;  
s3_resource.Bucket(BN).delete()
print("about to delete all buckets / objects ")
# loop through all buckets and delete objects and then bucket
buckets = s3_client.list_buckets()
for bucket in buckets['Buckets']:
    s3_bucket = s3_resource.Bucket(bucket['Name'])
    s3_bucket.objects.all().delete()
    s3_bucket.delete()
                         

                         
                         
                         
print ("Finished!")                         
