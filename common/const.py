# coding=utf-8

# =======客户端类型
CLIENT_TYPE_USER = 0
CLIENT_TYPE_LOGINGATE = 1
CLIENT_TYPE_LOGINSERVER = 2
CLIENT_TYPE_GAMECENTER = 3
CLIENT_TYPE_3CARD = 4

# =======ErrorCode
ERROR_OK = 0
ERROR_SERVER = 1
ERROR_SERVER_FULL = 2
ERROR_NO_LOGINGATE = 4
ERROR_NOT_READY_LOGIN = 5
ERROR_ACCOUNT_NOT_EXISTS = 6
ERROR_ACCOUNT_PWD_ERROR = 7
ERROR_ACCOUNT_TOKEN_INVALID = 8
ERROR_GAMECENTER_NOT_ONLINE = 9
ERROR_USER_NOT_EXISTS = 10
ERROR_USER_NOT_IN_GC = 11
ERROR_USER_IS_GAMING = 12

# =======心跳包
KEEPLIVE = 1

# =======各种服务器--->到管理服务器消息ID:[101-200]
S2SM_REQUEST_START = 101

# =======管理服务器--->各种服务器消息ID:[201-300]
SM2S_START_REPLY = 201

# 客戶端--->管理服务器消息ID:[501-600]
C2SM_GET_LOGINGATE = 501  # 请求获得登录网关信息
C2SM_GET_GAMECENTER = 502  # 请求获得游戏中心服务器信息

# 管理服务器--->客戶端消息ID:[601-700]
SM2C_GET_LOGINGATE_REPLY = 601  # 请求获得登录网关信息返回
SM2C_GET_GAMECENTER_REPLY = 602  # 请求获得游戏中心服务器信息返回

# 客户端--->登录网关消息ID:[701-800]
C2LG_REQUEST_LOGIN = 701  # 客户端请求登录

# 登录网关--->客户端消息ID:[801-900]
LG2C_READY_LOGIN = 801  # 当客户端连接登录网关之后返回是否可以请求登录
LG2C_REPLY_LOGIN = 802  # 客户端登录返回

# 登录服务器--->登录网关消息ID:[901-1000]
L2LG_LOGIN_RESULT = 901  # 登录结果
L2LG_TRANSFORM_CLIENT = 902  # 转发到客户端

# 诈金花服务器--->游戏中心服务器消息ID:[1001-2000]
TCS2GC_REGISTER = 1001  # 向游戏中心注册游戏
TCS2GC_CHECK_USER = 1002  # 向游戏中心验证玩家
TCS2GC_UPDATE_USER_GAMESTATE = 1003  # 更新游戏中心玩家状态

# 游戏中心--->炸金花游戏消息ID:[2001-3000]
GC2TCS_CHECK_USER_RESULT = 2001  # 游戏中心验证玩家返回

# 客户端--->游戏中心消息ID:[3001-4000]
C2GC_REQUEST_ENTER_GC = 3001  # 玩家进入游戏中心

# 游戏中心--->客户端消息ID:[4001-5000]
GC2C_REPLY_ENTER_GC = 4001  # 玩家进入游戏中心返回

# 客户端--->炸金花服务器消息:[5001-6000]
C2TCS_REQUEST_ENTERGAME = 5001  # 客户端请求进入炸金花服务器
# 炸金花服务器--->客户端消息:[6001-7000]
TCS2C_REPLY_ENTERGAME = 6001  # 进入炸金花游戏返回
