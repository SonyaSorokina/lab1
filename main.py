from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://omgtu.ru/ecab/persons/index.php?b=16'
    page = requests.get(url)
    print(page.status_code)

    soup = BeautifulSoup(page.text, 'html.parser')
    block = soup.findAll('div', class_='main__content')
    description = ''
    for data in block:
        if data.find('a'):
            description = data.text
    print(description)
    f = open('text.txt', 'w')
    f.write(description)
parse()