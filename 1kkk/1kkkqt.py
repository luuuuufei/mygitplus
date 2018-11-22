from io import BytesIO

from PIL import Image

# 将获取到的500张验证码切割成16*500张小验证码并命名
def get_geetest_image():
    for x in range(500):
        screenshot = Image.open('./1kkk/%s'%("%d.png"%(x)))
        for i in range(4):
            crop_img = screenshot.crop((76 * i, 0, 76 * (i + 1), 76))
            file_name = '%d_%d.png' % ((x), (i + 1))
            crop_img.save('./1kkkx/' + file_name)
            print(file_name)



if __name__ == '__main__':
    get_geetest_image()