import ruamel.yaml

with open('shaoshuren.yaml', 'r') as file:
    data = ruamel.yaml.safe_load(file)

var1 = 'DOMAIN-SUFFIX,tensorflow.org,🚀节点选择'
var2 = 'DOMAIN-SUFFIX,chatbot.theb.ai,🚀节点选择'
var3 = 'DOMAIN-SUFFIX,chat.openai.com,🚀节点选择'


# 遍历 rules 列表，找出需要插入 var1 的位置
for i in range(len(data["rules"])):
    if data["rules"][i] == "DOMAIN-SUFFIX,dl.google.com,🚀节点选择":
        # 将 var1 插入到该位置之后
        data["rules"].insert(i+1, var1)
        data["rules"].insert(i+2, var2)
        data["rules"].insert(i+3, var3)
        break

# 将更新后的数据写入 YAML 文件
with open('shaoshuren.yaml', 'w', encoding='utf-8') as file:
    ruamel.yaml.dump(data, file, allow_unicode=True)
