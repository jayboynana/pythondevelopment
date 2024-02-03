# 读写二进制文件
def main():
    try:
        with open('end_of_Summer.jpg','rb') as f1:
            img = f1.read()
            print(type(img))
        with open('夏末.jpg','wb') as f2:
            f2.write(img)
    except FileNotFoundError:
        print('File not found!!')
    except IOError:
        print('IO Error!!')
    print('Finished!!')

if __name__ == '__main__':
    main()