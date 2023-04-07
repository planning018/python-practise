import pandas as pd
import numpy as np

# 准备数据
df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                   ('bird', 'Psittaciformes', 24.0),
                   ('mammal', 'Carnivora', 80.2),
                   ('mammal', 'Primates', np.nan),
                   ('mammal', 'Carnivora', 58)],
                  index=['falcon', 'parrot', 'lion',
                         'monkey', 'leopard'],
                  columns=('class', 'order', 'max_speed'))


def groupby_object_create():
    print(df)
    print("=======================================================")
    # 创建分组对象
    grouped = df.groupby('class')
    # grouped = df.groupby('order', axis='columns') # 按行
    # grouped = df.groupby(['class', 'order'])  # 多个
    # 查看单个分组的内容
    print(grouped.get_group('bird'))    # 查看鸟类分组内容

    # 以下使用学生成绩表数据
    # 按索引奇偶行分组 True False 两组
    df.groupby(lambda x: x % 2 == 0)
    # 按前后50个分组  True False 两组
    df.groupby(lambda x: x >= 50)
    # 列名包含 Q 的分成一组
    df.groupby(lambda x: 'Q' in x, axis=1).sum()

    # 传入字典完成分组，键为原索引名，值为分组名
    # 可实现只对部分分组
    (
        df.set_index('team')
            .groupby({'A': 'A组', 'B': 'B组'})
            .sum()
    )

    # 以下使用学生成绩表数据｜列计算值
    # 按索引奇偶行分组 True False 两组
    df.groupby(df.index % 2 == 0)  # 同上
    # 按姓名首字母分组
    df.groupby(df.name.str[0])
    # 按 AB-其他团队 分组
    df.groupby(df.team.isin(['A', 'B']))
    # 按姓名第一个字母和第二个字母分组
    df.groupby([df.name.str[0], df.name.str[1]])
    # 按日期小时分组
    df.groupby([df.time.date, df.time.hour])

    # 按日期中的年份分组
    df.groupby(df.time.apply(lambda x: x.year)).count()

    # 姓名首字母元音辅音分组｜使用函数
    def get_letter_type(letter):
        if letter[0].lower() in 'aeiou':
            return 'vowel'
        else:
            return 'consonant'
    # 使用函数
    df.set_index('name').groupby(get_letter_type).sum()

    # 使用了 python 表达式和列名｜多种方法混用
    df.groupby([lambda x: x >= 50, 'team']).sum()

    # 直接使用分组方法
    df.pipe(pd.DataFrame.groupby, 'team').sum()


def groupby_func(df):
    # 分组统计方法
    df.groupby('team').describe()  # 描述性统计
    df.groupby('team').sum()  # 求和
    df.groupby('team').count()  # 每组数量，不包括缺失值
    df.groupby('team').max()  # 求最大值
    df.groupby('team').min()  # 求最小值
    df.groupby('team').size()  # 分组数量
    df.groupby('team').mean()  # 平均值
    df.groupby('team').median()  # 中位数
    df.groupby('team').std()  # 标准差
    grouped = df.groupby('team').var()  # 方差
    grouped.corr()  # 相关性系数
    grouped.sem()  # 标准误差
    grouped.prod()  # 乘积
    grouped.cummax()  # 每组的累计最大值
    grouped.cumsum()  # 累加
    grouped.mad()  # 平均绝对偏差

    # 特殊方法
    df.groupby('team').first()  # 组内第一个
    df.groupby('team').last()  # 组内最后一个
    df.groupby('team').ngroups  # 5 分组数
    df.groupby('team').ngroup()  # 分组序号
    # 库姆计数，按组对成员标记, 支持正排倒排
    # 返回每个元素在所在组的序号的序列
    grouped.cumcount(ascending=False)

    # 时序重采样
    idx = pd.date_range('1/1/2000', periods=100, freq='T')
    df = pd.DataFrame(data=1 * [range(2)],
                      index=idx,
                      columns=['a', 'b'])
    # 三个周期一聚合（一分钟一个周期）
    df.groupby('a').resample('3T').sum()
    # 30 秒一分组
    df.groupby('a').resample('30S').sum()
    # 每月
    df.groupby('a').resample('M').sum()
    # 以右边时间点为标识
    df.groupby('a').resample('3T', closed='right').sum()



if __name__ == '__main__':
    groupby_object_create()