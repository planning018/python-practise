from datetime import datetime
from elasticsearch7 import Elasticsearch
from elasticsearch7 import helpers
import logging
import json


# ES7 增删改查
def operator_basic():
    es = Elasticsearch("xxx")
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch usage',
        'timestamp': datetime.now()
    }
    resp = es.index(index="yxc-test-index", id=1, document=doc)
    print(resp['result'])

    resp = es.get(index='yxc-test-index', id=1)
    print(resp['_source'])

    es.indices.refresh(index="yxc-test-index")

    resp = es.search(index="yxc-test-index", query={"match_all": {}})
    print("Got %d Hits:" % resp['hits']['total']['value'])
    for hit in resp['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


# ES7 批量写入
def bulk_es(param_list):
    paramList = json.loads(param_list)
    es = Elasticsearch("xxx")
    saveSize = 50
    actions = []
    for param in paramList:
        print("param is :" + str(param))
        action = {
            "_index": "yxc-test-index",
            "_op_type": "index",
            "_type": "_doc",
            "_source": param
        }
        actions.append(action)
        if len(actions) >= saveSize:
            helpers.bulk(es, actions)
            del actions[0:len(actions)]

    if len(actions) > 0:
        helpers.bulk(es, actions)
    print("ES 写入数据 {size} 条".format(size= len(actions)))


if __name__ == '__main__':
    with open('../utils/file-txt/bulk_es.json', 'r') as f:
        paramList = f.read()
    # param_List = json.loads(paramList)
    # print(type(paramList))
    # for param in paramList:
    #     print(param)
    bulk_es(str(paramList))


