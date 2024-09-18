# coding:UTF-8

import os
import sys
import re

# 打开文件
path = "/Users/js/Desktop/wujiaxing"
dirs = os.listdir(path)

def remove_mark():
	old_names = os.listdir()
	for old_name in old_names:
		try:
			result = re.match(r'(^\[.*\])(.*)',old_name).group(2)
			rm = old_name