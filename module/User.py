# -*- coding: UTF-8 -*-

class User:
    def __init__(self,user_id,passwd=None,user_name=None,authenticated=False):
        self.user_id = user_id
        self.passwd = passwd
        self.user_name = user_name
        self.authenticated = authenticated

    def __repr__(self):
        s = {
            'id' : self.user_id,
            'passwd' : self.passwd,
            'name' : self.user_name,
            'authenticated' : self.authenticated
        }
        return str(s)

    def can_login(self, passwd):
         return self.passwd == passwd

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def get_id(self):
        return self.user_id

    def get_name(self):
        return self.user_name

    def is_anonymous(self):
        return False

