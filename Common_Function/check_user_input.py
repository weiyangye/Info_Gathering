#!/usr/bin/env python
# *.* coding=utf-8 *.*
'''
一般功能模块，用于存储系统的
'''

'''
regex = re.compile(
r'^((?:http|ftp)s?://)?'  # http:// or https://
r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
r'localhost|'  # localhost...
r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
r'(?::\d+)?'  # optional port
r'(?:/?|[/?]\S+)$', re.IGNORECASE)
'''

import re
import os,sys,argparse



class check_user_input():
    def __init__(self):
        pass
    def check_ip(self,ip):
        print "checking ip operation\n"
        pattern = r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
        if re.match(pattern, ip):
            return True
        else:
            return False



    def check_url(self,url):
        print "checking url operation\n"
        regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if regex.match(url):
            return  True
        else:
            return False


