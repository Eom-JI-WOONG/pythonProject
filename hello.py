# -*- coding: UTF-8 -*-
import os
import json
from flask import Flask, request, render_template, redirect, url_for,jsonify
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required

from controller.userController import userInfoService as us


app = Flask(__name__)
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)

#############LOGIN 사용자정보를 가져온다##########################
USERS = us.user_Info()

###########################################################
@login_manager.user_loader
def user_loader(id):
    return USERS[id]

@login_manager.unauthorized_handler
def unauthorized():
    res=dict(msg='로그인을 먼저 해주세요', errorcode='9500')
    return json.dumps(res, ensure_ascii=False, encoding="utf-8")

@app.before_request
def before_request():
    print 'before_request'

@app.teardown_request
def teardown_request(exception):
    print 'teardown_request'

@app.route('/')
def hello_word():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    print type(request.form['id'])
    id = request.form['id']
    passwd = request.form['passwd']

    if id not in USERS:
        res=dict(msg='등록된 사용자가 없습니다', errorcode='9000')
        return json.dumps(res, ensure_ascii=False, encoding="utf-8")
    elif not USERS[id].can_login(passwd):
        res=dict(msg='비밀번호가 틀렸습니다', errorcode='9100')
        return json.dumps(res, ensure_ascii=False, encoding="utf-8")
    else:
        USERS[id].authenticated = True
        login_user(USERS[id], remember=True)

        print USERS[id].get_name()
        username =USERS[id].get_name().encode('utf-8')
        print type(username)
        res=dict(msg='로그인 성공하였습니다', errorcode='0000',name=username)
        print res
        return json.dumps(res, ensure_ascii=False, encoding="utf-8")

    
@app.route('/search', methods=['GET','POST'])
@login_required
def show_Select():
    user = current_user;
    entries = us.show_All()
    return json.dumps(entries, ensure_ascii=False, encoding="utf-8")

@app.route('/registUser', methods=['GET', 'POST'])
@login_required
def user_Regist():
    id = request.form['id']
    passwd = request.form['passwd']
    name = request.form['name']

    if id in USERS:
        res=dict(msg='이미 등록 된 사용자가 있습니다', errorcode='9200')
    else:
        try:
            us.regist_User(id,passwd,name)
            res=dict(msg='등록처리 완료', errorcode='0000')
        except Exception as e:
            print e
            res=dict(msg='등록 처리중 알수 없는 오류 발생', errorcode='9300')

    return json.dumps(res, ensure_ascii=False, encoding="utf-8")

@app.route('/regist', methods=['GET', 'POST'])
@login_required
def regist_Form():
    return render_template('regist.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")



