import json

import pymysql
import requests
from lxml import etree




def main():
    host = '127.0.0.1'
    user = 'root'
    password = '778227655'
    database = 'bjx'
    port = 3306
    db = pymysql.connect(host, user, password, database, charset='utf8', port=port)
    cursor = db.cursor()
    response = requests.get('http://www.resgain.net/xmdq.html')
    response = etree.HTML(response.text)
    for i in range(104, 436):
        xing = response.xpath('/html/body/div[3]/div/div/div[2]/a[' + str(i) + ']/text()')[0].replace('姓名字大全','')
        title = response.xpath('/html/body/div[3]/div/div/div[2]/a[' + str(i) + ']/@title')[0]
        link = response.xpath('/html/body/div[3]/div/div/div[2]/a[' + str(i) + ']/@href')[0]
        # xing = str(xing)
        # print(xing, title, link)
        a = link.replace('.html', '')
        # print(a)
        for n in range(1, 11):
            response1 = requests.get('http:' + a + '_' + str(n) + '.html')
            # response1 = requests.get('http://zhao.resgain.net/name_list_'+str(n)+'.html')
            # print(response1.text)
            print(n)
            response11 = etree.HTML(response1.text)
            for x in range(1, 300):
                try:
                    ming = response11.xpath('/html/body/div[3]/div[2]/div[1]/div/a[' + str(x) + ']/text()')[0]
                    # print(ming[0])
                except:
                    pass
                else:
                    sql = """insert into wjx (xing,ming) values('%s','%s')""" % (xing,ming)
                    print(sql)
                    cursor.execute(sql)
                    db.commit()

if __name__ == '__main__':
    main()