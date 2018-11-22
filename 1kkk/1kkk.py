import requests


def get_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None

# 获取到的验证码图片保存到本地
def write_img(image,filename):
    with open('./1kkk/%s' % filename, 'wb')as f:
        f.write(image)

# 循环获取500张验证码
def main():
    for i in range(500):
        url = "http://www.1kkk.com//image3.ashx?t="+str(i)
        image = get_page(url)
        write_img(image, str(i)+'.png')
        print(i)

if __name__ == '__main__':
    main()