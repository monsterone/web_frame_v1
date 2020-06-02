
import unittest
import HTMLTestReportCN
#实例化套件对象
from Common.dir_config import testcase_dir, htmlreport_dir

s = unittest.TestSuite()
#TestLoader的用法
#1、实例化TestLoader对象
#2、使用discover去找到一个目录下的所有测试用例
#3、使用S

loader = unittest.TestLoader()
s.addTests(loader.discover(testcase_dir))
## 运行
runner = unittest.TextTestRunner()
s.run(s)

fp = open(htmlreport_dir + '/autoTest_report.html')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         title="测试报告",
                                         description="cs报告",
                                         tester="monster")
runner.run(s)