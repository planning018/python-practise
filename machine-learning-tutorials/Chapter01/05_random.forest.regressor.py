import csv
import numpy as np
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, explained_variance_score
import matplotlib.pyplot as plt

filename = 'resource/bike_day.csv'
file_reader = csv.reader(open(filename, 'r'), delimiter = ',')
x, y = [],[]
# 先不放入 14、15 列
for row in file_reader:
    x.append(row[2:13])
    y.append(row[-1])

# 提取特征名称
feature_names = np.array(x[0])
# 将第一行特征名称移除，只保留数值
x = np.array(x[1:]).astype(np.float32)
y = np.array(y[1:]).astype(np.float32)

# 打乱数据
shuffle(x,y, random_state=7)

num_training = int(0.9 * len(x))
x_train, y_train = x[:num_training], y[:num_training]
x_test, y_test = x[num_training:], y[num_training:]

# 参数 n_estimators 是指评估器的数量，表示随机森林需要使用的决策树数量
# 参数 max_depth 是指决策树的最大深度
# 参数 min_samples_split 是指决策树分裂一个节点需要用到的最小数据样板量
rf_regressor = RandomForestRegressor(n_estimators=1000, max_depth=10, min_samples_split=2)
rf_regressor.fit(x_train, y_train)

# 评估随机森林回归器的训练效果
y_pred = rf_regressor.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
evs = explained_variance_score(y_test, y_pred)
print("#### Random Forest regressor performance ####")
print("Mean squared error =", round(mse, 2))
print("Explained variance score =", round(evs, 2))

RFFImp = rf_regressor.feature_importances_
RFFImp = 100 * (RFFImp / max(RFFImp))
index_scored = np.flipud(np.argsort(RFFImp))
pos = np.arange(index_scored.shape[0]) + 0.5

plt.figure()
plt.bar(pos, RFFImp[index_scored], align='center')
plt.xticks(pos, feature_names[index_scored])
plt.ylabel('Relative Importance')
plt.title('Random Forest regressor')
plt.show()