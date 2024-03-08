import logging
import os.path

import requests
from datetime import datetime
import pandas as pd


def monitor_gpu(host, filename):
    try:
        url = "http://" + host + ":9400/metrics"
        response = requests.request("GET", url)
        response_content = response.content.decode("utf-8")
        lines = response_content.split('\n')
        target_line_list = []
        # 找出 GPU 利用率
        for line in lines:
            if line.startswith('DCGM_FI_DEV_GPU_UTIL{gpu'):
                target_line_list.append(line)

        result = []
        for data in target_line_list:
            # 根据空格将数据分割为两部分：属性和利用率数值
            attr, utilization = data.rsplit(' ', 1)
            # 提取属性部分
            attributes = attr.split(',')
            attributes_dict = {}
            for attribute in attributes:
                key, value = attribute.split('=')
                attributes_dict[key] = value.strip('"')
            result.append([datetime.now().strftime("%Y%m%d-%H:%M:%S"), attributes_dict['DCGM_FI_DEV_GPU_UTIL{gpu'], utilization])

        result_df = pd.DataFrame(result, columns=['Time', 'GPU Index', 'Utilization'])

        if os.path.exists(filename):
            result_df.to_csv(filename, mode='a', header=False)
        else:
            result_df.to_csv(filename)
        logging.info("monitor gpu success")
    except OSError as reason:
        logging.info("Error trigger train : %s" % str(reason))


if __name__ == '__main__':
    dt = datetime.now().strftime("%Y%m%d")
    filename = "Node_xx1_GPU_Utilization_{dt}.csv".format(dt=dt)
    monitor_gpu('xxx', filename)

    filename = "Node_xx2_GPU_Utilization_{dt}.csv".format(dt=dt)
    monitor_gpu('xxx', filename)