import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from TestDatas import common_datas as CD

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
    driver.refresh()



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