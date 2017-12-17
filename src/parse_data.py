# -*- coding:utf-8 -*-
import sys
import tushare as ts

print(sys.version, ts.__version__)

def parseDate():
    print(ts.get_hist_data('600848'))