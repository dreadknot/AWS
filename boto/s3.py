import boto
c = boto.connect_s3()
b = c.get_bucket('splunkwhisper-backup-mregan-data')
rs = b.list('mregan-idx2/config_backup/')
print rs
for key in rs:
  print "%s %s" % (key.last_modified, key.size)