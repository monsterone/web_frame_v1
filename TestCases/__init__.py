

##
# 1.数据分离 - TestDatas
# 2.测试用例 ddt 引用
# 3.优化了执行效率 setUpClass tearDownClass,每条用例之间互不影响
    # (1)用例执行开始前打开浏览器，输入网址
    #（2）每条用例结束后，刷新浏览器
    #（3）最后执行登录成功用例
# 4.元素定位分离 元素定位类型和表达式用元祖来管理 PageLocators


# 记录：6 月 1日
# TestCase - test_invest.py setUpClass 优化，直接进入页面每次用例刷新，不同每次退出
# 参考登录用例 （web自动化实战（六）下-3，视频）
