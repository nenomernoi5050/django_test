import requests
import codecs
from bs4 import BeautifulSoup as BS
import csv
import user_agent_list as ua

import urllib3

def img_save(url, title):
    http = urllib3.PoolManager()


    req = http.request('GET', url)

    with open("../../images/{}.jpg.".format(title), "wb") as f:
        f.write(req.data)


def card_item(url):
    resp = requests.get(url, ua.rand_user_agent())
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        sku = soup.find('span', class_='sku').text
        info = soup.find('div', class_='product-info')
        desc = soup.find('div', id='tab-description').contents[0:10]
        post_instagramm = soup.find('div', class_='sbi-embed-wrap').contents
        print(post_instagramm)

        price = info.find('bdi').contents[1]
        info_2 = soup.find('div', id='tab-additional_information')
        size = info_2.find('td', class_='woocommerce-product-attributes-item__value').p.text

        card_product = soup.find('div', class_='product-thumbnails')
        imges = card_product.find_all('div', class_='col')
        i = 1
        for res in imges:
            img = res.find('img', class_='attachment-woocommerce_thumbnail')
            name = "{}-{}".format(sku, i)
            i += 1
            if img.get('data-src', 0) == 0:
                pass
                # img_save(img['src'], name)
            else:
                pass
                # img_save(img['data-src'], name)







card_item('https://www.littleforbig.com/product/daddys-princess-lacy-dress/')

def sitelittle_for_big(url):
    http = 'https://joblab.ru/'
    data = []
    errors = []
    next_page = True
    i = 1
    while next_page == True:
        resp = requests.get(url+str(i), ua.rand_user_agent())

        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            card_product = soup.find_all('div', class_='product-small')
            pagin = soup.find('a', class_='next')
            if pagin != None:
                i += 1
            else:
                next_page = False

            for div in card_product:
                title = div.find('p', class_='product-title').text
                href = div.find('p', class_='product-title').a['href']
                img = div.find('img', class_='attachment-woocommerce_thumbnail')
                img_save(img['data-src'], title)
                data.append({'title': title,
                             'url': href,
                             'img': img['data-src'],
                             # 'company': firma_list,
                             })

        else:
            errors.append({'url': url, 'text': resp.text})
            i += 1
    print(data)
    return data, errors


# sitelittle_for_big('https://www.littleforbig.com/product-category/clothes/adult-onesie-bodysuits/onesie-bodysuit-skirt-sets/page/')

def site_126(url):

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
                         'url': href,
                         'description': title.replace('\n', ''),
                         'company':firma_list.strip(),
                         })
    else:
        errors.append({'url': url, 'text': resp.text})
    return data, errors
    # print(data)
    # with open('../new_file_126.csv', 'w', newline ='') as file:
    #     csv_writer = csv.writer(file)
    #     csv_writer.writerow(data)
    #
    # h = codecs.open('../error_126.txt', 'w', 'utf-8')
    # h.write(str(errors))
    # h.close()


def site_joblab(url):
    http = 'https://joblab.ru/'
    data = []
    errors = []
    resp = requests.get(url, ua.rand_user_agent())
    print(resp)
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
                             'url': http + href,
                             'description': description,
                             'company': firma_list,
                             })

    else:
        errors.append({'url': url, 'text': resp.text})

    return data, errors
    # with open ('../new_joblab.csv', 'w', newline ='') as file:
    #     csv_writer = csv.writer(file)
    #     csv_writer.writerow(data)
    #
    # h = codecs.open('../error_joblab.txt', 'w', 'utf-8')
    # h.write(str(errors))
    # h.close()


def site_1777(url):
    http = 'https:'
    data = []
    errors = []
    resp = requests.get(url, ua.rand_user_agent())
    print(resp)
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
    return data, errors
    # with open('../new_file_1777.csv', 'w', newline = '') as file:
    #     csv_writer = csv.writer(file)
    #     csv_writer.writerow(data)
    #
    # h = codecs.open('../error_1777.txt', 'w', 'utf-8')
    # h.write(str(errors))
    # h.close()