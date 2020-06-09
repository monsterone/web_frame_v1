import pytest
from selenium import webdriver

from PageObjects.bid_page import BidPage
from PageObjects.index_page import IndexPage
from PageObjects.login_page import LoginPage
from TestDatas import common_datas as CD
from Common.logger import Logger
import time

import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
##contftest 执行过程
#1.conftest.py
#2.定义fixture @pytest.fixture
#3.yeid分离前置和后置，返回值
#4.可以定义多个fixture
# 测试类、测试用例。@pytest.mark.usefixtures("fixture函数名称")
## 记录：
# pytest的执行顺序---与用例在页面的先后位置有关
# conftest 可以在子模块中创建，如果子模块中conftest与外面的conftest函数名重复
# 则优先使用子模块的，相当如函数的从写
# pytest 失败重运行机制，失败之后马上重运行。robootframekr,等全部用例运行完后再重运行失败用例
# -s 打印日志
##pytest报告 #xml、log格式是pytest自带的，html格式需要插件pytest-html（使用相对路径，不支持绝对路径），
#python_hm\web_frame_v1>pytest -m demo --reruns 2 --reruns-delay 5 -s --junitxml=Outputs/re
# ports/report.xml --html=Outputs/reports/html_report.html

#pytest -m invest --reruns 2 --reruns-delay 5 -s --junitxml=Outputs/
# reports/report_invest.xml --html=Outputs/reports/html_report_invest.html

#allure-report
#pytest -m invest --reruns 2 --reruns-delay 5 -s --junitxml=Outputs/
# reports/report_invest.xml --html=Outputs/reports/html_report_invest.html
## --alluredir=Outputs/allure_reports


logger = Logger(__name__).getlog()
driver = None
#声明它是一个fixture
@pytest.fixture(scope="class")
def access_web():
    global driver
    #前置操作
    print("=====测试用例执行之前，setUpClass，整个测试类只执行一次")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield (driver,lg)  #分割线； #后面接返回值
    #后置操作
    print("=====测试用例执行之后，tearDownClass，整个测试类只执行一次")
    driver.quit()

@pytest.fixture()
def refresh_page():
    global driver
    #前置操作
    yield
    #后置操作
    logger.info("======每一个用例后置：刷新当前页面======")
    driver.refresh()
    time.sleep(0.5)

# =====test_invest======
@pytest.fixture(scope="class")
def access_invest():
    global driver
    # 初始化浏览器会话
    logger.info("======用例类前置：初始化浏览器会话，登录XXX系统======")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    LoginPage(driver).login(CD.user, CD.passwd)
    # 首页-选一个标来投资，直接选第一个标/随机选一个标
    IndexPage(driver).click_bid_by_random()
    ## 投标页面
    bid_page = BidPage(driver)
    yield (driver,bid_page)
    logger.info("======用例类后置：关闭浏览器会话，清理环境======")
    driver.quit()









# ==========test_demo=======
@pytest.fixture("session")
def session_demo():
    print("=====测试前---session_demo====")
    yield
    print("=====测试后---session_demo====")


@pytest.fixture("class")
def class_demo():
    print("=====测试前---class_demo====")
    yield
    print("=====测试后---class_demo====")

@pytest.fixture("function")
def function_demo():
    print("=====测试前---function_demo====")
    yield
    print("=====测试后---function_demo====")