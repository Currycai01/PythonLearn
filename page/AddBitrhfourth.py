from selenium.webdriver.common.by import By
from Base.base import Base
from selenium import webdriver

class addbirthforth(Base):

    page_url = 'test'     #定义本页面的url
    search_btn1=(By.XPATH,'//*[@id="main_body"]/div/footer/div/button[1]/span')
    search_input=(By.ID,'kw')       #查询框的查找


    def __init__(self):     #初始化Baidu.Page
        driver = webdriver.Chrome()       #初始化浏览器为谷歌浏览器
        Base.__init__(self,driver)      #初始化父类
        self.go_page(self.page_url)     #初始化BaiduPage实例，进入url

    def next_1(self):
        self.ele_click(*self.search_btn1)