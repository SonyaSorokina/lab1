from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://omgtu.ru/ecab/persons/index.php?b=16'
    try:
        page = requests.get(url)
        print(page.status_code)
        soup = BeautifulSoup(page.text, 'html.parser')
    except:
        print('Error')
        return -1

    block = soup.findAll('div', id='pagecontent')
    description = ''
    finaldescription = ''

    for data in block:
        if data.find('a'):
            description = str(data.text).replace('\n','')

    l = description.split(' ')
    l2 = list()
    x = l.index('Савва')

    for i in range(x, len(l)):
        if (l[i]!='') or (l[i]!=' '):
            l2.append(l[i])
    count = 0
    stroka = list()

    for i in l2:
        count = count+1
        if count < 4:
            stroka.append(i)
        else:
            finaldescription = finaldescription + ' '.join(stroka) + '\n'
            count = 0
            stroka.clear()

    print(finaldescription)
    f = open('text.txt', 'w')
    f.write(finaldescription)
    f.close()