import json

import pymysql
import requests

def get_one_page(url):
        headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            text = response.content.decode('utf-8')
            return text
        return None


def get_real_content(html):
    if html and len(html) > 128:
        html1 = html.split('(')[1:][0]
        html1 = html1.replace(');', '')
        return html1
    return None


def main():
    host = '127.0.0.1'
    user = 'root'
    password = '778227655'
    database = 'mogujie'
    port = 3306
    db = pymysql.connect(host, user, password, database, charset='utf8', port=port)
    cursor = db.cursor()
    for k in range(7, 2000):
        url = 'https://list.mogujie.com/search?callback=jQuery21108482104248020108_1540373298633&_version=8193&ratio=3%3A4&cKey=15&page='+ str(k+1)+str('&sort=pop&ad=0&fcid=51894&action=magic')
        html = get_one_page(url)
        html_content = get_real_content(html)
        result = json.loads(html_content)
        docs = result['result']['wall']['docs']
        for i in range(len(docs)):
            title = result['result']['wall']['docs'][i]['title']
            orgPrice = result['result']['wall']['docs'][i]['orgPrice']
            sale = result['result']['wall']['docs'][i]['sale']
            cfav = result['result']['wall']['docs'][i]['cfav']
            price = result['result']['wall']['docs'][i]['price']
            tradeItemId = result['result']['wall']['docs'][i]['tradeItemId']
            sql = """insert into makeups (title,orgPrice,sale,cfav,price,tradeItemId) values('%s','%s','%s','%s','%s','%s')""" % (title, orgPrice, sale, cfav, price, tradeItemId)
            print(sql)
            cursor.execute(sql)
            db.commit()
            if result['result']['wall']['isEnd']:
                return None
    return None

if __name__ == '__main__':
    main()