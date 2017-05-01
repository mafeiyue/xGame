#coding=utf-8
'''
Created on 2016年1月11日

@author: xxw
'''
import struct
from common import fprotocol,const

#登录
def c2lg_login(client,pkt):
    user_name = u"xGame_test"
    user_pwd = u"xGame_pwd"

__cmdTable = {
                const.C2LG_Login:c2lg_login,
             }

def parse(clinet, cmd, pkt):
    func = __cmdTable.get(cmd)
    if not func:
        raise fprotocol.FPError(u"unknow cmd=%d" % cmd)
    func(clinet, pkt)

if __name__ == '__main__':
    pass
