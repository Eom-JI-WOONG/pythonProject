# -*- coding: UTF-8 -*-

import json,datetime

from models.userInfo import UserInfo
from module.User import User
from module.database import db_session

######################사용자 정보 요청 Controller##########################
class userInfoService:
    def __init__(self):
        print "클래스생성"

    @staticmethod
    def search_User(userId):
        querys = db_session.query(UserInfo).filter(UserInfo.id == userId)
        entries=[]

        for q in querys:
            entries.append(UserInfo.as_dict(q))
        #return entries
        #querys = UserInfo.query.filter(UserInfo.id == 'skyofblue').first()
        #entries = [dict(seq=q.seq, id=q.id, passwd=q.passwd, name=q.name, rgi_dt=q.rgi_dt.strftime('%Y%m%d')) for q in querys] 

        return entries

    @staticmethod
    def show_All():
        querys = db_session.query(UserInfo)
        entries=[]

        for q in querys:
            entries.append(UserInfo.as_dict(q))
        return entries

    @staticmethod
    def user_Info():
        querys = db_session.query(UserInfo)
        users={}
        for q in querys:
            users[q.id] = User(q.id,q.passwd,q.name)
        return users

    @staticmethod
    def regist_User(userId,passwd,name):
        print "Regist user method start!"
        user = UserInfo(userId,passwd,name,datetime.datetime.now())
        try:
            db_session.add(user)
            db_session.commit()
            print db_session.query(UserInfo).count()
        except Exception as e:
            print e.message
            db_session.rollback()
            raise e
        finally:
            db_session.close()
