# 拆分字符串

import re

def main():
    sentence = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[,.，。]',sentence)
    print(sentence_list)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

if __name__ == '__main__':
    main()