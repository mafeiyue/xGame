#coding=utf-8
class Config(object):
    def __init__(self):
        self.server_ip = u""
        self.server_port = 1111
        self.max_client = 10000
        self.server_pid = u"/tmp/servermanager.pid"

        self.log_file = u"servermanager.log"
        self.log_format = u"%(asctime)s %(levelname)s %(message)s"
        self.log_level = u"DEBUG"

        self.redis_ip = u"192.168.195.128"
        self.redis_port = 6379
        self.redis_db = 0
        self.redis_pwd = u""
        self.redis_linkcount=1

        #最大登录网关数量
        self.max_logingate = 88
        #最大登录服务器数量
        self.max_loginserver = 200
        #扎金花游戏服务器最大数量
        self.max_3cardserver = 100



instance = Config()
