"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

import re

def main():
    username = input('please enter your username: ')
    qq_code = input('please enter your qq code:')

    m1 = re.match(r'^[a-zA-Z0-9_]{6,20}$',username)
    if not m1:
        print('invalid username!')

    m2 = re.match(r'^[1-9]\d{4,12}',qq_code)
    if not m2:
        print('invalid QQ!')

    if m1 and m2:
        print('valid!')

if __name__ == '__main__':
    main()