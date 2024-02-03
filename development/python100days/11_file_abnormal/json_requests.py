import json
import requests

def main():
    url = 'https://apis.tianapi.com/bfrsum/index?key=292ea81043ebd19fb74ffcafeb68d3e2&height=180&weight=58&age=22&sex=1'
    response = requests.get(url)
    data = json.loads(response.text)
    for item in data.items():
        print(item)

if __name__ == '__main__':
    main()