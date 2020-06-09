import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage

from TestDatas import common_datas as CD
from TestDatas import login_datas as LD
import ddt
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
import pytest

@pytest.mark.usefixtures("class_demo")
@pytest.mark.usefixtures("function_demo")
@pytest.mark.demo
def test_demo():
    print("HHHHHHHHHHHHHHHHHHHHHH")
    assert False




@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin():

    # @classmethod
    # def setUpClass(cls):
    #     print("=====测试用例执行之前，setUpClass，整个测试类只执行一次")
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.maximize_window()
    #     cls.driver.get(CD.web_login_url)
    #     cls.lg = LoginPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("=====测试用例执行之后，tearDownClass，整个测试类只执行一次")
    #     cls.driver.quit()
    #
    # def setUp(self):
    #     # 前置 访问登录页面
    #     # self.driver = webdriver.Chrome()
    #     # self.driver.get(CD.web_login_url)
    #     # self.lg = LoginPage(self.driver)
    #     pass
    #
    # def tearDown(self):
    #     # 后置
    #     # self.driver.quit()
    #     self.driver.refresh()

    #正常用例 - 登录成功


    #异常用例 - 手机号格式不正确(大于11位，小于11位，不在号码段，用户名或密码为空) ddt
    # @ddt.data(*LD.phone_data)
    @pytest.mark.parametrize("data",LD.phone_data)
    def test_login_0_user_wrongFormat(self,data,access_web):
        # 步骤 输入用户名：XX 密码：XX 点击登录
        access_web[1].login(data["user"],data["passwd"])
        # 断言 登录页面 提示 - 请输入正确手机号
        #登录页面中 - 获取提示框的文本内容
        #比对文本内容 与 期望的值 是否相等。
        assert access_web[1].get_errorMsg_from_loginArea() == data["check"]


    #异常用例 - 账号未注册，密码错误（中间提示）
    # @ddt.data(*LD.phone_data_err)
    @pytest.mark.parametrize("data",LD.phone_data_err)
    def test_login_0_wrongPwd_noReg(self,data,access_web):
        # 步骤 输入用户名：XX 密码：XX 点击登录
        access_web[1].login(data["user"], data["passwd"])
        # 断言 登录页面 页面正中间提示提示 - XXX
        # 登录页面中 - 获取提示框的文本内容
        # 比对文本内容 与 期望的值 是否相等。
        assert access_web[1].get_errorMsg_from_pageCenter() == data["check"]


     # 正常用例 - 登录成功 #fixture的函数名称，用来接收它的返回值
    @pytest.mark.smoke
    def test_login_1_success(self, access_web):
        # 步骤 输入用户名：XX 密码：XX 点击登录
        access_web[1].login(LD.success_data["user"], LD.success_data["passwd"])
        # 断言 首页当中 - 能否找到 退出 这个元素
        assert IndexPage(access_web[0]).isExist_logout_ele()





