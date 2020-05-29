# -*- coding: utf-8 -*-
# @Author : Monster
# @File : test_invest.py

#独立的测试账号


#正常用例
#前提条件：
####################（尽量不要依赖测试环境的数据，如果没有，就自己造环境）#########
#1、用户已登陆
#2、有能够投资的标#如果没有标，则先加标。#接口的方式加标。
#3、用户有余额可以投资
    #1、1个亿
    #2、接口方式：查询当前用户还有多少钱。>6000不用充值。如果小于用例中投资的金额，那就充值。


#步骤
#1、在首页选标—不根据标名，根据抢投标。默认第一个标。
###标页面-获取一下投资前的用户余额
#2、标页面-输入投资金额、点击投资按钮
#3、标页面-点击投资成功的弹出框-查看并激活，进入个人页面

#断言
#钱投资后的金额，是不是少了投资的量。
#个人页面-获取投资后的金额
# 投资前的金额一投资后的金额=投资金额

#投资记录对不对


# -------------------


#异常用例：非常好创造环境，非常好写的。

#不考虑自动化实现
#异常用例：全投操作？标的可投金额〉个人余额    （异常复杂可以不要自动化，手工验证就好）
            #投资金额〉标的可投金额#满足这种条件标、用户



import unittest
from selenium import webdriver
from PageObjects.index_page import IndexPage
from PageObjects.bid_page import BidPage
from PageObjects.login_page import LoginPage

from TestDatas import common_datas as CD
from TestDatas import login_datas as LD

class TestInvest(unittest.TestCase):

    def setUp(self):
        # 前置 访问登录页面,成功登录
        self.driver = webdriver.Chrome()
        self.driver.get(CD.web_login_url)
        #登录页面，登录
        self.lg = LoginPage(self.driver)
        self.lg.login(LD.success_data["user"], LD.success_data["passwd"])


    def tearDown(self):
        self.driver.quit()

    # 正常用例 - 投标成功
    def test_invest_success(self):
        # 步骤
        # 1、在首页选标—不根据标名，根据抢投标。默认第一个标。
        ###标页面-获取一下投资前的用户余额
        # 2、标页面-输入投资金额、点击投资按钮
        # 3、标页面-点击投资成功的弹出框-查看并激活，进入个人页面

        # 断言
        # 钱投资后的金额，是不是少了投资的量。
        # 个人页面-获取投资后的金额
        # 投资前的金额一投资后的金额=投资金额

        # 首页
        ig = IndexPage(self.driver)
        ig.click_bid_by_random()



        pass

    #异常用例 -
    def test_invest_failed_nol00(self):


        pass

    # 异常用例 -
    def test_invest_failed_nol0(self):
        pass







