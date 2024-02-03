# def main():
#     try:
#         with open('./致橡树.txt','r',encoding='utf-8') as file:
#             print(file.read())
#     except FileNotFoundError:
#         print('the file is not found!!')
#     except LookupError:
#         print('unknown encoding!!')
#     except UnicodeDecodeError:
#         print('Decoding error!!')
import time


def main():
    # with open('致橡树.txt','r',encoding='utf-8') as f:
    #     for line in f:
    #         print(line,end='')
    #         time.sleep(0.5)
    # print()

    with open('致橡树.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line,end='')

if __name__ == '__main__':
    main()