import time
from page.AddBitrhfourth import addbirthforth
import allure

@allure.feature('百度首页')
class Testearch:

    def setup_class(self):      #启动浏览器
        self.baidu_search = addbirthforth()    #初始化页面，自定义baidu_search页面

    @allure.story('测试百度搜索框，输入为selenium')
    @allure.description('进入百度首页，测试百度搜索框功能，输入内容为selenium')
    @allure.title('testcast1:搜索selenium')
    def test_case1(self):       #第一个测试用例
        self.addbirthforth.next_1()

    def teardown_class(self):
        time.sleep(1)
        self.baidu_search.web_quit()        #调用初始化的baidu_search，调用父类Baidu_Page类的父类base_lelment的web_quit方法