import time

import pytest

from page.Baidu import BaiduPage
import allure

@allure.feature('百度首页')
class Testearch:

    baidu_search = BaiduPage()

    def setup_class(self):      #启动浏览器
        #baidu_search = BaiduPage() #初始化页面，自定义baidu_search页面
        self.baidu_search.go_page()
        self.baidu_search.max_window()
        time.sleep(2)

    @pytest.mark.skip
    @allure.story('测试点击新闻跳转')
    def test1(self):
        self.baidu_search.click_xinwen()
        time.sleep(2)
        self.baidu_search.Current_handel()

    @pytest.mark.skip
    @allure.story('测试点击hao123跳转')
    def test2(self):
        self.baidu_search.click_hao()
        time.sleep(2)
        self.baidu_search.Current_handel()

    @allure.story('测试点击地图跳转')
    def test3(self):
        self.baidu_search.click_ditu()
        time.sleep(2)
        print(self.baidu_search.get_title())
        self.baidu_search.Current_handel()

    @pytest.mark.skip
    @allure.story('测试点击贴吧跳转')
    def test4(self):
        self.baidu_search.click_tieba()
        time.sleep(2)
        self.baidu_search.Current_handel()

    @pytest.mark.skip
    @allure.story('测试点击视频跳转')
    def test5(self):
        self.baidu_search.click_shiping()
        time.sleep(2)
        self.baidu_search.Current_handel()

    @pytest.mark.skip
    @allure.story('测试点击图片跳转')
    def test6(self):
        self.baidu_search.click_tupian()
        time.sleep(2)
        self.baidu_search.Current_handel()

    @pytest.mark.skip
    @allure.story('测试点击网盘跳转')
    def test7(self):
        self.baidu_search.click_wangpan()
        time.sleep(2)
        self.baidu_search.Current_handel()

    @pytest.mark.skip
    @allure.story('测试点击文库跳转')
    def test8(self):
        self.baidu_search.click_wenku()
        time.sleep(2)
        self.baidu_search.Current_handel()

    @pytest.mark.skip
    @allure.story('测试点击更多跳转')
    def test9(self):
        self.baidu_search.click_gengduo()
        time.sleep(2)
        self.baidu_search.Current_handel()


    @allure.story('测试点击设置')
    def test10(self):
        self.baidu_search.click_setting()
        time.sleep(2)

    @pytest.mark.skip
    @allure.story('鼠标移动到设置按钮')
    def test_cover(self):
        self.baidu_search.cover('id','s-usersetting-top')

    @allure.story('测试悬浮并点击搜索设置')
    def test_set_search(self):
        self.baidu_search.click_set_search()

    @pytest.mark.skip
    @allure.story('测试点击登录')
    def test11(self):
        self.baidu_search.click_login()
        time.sleep(5)

    @pytest.mark.skip
    @allure.story('测试点击退出登录')
    def test12(self):
        self.baidu_search.login_exit()
        time.sleep(2)

    @pytest.mark.skip
    @allure.story('测试点击输入框')
    def test13(self):
        self.baidu_search.click_input()
        time.sleep(2)

    @pytest.mark.skip
    @allure.story('测试输入内容')
    def test14(self):
        self.baidu_search.senk_keys_input('猫薄荷猫可以吃吗')
        time.sleep(2)

    @pytest.mark.skip
    @allure.story('测试点击搜索')
    def test15(self):
        self.baidu_search.click_search()
        time.sleep(2)

    '''
    @allure.story('测试百度搜索框，输入为selenium')
    @allure.description('进入百度首页，测试百度搜索框功能，输入内容为selenium')
    @allure.title('testcast1:搜索selenium')
    def test_case1(self):       #第一个测试用例
        self.baidu_search.clear_input()     #调用初始化的baidu_search，调用父类Baidu_Page类的clear_input方法
        self.baidu_search.input_text('selenium')        #调用初始化的baidu_search，调用父类Baidu_Page类的input_text方法
        self.baidu_search.click_btn()       #调用初始化的baidu_search，调用父类Baidu_Page类的click_btn方法
        self.baidu_search.wait_title_content('selenium')
        assert self.baidu_search.page_title()=='selenium_百度搜素'

    @allure.story('测试百度搜索框，输入为 自动化测试')
    @allure.description('进入百度首页，测试百度搜素框功能，输入内容为自动化测试')
    @allure.title('tesecase2:搜素 自动化测试')
    def test_case2(self):
        self.baidu_search.clear_input()
        self.baidu_search.input_text('自动化测试')
        self.baidu_search.click_btn()
        self.baidu_search.wait_title_content('自动化测试')
        assert self.baidu_search.page_title()=='自动化测试_百度搜索'

    def teardown_class(self):
        time.sleep(1)
        self.baidu_search.web_quit()
    '''