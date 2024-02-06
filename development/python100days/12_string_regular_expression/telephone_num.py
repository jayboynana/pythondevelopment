# 从一段文字中提取出国内手机号码

import re

def main():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''

    find_list = re.findall(pattern,sentence)
    # find_list = pattern.findall(sentence)
    print(find_list)
    print('-------------')

    for temp in pattern.finditer(sentence):
        print(temp.group())
        # print(temp)

    print('-------------')

    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence,m.end())

if __name__ == '__main__':
    main()