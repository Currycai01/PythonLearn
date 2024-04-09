from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import  webdriver
from selenium.webdriver.common.by import By

class Base:

    #初始化Base实例，需要传参driver
    def __init__(self,driver):
        self.driver=driver    #实例属性driver

    #前往某个页面,需要传参url
    def go_page(self,url):
        self.driver.get(url)

    #浏览器操作
    #最大化窗口
    def max_window(self):
        self.driver.maximize_window()

    #获取当前页面标题
    def get_title(self):
        return self.driver.title

    #切换到旧窗口
    def Current_handel(self):
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[0])

    #查找元素功能
    def FindElement(self, type, value):
        if type == "id":
            el = self.driver.find_element(By.ID,value)
        elif type == "name":
            el = self.driver.find_element(By.NAME,value)
        elif type == "class_name":
            el = self.driver.find_element(By.CLASS_NAME,value)
        elif type == "tag_name":
            el = self.driver.find_element(By.TAG_NAME,value)
        elif type == "link_text":
            el = self.driver.find_element(By.LINK_TEXT,value)
        elif type == "partial_link_text":
            el = self.driver.find_element(By.PARTIAL_LINK_TEXT,value)
        elif type == "xpath":
            el = self.driver.find_element(By.XPATH,value)
        elif type == "css_selector":
            el = self.driver.find_element(By.CSS_SELECTOR,value)

        return el

    # 点击元素功能
    def click(self, type, value):
        el = self.FindElement(type, value)
        el.click()

    # 对定位到元素进行输入
    def input_data(self, type, value, data):
        el = self.FindElement(type, value)
        el.send_keys(data)

    #鼠标悬停
    def cover(self,type,value):
        el = self.FindElement(type,value)
        ActionChains(self).move_to_element(el).perform()

    # Base实例退出浏览器
    def web_quit(self):
        self.driver.quit()

    '''
    #Base实例查找元素,传入地址loc,返回界面元素
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    #Base实例查找元素，并输入文本
    def send_key(self,text,*loc):
        self.find_element(*loc).send_keys(text)

    #Base实例查找元素并清除输入框
    def ele_clear(self,*loc):
        self.find_element(*loc).clear()

    #Base实例查找元素并进行点击
    def ele_click(self,*loc):
        self.find_element(*loc).click()

    #Base实例获取页面标题
    def page_title(self):
        return self.driver.title

 

    def wait_title_content(self,title):
        WebDriverWait(self.driver,5).until(EC.title_contains(title))
    '''