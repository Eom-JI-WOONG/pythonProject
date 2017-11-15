# -*- coding: UTF-8 -*-

import json

from models.userInfo import UserInfo
from module.User import User
from module.database import db_session

######################사용자 정보 요청 Controller##########################
class userInfoService:

    def __init__(self):
        print "클래스생성"

    @staticmethod
    def search_User(userId):
        print "메소드호출"
        querys = db_session.query(UserInfo).filter(UserInfo.id == userId)
        entries=[]

        for q in querys:
            entries.append(UserInfo.as_dict(q))

        #return entries
        #querys = UserInfo.query.filter(UserInfo.id == 'skyofblue').first()
        #entries = [dict(seq=q.seq, id=q.id, passwd=q.passwd, name=q.name, rgi_dt=q.rgi_dt.strftime('%Y%m%d')) for q in querys] 

        return json.dumps(entries, ensure_ascii=False, encoding="utf-8")

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
            users[q.id] = User(q.id,q.passwd)
        print users
        return users

