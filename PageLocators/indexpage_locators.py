# -*- coding: utf-8 -*-
# @Author : Monster
# @File : indexpage_locators.py


from selenium.webdriver.common.by import By

# 首页页面元素定位
class IndexPageLocator:

    # 元素定位
    #抢投标按钮
    invest_button = (By.XPATH,'//a[text()="抢投标"]')
    # invest_button = (By.CLASS_NAME,'btn btn-special')
