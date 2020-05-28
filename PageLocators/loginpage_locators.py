

from selenium.webdriver.common.by import By

# 登录页面元素定位
class LoginPageLocator:
    # 元素定位
    # 用户名输入框
    name_text = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    pwd_text = (By.XPATH, '//input[@name="password"]')
    # 登录按钮
    login_but = (By.XPATH, '//button[text()="登录"]')
    # 错误提示框 - 登录区域
    errorMsg_from_loginArea = (By.XPATH, '//div[@class="form-error-info"]')
    # 错误提示框 - 登录页面正中间
    errorMsg_from_pageCenter = (By.XPATH, '//div[@class="layui-layer-content"]')
