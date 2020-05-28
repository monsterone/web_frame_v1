
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.loginpage_locators import LoginPageLocator as loc
#引入页面元素定位页面，页可以继承该类，但元素多了不好区分，长远考虑用loc快速找到定位元素

class LoginPage:


    def __init__(self,driver):
        self.driver = driver


    #登录操作
    def login(self,username,passwd):
        #输入用户名
        #输入密码
        #点击登录
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.name_text))
        self.driver.find_element(*loc.name_text).send_keys(username)
        self.driver.find_element(*loc.pwd_text).send_keys(passwd)
        #判断rember_user 的值，来决定，是否勾选
        self.driver.find_element(*loc.login_but).click()



    #获取错误提示信息 - 登录区域
    def get_errorMsg_from_loginArea(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.errorMsg_from_loginArea))
        return self.driver.find_element(*loc.errorMsg_from_loginArea).text

    # 获取错误提示信息 - 登录页面正中间
    def get_errorMsg_from_pageCenter(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(loc.errorMsg_from_pageCenter))
        return self.driver.find_element(*loc.errorMsg_from_pageCenter).text




    #注册入口
    def register_enter(self):
        pass

    #忘记密码

