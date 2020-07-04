#coding=utf-8
#!usr/bin/python
import unittest
import time,os,sys
from public import base,HTMLTestRunnerCN
from oper import send_mail
import filePath
from oper import read_Config
path = filePath.get_Path()

#在测试报告目录下找到最新的报告文件,打印且返回最新报告的名称
def report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"/"+fn))
    filename = os.path.join(testreport,lists[-1])
    print("报告已生成：%s" % filename)
    return filename
def fp():
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    # filename = './report/' + now + '_result.html'
    report_name = now + '_result.html'
    print(report_name)
    filename = os.path.join(path,'report',report_name)
    print(filename)
    return filename

if __name__ =="__main__":
    #构建测试集
    test_dir = os.path.join(path,"testcase")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    fp = open(fp(),"wb")
    mail_config = read_Config.ReadConfig()
    title = mail_config.get_config('EMAIL','title')
    description = mail_config.get_config('EMAIL','description')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title=title,description=description,verbosity=2)
    runner.run(discover)
    fp.close()
    test_report = os.path.join(path,"report")
    rep = report(test_report)
    #发送邮件
    send_mail.send_mail(rep)