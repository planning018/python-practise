import os
import pandas as pd
from datetime import datetime
import json


def calculate_gpu_utilization(file_path, gpu_indices):
    df = pd.read_csv(file_path)
    result = {}
    for index in gpu_indices:
        gpu_data = df[df["GPU Index"] == index]
        utilization_mean = gpu_data['Utilization'].mean().round(2)
        result[index] = utilization_mean
    return result


gpu_indices = {
    "Node_11": [0, 1, 2, 3],
    "Node_12": [0, 1, 2, 3, 4, 5],
}

dt = datetime.now().strftime("%Y%m%d")
file_paths = {
    "Node_11": "Node_11_GPU_Utilization_{dt}.csv".format(dt=dt),
    "Node_12": "Node_12_GPU_Utilization_{dt}.csv".format(dt=dt)
}

temp_result = []
for node, indices in gpu_indices.items():
    file_path = os.path.join(file_paths[node])
    util_result = calculate_gpu_utilization(file_path, indices)
    temp_result.append(util_result)

temp_result[1] = {k+4: v for k, v in temp_result[1].items()}

formatted_result = [
    f"GPU{i}: {utilization:.2f}%" for i, utilization in temp_result[0].items()
] + [
    f"GPU{i}: {utilization:.2f}%" for i, utilization in temp_result[1].items()
]
print(formatted_result)
json_result = json.dumps({f"GPU{i}": utilization.split(":")[1].strip() for i, utilization in enumerate(formatted_result)})
print(json_result)

