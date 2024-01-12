"""
构建一个索引映射，列出词出现的位置
"""

import re
import sys

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='uft-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, cloumn_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

# 按字母顺序显示
for word in sorted(index, key=str.upper):
    print(word, index[word])