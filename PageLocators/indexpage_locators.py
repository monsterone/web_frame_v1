# -*- coding: utf-8 -*-
# @Author : Monster
# @File : indexpage_locators.py


from selenium.webdriver.common.by import By

# 首页页面元素定位
class IndexPageLocator:

    # 元素定位
    #登录成功断言（退出）
    index_logout = (By.XPATH,'//a[@href="/Index/logout.html"]')

    #抢投标按钮
    invest_button = (By.XPATH,'//a[text()="抢投标"]')
    # invest_button = (By.CLASS_NAME,'btn btn-special')
