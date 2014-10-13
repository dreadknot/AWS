import boto
c = boto.connect_s3()
b = c.get_bucket('bucket')
rs = b.list("dir/dir")
print rs
<boto.s3.bucketlistresultset.BucketListResultSet object at 0x1439c90>
for key in rs:
...    print key.name
...
