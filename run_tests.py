# -*- coding: utf-8 -*-
import sys
import time
import os

from HTMLTestRunner import HTMLTestRunner
#import unittest
from unittest import defaultTestLoader

sys.path.append('./interface')
sys.path.append('./report')
test_dir = './interface'
report_dir = './report'
testsuit = defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ =="__main__":

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp, title='yanss_API', description='mysql, python, request,unittest')
    runner.run(testsuit)
    fp.close()
    os.system("python "+report_dir+"/sendMail.py")

    #unittest.TextTestRunner().run(testsuit)