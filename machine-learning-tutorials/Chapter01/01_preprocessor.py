import numpy as np
from sklearn import preprocessing

# 数据预处理

data = np.array([[3, -1.5,  2, -5.4], [0,  4,  -0.3, 2.1], [1,  3.3, -1.9, -4.3]])

print(data)

# 均值移除 Mean removal | axis=0  column | axis=1  row
print("Mean: ", data.mean(axis=0))
print("Standard Deviation: ", data.std(axis=0))

data_standardized = preprocessing.scale(data)

print("Mean Standardized data: ", data_standardized.mean(axis=0))
print("standard Deviation standardized data: ", data_standardized.std(axis=0))


# 范围缩放 Scaling
data_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled = data_scaler.fit_transform(data)
print("data_scaled: ")
print(data_scaled)

print("Min: ", data.min(axis=0))
print("Max: ", data.max(axis=0))

print("data_scaled Min: ", data_scaled.min(axis=0))
print("data_scaled Max: ", data_scaled.max(axis=0))

print(data_scaled)

# 归一化 Normalization
data_normalized = preprocessing.normalize(data, norm='l1', axis=0)
print("data_normalized : ")
print(data_normalized)

data_norm_abs = np.abs(data_normalized)
print("data_norm_abs : ")
print(data_norm_abs.sum(axis=0))


# 二值化 Binarization
data_binarized = preprocessing.Binarizer(threshold=1.4).transform(data)
print("data_binarized: ")
print(data_binarized)

print("===============================================")
# 独热编码 One Hot Encoding
data = np.array([[1, 1, 2], [0, 2, 3], [1, 0, 1], [0, 1, 0]])
print(data)

encoder = preprocessing.OneHotEncoder()
encoder.fit(data)
encoded_vector = encoder.transform([[1, 2, 3]]).toarray()

print("encoded_vector 1 2 3: ", encoded_vector)

