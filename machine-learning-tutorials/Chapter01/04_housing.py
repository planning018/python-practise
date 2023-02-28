import numpy as np
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn import datasets
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.utils import shuffle
import matplotlib.pyplot as plt


def plot_feature_importances(feature_importances, title, feature_names):
    # Normalize the importance values
    # 将重要性能值标准化
    feature_importances = 100.0 * (feature_importances / max(feature_importances))

    # Sort the values and flip them
    # 将得分从高到低排序
    index_sorted = np.flipud(np.argsort(feature_importances))

    # Arrange the X ticks
    # 让 X坐标轴上的标签居中显示
    pos = np.arange(index_sorted.shape[0]) + 0.5

    # Plot the bar graph
    plt.figure()
    plt.bar(pos, feature_importances[index_sorted], align='center')
    plt.xticks(pos, feature_names[index_sorted])
    plt.ylabel('Relative Importance')
    plt.title(title)
    plt.show()


if __name__=='__main__':
    # Load housing data
    housing_data = datasets.load_boston()

    # Shuffle the data
    x,y = shuffle(housing_data.data, housing_data.target, random_state=7)

    # Split the data 80/20 (80% for training, 20% for testing)
    num_training = int(0.8 * len(x))
    x_train, y_train = x[:num_training], y[:num_training]
    x_test, y_test = x[num_training:], y[num_training:]

    # Fit decision tree regression model
    dt_regressor = DecisionTreeRegressor(max_depth=4)
    dt_regressor.fit(x_train, y_train)

    # Fit decision tree regression model with AdaBoost
    ab_regressor = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
    ab_regressor.fit(x_train, y_train)

    # Evaluate performance of Decision Tree regressor
    y_pred_dt = dt_regressor.predict(x_test)
    # 均方误差
    mse = mean_squared_error(y_test, y_pred_dt)
    # 解释方差分
    evs = explained_variance_score(y_test, y_pred_dt)
    print("### Decision Tree Performance ###")
    print("Mean squared error =", round(mse, 2))
    print("Explained variance score =", round(evs, 2))

    # Evaluate performance of AdaBoost
    # Adaboost 算法可以让误差更小，且解释方差分更接近1
    y_predict_ab = ab_regressor.predict(x_test)
    mse = mean_squared_error(y_test, y_predict_ab)
    evs = explained_variance_score(y_test, y_predict_ab)
    print("### Adaboost performance ###")
    print("Mean squared error =", round(mse, 2))
    print("Explained variance score =", round(evs, 2))

    # Plot relative feature importances
    plot_feature_importances(dt_regressor.feature_importances_, 'Decision Tree regressor', housing_data.feature_names)
    plot_feature_importances(ab_regressor.feature_importances_, 'AdaBoost regressor', housing_data.feature_names)