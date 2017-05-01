#coding=utf-8
'''
Created on 2016年1月11日

@author: xxw
'''

import logging
import time
from twisted.internet import protocol
from common import fprotocol
import clientfactory
import clientparse
import loginservermanager
import loginserver

CLIENT_STATE_INIT               = 0
CLIENT_STATE_AUTH               = 1
CLIENT_STATE_LOGINED            = 2
CLIENT_STATE_TO_CLOSE           = 3


class Client(fprotocol.FProtocol):
    def __init__(self, pid, addr):
        fprotocol.FProtocol.__init__(self)
        self.__id = pid
        self.__addr = addr
        self.__ip = addr.host.decode('utf-8')
        self.toclosetime = time.time()
        self.state = CLIENT_STATE_INIT
        self.loginserver = None

    def getId(self):
        return self.__id
    
    def getIp(self):
        return self.__ip

    def getState(self):
        return self.state
    
    def isLogined(self):
        return self.state==CLIENT_STATE_LOGINED
        
    def packetReceived(self, cmd, pkt):
        if self.state == CLIENT_STATE_TO_CLOSE:
            return
        try:
            clientparse.parse(self, cmd, pkt)
        except Exception:
            logging.exception(u"clientparse.parse() cmd=%d" % cmd)
            self.abort()

    def connectionMade(self):
        logging.debug(u"Client.connectionMade() ip=%s", self.__ip)
        #分配一个空闲的loginserver
        freeloginserver = loginservermanager.instance.GetFreeLoginServerID()
        if freeloginserver:
            id = int(freeloginserver[u"id"])
            ip = freeloginserver[u"ip"]
            port = int(freeloginserver[u"port"])
            logging.warn(u"分配用户空闲登录服务器成功 client_id:%d loginserver_id:%s loginserver_ip:%s loginserver_port:%s",self.getId(),id,ip,port)
            #分配成功之后，建立连接
            loginsvr_client = loginservermanager.instance.GetLoginServer(id)
            if not loginsvr_client:
                loginserver.LoginServer().start(id,ip,port,self.ConnectLoginSvrCB)
        else:
            self.goToClose()
            logging.warn(u"分配用户空闲登录服务器失败 client_id:%d",self.getId())
   
    def connectionLost(self, reason=protocol.connectionDone):
        logging.debug(u"Client.connectionLost %s", reason) 
        clientfactory.instance.removeProtocol(self)
    
    def goToClose(self):
        self.state = CLIENT_STATE_TO_CLOSE
        self.toclosetime = time.time()
        
    def kick(self):
        logging.debug(u"Client.kick()")
        self.goToClose()

    def ConnectLoginSvrCB(self,connected,loginserver):
        if connected:
            loginservermanager.instance.AddLoginServer(loginserver.id,loginserver)
            logging.warn(u"连接用户所在登录服务器成功 client_id:%d loginserver_id:%d",self.getId(),id)
            self.loginserver = loginserver
        else:
            loginservermanager.instance.AddLoginServer(loginserver.id)
            self.goToClose()
