import requests

print('import api')
def get_random_advise():
    response = requests.get('http://fucking-great-advice.ru/api/random')
    json = response.json()
    return json['text']

if __name__ == '__main__':
    ad = get_random_advise()
    print(ad)
