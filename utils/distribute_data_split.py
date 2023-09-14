import csv


def split_csv(file_path, num_files):
    """
    Split a CSV file into multiple files.

    Parameters:
    file_path (str): The path to the csv file to split.
    num_files (int): The number of split files.
    """

    # 保存所有文件句柄的列表
    writers = [None] * num_files
    output_files = [None] * num_files
    file_counter = 0

    with open(file_path, 'r') as f:
        csvreader = csv.reader(f)
        headers = next(csvreader)

        # 写入每一行
        for i, row in enumerate(csvreader):
            if writers[i % num_files] is None:
                file_counter += 1
                output_files[i % num_files] = open(f"{file_path.rsplit('.', 1)[0]}_{file_counter}.csv", "w", newline='')
                writers[i % num_files] = csv.writer(output_files[i % num_files])
                writers[i % num_files].writerow(headers)

            writers[i % num_files].writerow(row)

    # 关闭所有文件
    for output_file in output_files:
        if output_file:
            output_file.close()

# 使用函数
split_csv('/Users/planning/Documents/work_data/Short/20230725/9/shortdistance_hour_model.csv', 5)
