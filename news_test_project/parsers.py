import requests
import codecs
from bs4 import BeautifulSoup as BS
import csv
import user_agent_list as ua




def site_126(url):
    http = 'https:'
    data = []
    errors = []
    resp = requests.get(url, ua.rand_user_agent())
    print(resp)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        card_vac = soup.find_all('div', class_='sr-2-list-item-n-r')

        for div in card_vac:
            title = div.find('div', class_='sr-2-list-item-n-title').text
            href = div.find('div', class_='sr-2-list-item-n-title').a['href']
            firma_list = div.find('div', class_='sr-2-item-address').text

            data.append({'title':title.replace('\n', ''),
                         'url':http + href,
                         'description': title.replace('\n', ''),
                         'company':firma_list.strip(),
                         })
    else:
        errors.append({'url': url, 'text': resp.text})

    print(data)
    with open('../new_file_126.csv', 'w', newline ='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)

    h = codecs.open('../error_126.txt', 'w', 'utf-8')
    h.write(str(errors))
    h.close()


def site_joblab(url):
    http = 'https://joblab.ru/'
    data = []
    errors = []
    resp = requests.get(url, ua.rand_user_agent())

    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        card_vac = soup.find_all('td', class_='td-to-div')

        for div in card_vac:
            title = div.find('p', class_='prof')
            if title != None:
                title = div.find('p', class_='prof').text
                href = div.find('p', class_='prof').a['href']
                firma_list = div.find('p', class_='org').text
                city = div.find('td', class_='td-to-div-city')
                description = div.find('p', class_='prof').text

                data.append({'title': title,
                             'url': href,
                             'description': description,
                             'company': firma_list,
                             })

    else:
        errors.append({'url': url, 'text': resp.text})


    with open ('../new_joblab.csv', 'w', newline ='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)

    h = codecs.open('../error_joblab.txt', 'w', 'utf-8')
    h.write(str(errors))
    h.close()


def site_1777(url):
    http = 'https:'
    data = []
    errors = []
    resp = requests.get(url, ua.rand_user_agent())
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        card_vac = soup.find_all('table', class_='view_ads')
        for div in card_vac:
            title = div.find('div', class_='view_doljnost').text
            href = div.find('div', class_='view_doljnost').a['href']
            firma_list = div.find('div', class_='view_firma').text
            data.append({'title':title,
                         'url':http + href,
                         'description': title,
                         'company':firma_list,
                         })
    else:
        errors.append({'url': url, 'text': resp.text})

    with open('../new_file_1777.csv', 'w', newline = '') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)

    h = codecs.open('../error_1777.txt', 'w', 'utf-8')
    h.write(str(errors))
    h.close()