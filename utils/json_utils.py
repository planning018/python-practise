from flask import json
import demjson

with open('file/demo.json', 'r') as f:
    # 去除转义字符
    info = demjson.decode(f.read())
    info = json.loads(info)
    print(info)