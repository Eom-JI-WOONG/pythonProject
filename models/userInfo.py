# -*- coding: UTF-8 -*-
from sqlalchemy import Column,String,Integer,Date,Sequence
from module.database import Base

class UserInfo(Base):  
    __tablename__ = 'userinfo'
    id = Column(String,primary_key=True)
    passwd = Column(String)
    name = Column(String)
    rgi_dt = Column(Date)
    

    
    def __init__(self, id=None, passwd=None, name=None, rgi_dt=None):
        self.id = id
        self.name = name
        self.passwd = passwd
        self.rgi_dt = rgi_dt

    def __repr__(self):
        return '<userinfo %r>' % (self.name)

    def as_dict(self):
        result={}       
        for x in self.__table__.columns:
            if(x.name == 'rgi_dt'):
                value = getattr(self, x.name).strftime('%Y%m%d')
            else:
                value = getattr(self, x.name)
            result[x.name]=value
        return result
