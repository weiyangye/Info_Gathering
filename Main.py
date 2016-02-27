#!/usr/bin/env python
# *.* coding=utf-8 *.*
# author: 夜未央
# email: weiyangye@hotmail.com
'''
主函数：负责对整体系统的调用和展示
common 目录负责一般功能代码实现的存储
plugins 目录存储功能插件
'''

import os,sys
import re, argparse
import sqlite3
import logging
import Common_Function.check_user_input as cm



class StartFunction(object):
    '''
    开始进行相应的处理过程
    '''
    def __init__(self):
        self.info_dic = {'domain': {},'ipaddress': {}, 'dns': {}, 'mx': {}, 'soa': {}}

    def start_URL_check(self):
        pass

    def start_IP_check(self):
        pass


if __name__ == "__main__":
    print "main function"
    print "Please input URL or IP Address: "

    if len(sys.argv) == 2:
        print "校验输入ing.........\n"
        ip_flag = cm.check_user_input().check_ip(sys.argv[1])
        if ip_flag is True:
            print "IP 地址合法，将进入下一步流程...\n"
        else:
            print "IP 地址不合法，校验是否为域名....\n"
            url_flag = cm.check_user_input().check_url(sys.argv[1])
            if url_flag is True:
                print "URL 合法，将进行接下来的分析....\n"
            else:
                print "URL 不合法，请重新输入....\n"
    else:
        print ("usage: %s ip_address or url_address" % sys.argv[0])
        sys.exit(-1)
