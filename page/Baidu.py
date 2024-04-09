from selenium.webdriver.common.by import By
from Base.base import Base
from selenium import webdriver

class BaiduPage(Base):

    #构造方法与实例属性
    def __init__(self):     #初始化Baidu.Page
        driver = webdriver.Chrome()       #实例属性，初始化浏览器为谷歌浏览器driver
        super().__init__(driver)      #传参浏览器driver，初始化父类，才可以调用父类的方法

    #查找元素的路径
    #左上角按钮
    xinwen = '//*[@id="s-top-left"]/a[1]'
    hao123 = '//*[@id="s-top-left"]/a[2]'
    ditu = '//*[@id="s-top-left"]/a[3]'
    tieba = '//*[@id="s-top-left"]/a[4]'
    shiping = '//*[@id="s-top-left"]/a[5]'
    tupian = '//*[@id="s-top-left"]/a[6]'
    wangpan = '//*[@id="s-top-left"]/a[7]'
    wenku = '//*[@id="s-top-left"]/a[8]'
    gengduo = '//*[@id="s-top-left"]/div/a'

    #右上角按钮
    setting = 's-usersetting-top'
    set_search = '//*[@id="s-user-setting-menu"]/div/a[1]/span'
    login = 's-top-loginbtn'
    loginexit = 'TANGRAM__PSP_25__closeBtn'

    #输入框
    input = ['id','kw']
    button = 'su'

    #百度热搜
    reshou = '//*[@id="s-hotsearch-wrapper"]/div/a[1]/div/i[1]'
    change = '//*[@id="hotsearch-refresh-btn"]/i'
    reshou1 = '//*[@id="hotsearch-content-wrapper"]/li[1]/a'

    def go_page(self):
        page_url = 'https://www.baidu.com'  # 定义本页面的url
        super().go_page(page_url)     #初始化BaiduPage实例，进入url

    def click_xinwen(self):    #查找新闻按钮并点击
        super().click("xpath",self.xinwen)

    def click_hao(self):    #查找hao123按钮并点击
        super().click("xpath",self.hao123)

    def click_ditu(self):    #查找地图按钮并点击
        super().click("xpath",self.ditu)

    def click_tieba(self):    #查找贴吧按钮并点击
        super().click("xpath",self.tieba)

    def click_shiping(self):    #查找视频按钮并点击
        super().click("xpath",self.shiping)

    def click_tupian(self):    #查找图片按钮并点击
        super().click("xpath",self.tupian)

    def click_wangpan(self):    #查找网盘按钮并点击
        super().click("xpath",self.wangpan)

    def click_wenku(self):    #查找文库按钮并点击
        super().click("xpath",self.wenku)

    def click_gengduo(self):    #查找更多按钮并点击
        super().click("xpath",self.gengduo)

    def click_setting(self):    #查找设置按钮并点击
        super().click("id",self.setting)

    def click_set_search(self):
        super().click('xpath',self.set_search)

    def click_login(self):      #查找登录按钮并点击
        super().click("id",self.login)

    def login_exit(self):       #查找退出登录按钮并点击
        super().click("id",self.loginexit)


    def click_input(self):
        super().click(self.input[0],self.input[1])

    def click_search(self):
        super().click("id",self.button)

    #输入关键字查询
    def senk_keys_input(self,data):
        super().input_data(self.input[0],self.input[1],data)







    '''
    def clear_input(self):      #构造本页面的清除输入框函数，调用父类的ele_clear()
        self.ele_clear(*self.search_input)

    def input_text(self,text):      #构造本页面的输入函数,调用父类的send_key
        self.send_key(text,*self.search_input)

    def click_btn(self):        #构造本页面的点击函数,调用父类的ele_click()
        self.ele_click(*self.search_btn)
    '''