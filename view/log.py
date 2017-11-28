#!/usr/bin/env python
#-*- coding:utf-8 -*-
from main import *


# 获取适配log的select选项菜单值
def getOptions():
    try:
        opData = db.query('''select * from log_type where type in ("role","os","cpu","hdd","mem","model","idc","idctag") and status="yes" order by type,value''')
    except Exception,e:
        print "MySQL Error: ",Exception,":",e
        return None
    sd = {'machine':[],'os':[],'cpu':[],'hdd':[],'mem':[],'model':[],'idc':[],'idctag':[]}
    for i in opData:
        sd[i.type].append({"id":i.id,"value":i.value})
    #要解决输出顺序问题
    #print sd
    return sd

# 日志首页，显示日志清单
class Index:
    def GET(self):
        if getLogin():
            SID = getLogin()['SID']
            ShowName = getLogin()['ShowName']
            try:
                getMachine = db.query('''
                     select 
                     ''')
            except:
                return "服务器(数据库)错误"
            return render.log(ShowName=ShowName, uid=SID, getMachine=getMachine, machineShow=getOptions())
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

'''
# 显示日志详情
class Detail:
    def GET(self):

    def POST(self):

#增加日志监控项
class Add:
    @Check_Login
    def GET(self):

    def POST(self):

#编辑日志监控项
class Edit:
    @Check_Login
    def GET(self):

    def POST(self):
'''