# 替换

import re

def main():
    sentence = '你丫是傻叉吗? 我操.fuck you!'
    pure = re.sub('[操艹]|shit|fuck|[sb]|傻[比逼叉]|[煞笔]','*',sentence,flags=re.IGNORECASE)
    print(pure)

if __name__ == '__main__':
    main()