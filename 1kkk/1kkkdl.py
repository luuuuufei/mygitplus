import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



EMAIL = '77827655@qq.com'
PASSWORD = '778227655'
BORDER = 6
INIT_LEFT = 60


class page_dl():
    def __init__(self):
        self.url = 'http://www.1kkk.com/login/'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    # def __del__(self):
    #     self.browser.close()


    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.name, 'txt_name')))
        password = self.wait.until(EC.presence_of_element_located((By.name, 'txt_password')))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gt_cut_fullbg.gt_show')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)


    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        top, bottom, left, right = self.get_position()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(screenshot)
        return screenshot



    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha


if __name__ == '__main__':
    page_dl()