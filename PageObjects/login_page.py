
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from PageLocators.loginpage_locators import LoginPageLocator as loc
#引入页面元素定位页面，页可以继承该类，但元素多了不好区分，长远考虑用loc快速找到定位元素
from Common.basepage import BasePage
class LoginPage(BasePage):


    #登录操作
    def login(self,username,passwd):
        #输入用户名
        #输入密码
        #点击登录
        doc = "登录页面_登录功能"
        self.wait_eleVisible(loc.name_text,doc=doc)
        self.input_text(loc.name_text,username,doc)
        self.input_text(loc.pwd_text,passwd,doc)
        #判断rember_user 的值，来决定，是否勾选
        self.click_element(loc.login_but,doc)
        # self.driver.find_element(*loc.login_but).click()



    #获取错误提示信息 - 登录区域
    def get_errorMsg_from_loginArea(self):
        doc = "登录页面_获取错误提示信息(登录区域)"
        self.wait_eleVisible(loc.errorMsg_from_loginArea, doc=doc)
        return self.get_text(loc.errorMsg_from_loginArea,doc)

    # 获取错误提示信息 - 登录页面正中间
    def get_errorMsg_from_pageCenter(self):
        doc = "登录页面_获取错误提示信息(登录页面正中间)"
        self.wait_eleVisible(loc.errorMsg_from_pageCenter, doc=doc)
        return self.get_text(loc.errorMsg_from_pageCenter, doc)




    #注册入口
    def register_enter(self):
        pass

    #忘记密码

