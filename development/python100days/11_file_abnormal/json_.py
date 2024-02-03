import json

def main():

    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        # with open('mydict.json', 'w',encoding='utf-8') as f:
        #     json.dump(mydict,f)
        with open('mydict1.json', 'w',encoding='utf-8') as f:
            str_ = json.dumps(mydict)
            f.write(str_)
    except IOError:
        print('IO Error!!')
    print('Finished!!')

if __name__ == '__main__':
    main()