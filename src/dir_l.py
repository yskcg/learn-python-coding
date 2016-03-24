# -*- coding: utf-8 -*-
from datetime import datetime
import  os

pwd = os.path.abspath('.')

def dir_l(path):
    for i in os.listdir(path):
        fsize = os.path.getsize(i)
        mtime = datetime.fromtimestamp(os.path.getmtime(i)).strftime("%Y-%m-%d %H:%M")
        flag = '/' if os.path.isdir(i) else ''
        print('%10d  %s  %s%s' % (fsize, mtime, i, flag))

dir_l(pwd)