# -*- coding: utf-8 -*-
# @Author : Monster
# @File : bidpage_locators.py


from selenium.webdriver.common.by import By

# 投标页面元素定位
class BidPageLocator:

    # 元素定位
    # 投标金额输入框
    invest_input = (By.XPATH,'//div[@class="clearfix left"]/input[contains(@placeholder,"可用余额")]')

    # 投标按钮
    do_invest_button = (By.XPATH,'//button[text() = "投标"]')

    # 查看并激活按钮(投标成功)
    click_activeButton = (By.XPATH,'//div[text()="投标成功！"]//following-sibling::div[@class="capital_btn"]//button[text()="查看并激活"]')

    # 中间错误弹框提示信息
    center_err_msg = (By.XPATH,'//div[@class="text-center"]')

    # 中间错误弹框提示信息,确认
    center_err_msg_button = (By.XPATH,'//a[@class="layui-layer-btn0"]')

    # 错误提示信息投标按钮
    err_invest_msg_button = (By.XPATH,'//button[@class="btn btn-special height_style"]')