>>> import boto
>>> c = boto.connect_s3()
>>> b = c.get_bucket('splunkwhisper-backup-mregan-data')
>>> rs = bucket.list("FamilyPhotos")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'bucket' is not defined
>>> rs = b.list("mregan-idx2/config_backup")
>>> print rs
<boto.s3.bucketlistresultset.BucketListResultSet object at 0x1439c90>
>>> for key in rs:
...    print key.name
...
