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
    print '로그인을 먼저 해주세요'
    return render_template('index.html')

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
        res=dict(msg='로그인 성공하였습니다', errorcode='0000')
        return json.dumps(res, ensure_ascii=False, encoding="utf-8")

    
@app.route('/search', methods=['GET','POST'])
@login_required
def show_Select():
    user = current_user;
    if current_user.is_authenticated():
        print "로그인을 하셨군요"
    else:
        print "로그인을 안했네요"
    entries = us.show_All()
    print entries
    return render_template('listForm.html', entries=entries);

@app.route('/regist', methods=['GET', 'POST'])
@login_required
def user_Regist():
    return "등록페이지 입니다"

if __name__ == '__main__':
    app.run(debug=True)
