from math import sqrt

def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    files_names = ['file1.txt', 'file2.txt', 'file3.txt']
    files = []
    try:
        for file_name in files_names:
            files.append(open(file_name,'w',encoding='utf-8'))
        for num in range(1,10000):
            if is_prime(num):
                if num < 100:
                    files[0].write(str(num) + '\n')
                elif num < 1000:
                    files[1].write(str(num) + '\n')
                else:
                    files[2].write(str(num) + '\n')
    except IOError as ex:
        print(ex)
        print('errors in writing!!')
    finally:
        for file in files:
            file.close()
    print('Finished!!')

if __name__ == '__main__':
    main()

