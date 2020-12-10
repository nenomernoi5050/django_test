import random
import requests
import news_test_project.user_agent_list as ua
import pymysql


# https://yadi.sk/d/vRswyVOVdzOf7Q
# https://yadi.sk/d/WYEzlpCxXwOIes?w=1
# https://yadi.sk/d/nnDYcaxzfWuaoC
# 14


def find_db(find):
    query = f"SELECT COUNT(*) FROM yandex  WHERE url='{find}';"
    cursor.execute(query)
    result = cursor.fetchone()
    if result[0] == 0:
        return False
    else:
        return True

def set_db(url):

    query = f"INSERT INTO yandex (url) VALUES (%s);"
    cursor.execute(query,(url))
    connect.commit()

def insert_true(url):
    query = f"INSERT INTO true_result (url) VALUES (%s);"
    cursor.execute(query,(url))
    connect.commit()


def get_url(res):
    url = "https://yadi.sk/d/{}?w=1".format(res)
    if find_db(url) == False:
        resp = requests.get(url,  ua.rand_user_agent())
        if resp.status_code == 200:
            insert_true(url)
        else:
            print(url)
            set_db(url)
    else:
        print(f'{url} - существует')



def main_func(quantity, lenght,chars):
    for i in range(quantity):
        res = ''
        for n in range(lenght):
            res +=random.choice(chars)
        get_url(res)


if __name__ == '__main__':
    connect = pymysql.connect(host='localhost', user='root', password='', db='yandex', port=3306)
    cursor = connect.cursor()
    quantity = 10000  # Количество ссылок
    lenght = 14  # Длина ссылки
    chars = '-_abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    main_func(quantity, lenght, chars)
