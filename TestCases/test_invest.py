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
from PageObjects.user_page import UserPage

from TestDatas import common_datas as CD
from TestDatas import login_datas as LD
from TestDatas import invest_datas as IDs
import ddt

@ddt.ddt
class TestInvest(unittest.TestCase):

    def setUp(self):
        # 前置 访问登录页面,成功登录
        self.driver = webdriver.Chrome()
        self.driver.get(CD.web_login_url)
        self.driver.maximize_window()
        #登录页面，登录
        self.lg = LoginPage(self.driver)
        self.lg.login(LD.success_data["user"], LD.success_data["passwd"])


    def tearDown(self):
        self.driver.quit()

    #进入投标页面函数
    def into_inverst(self):
        ## 首页面
        self.ig = IndexPage(self.driver)
        # 点击抢投标，进入投标页面
        self.ig.click_bid_by_random()
        ## 投标页面
        self.bg = BidPage(self.driver)


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

        # 调用进入投标页面函数
        self.into_inverst()
        #获取输入框资前的用户余额
        befor_amount = self.bg.get_uer_money()

        #正常投资
        self.bg.invest(IDs.inverst_success["money"])
        #点击投资成功的弹出框-查看并激活
        self.bg.click_activeButton_on_success_popup()

        ## 用户页面
        self.ug = UserPage(self.driver)
        # 获取投资后的金额
        after_amount = self.ug.get_avabile_mount()
        #断言：
        self.assertEqual(befor_amount-after_amount,IDs.inverst_success["check"])





    # 异常用例 - 弹框提示
    @ddt.data(*IDs.inverst_fail_alert)
    def test_invest_failed_nol00(self,data):

        #调用进入投标页面函数
        self.into_inverst()
        # 投资,投标金额不是 100的整数倍 ---按钮可点击
        self.bg.invest(data["money"])
        #获取断言提示
        self.assertEqual(self.bg.get_errorMsg_from_pageCenter(),data["check"])


    # 异常用例 - 按钮提示
    @ddt.data(*IDs.inverst_fail_button)
    def test_invest_failed_noButton(self,data):
        # 调用进入投标页面函数
        self.into_inverst()
        # 投资,投标金额不是 10的整数倍---按钮可不点击
        self.bg.invest_no_click(data["money"])
        # 获取断言提示
        self.assertEqual(self.bg.get_errorMsg_from_investButton(), data["check"])







