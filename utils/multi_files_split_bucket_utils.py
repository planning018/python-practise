import os


data_bucket_size = 5
data_feature_obj = {
    "train_path": "some csv file"
}

path_size_list = [(p, os.stat(p).st_size) for p in data_feature_obj["train_path"].split(',')]
path_size_list = sorted(path_size_list, key=lambda x: x[1], reverse=True)

buckets = [[] for i in range(data_bucket_size)]
buckets_size = [0.0] * data_bucket_size

for path, size in path_size_list:
    min_index = buckets_size.index(min(buckets_size))
    buckets[min_index].append(path)
    buckets_size[min_index] += size

for i in range(len(buckets)):
    print(f'######## bucket[{i}] {buckets[i]}')
print(f'######## buckets size: {["%.2f MB" % (x / 1024 / 1024) for x in buckets_size]}')
print(f'######## buckets length: {[len(bucket) for bucket in buckets]}')

data_feature_obj['bucket_path'] = buckets

print("data_feature_obj result is : {}".format(data_feature_obj))

is_chief = False
if is_chief == True:
    chief_data_path = data_feature_obj['bucket_path'][0]
    print("chief_data_path is {}".format(chief_data_path))
else:
    worker_data_path = data_feature_obj['bucket_path'][1]
    print("worker_data_path is {}".format(worker_data_path))


