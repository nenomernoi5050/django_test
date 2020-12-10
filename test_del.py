import random
import requests
import news_test_project.user_agent_list as ua
import pymysql
import asyncio
import aiohttp


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


async def get_url(res):

    char_last_simbol = 'wgAQ'
    char_end = random.choice(char_last_simbol)
    url = "https://yadi.sk/d/{}{}?w=1".format(res, char_end)
    # if find_db(url) == False:
        # resp = requests.get(url,  ua.rand_user_agent())
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                insert_true(url)
            else:
                print(url)

    # else:
    #     print(f'{url} - существует')



async def main_func(quantity, lenght,chars):
    for i in range(quantity):
        res = ''
        for n in range(lenght):
            res +=random.choice(chars)
        await get_url(res)



if __name__ == '__main__':

    connect = pymysql.connect(host='localhost', user='root', password='', db='yandex', port=3306)
    cursor = connect.cursor()
    quantity = 1000  # Количество ссылок
    lenght = 13  # Длина ссылки
    chars = '-_abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    futures = [main_func(quantity, lenght, chars)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    # main_func(quantity, lenght, chars)
