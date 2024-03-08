import schedule
import time
import subprocess


def job():
    subprocess.run(['/home/conda/data/bin/python3', '/xxx/gpu_monitor.py'])

# 每分钟执行一次任务
schedule.every(1).minutes.do(job)

# 在后台运行，持续执行定时任务
while True:
    schedule.run_pending()
    time.sleep(1)
