# -*- coding: utf-8 -*-
"""
Created on Thu May 18 21:41:32 2017

@author: 55
"""

#!/usr/bin/env python3
# coding: utf-8

from wxpy import *

# 扫码登陆
bot = Bot()

# 初始化图灵机器人 (API key 申请:http://www.tuling123.com/)
tuling = Tuling(api_key='a59706eb47d543df9a64e71')


# 自动回复所有文字消息
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)


# 开始运行
bot.join()
