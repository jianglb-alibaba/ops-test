#!/usr/bin/env python
#-*- coding:utf-8 -*-
from main import *

# 监控中心

# Redis
class M_Redis:
    def GET(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            #print sData            
            #print "ShowName: " + ShowName
            return render.monitor_redis(ShowName=ShowName,uid=SID)
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")
# MySQL
class M_MySQL:
    def GET(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            #print sData            
            #print "ShowName: " + ShowName
            return render.monitor_mysql(ShowName=ShowName,uid=SID)
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")

# 网络流量
class M_Traffic:
    def GET(self):
        if getLogin():
            sData = getLogin()
            SID = sData['SID']
            ShowName = sData['ShowName']
            #print sData            
            #print "ShowName: " + ShowName
            return render.monitor_bandwidth(ShowName=ShowName,uid=SID)
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")




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
            return render.container(ShowName=ShowName, uid=SID, getMachine=getMachine, machineShow=getOptions())
        else:
            web.setcookie('HTTP_REFERER', web.ctx.fullpath, 86400)
            return web.seeother("/login")