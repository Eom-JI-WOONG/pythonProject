# -*- coding: UTF-8 -*-
import json

from flask import Flask, request, render_template
from flask_login import current_user

from controller.userController import userInfoService as us
from module.Logger import logger

app = Flask(__name__)


@app.before_request
def before_request():
    logger.debug('before_request')

@app.teardown_request
def teardown_request(exception):
    logger.debug('teardown_request')

@app.route('/')
def hello_word():

    return render_template('index.html')

@app.route('/api/login', methods=['GET','POST'])
def login():
    id = request.form['id']
    passwd = request.form['passwd']
    USERS = us.user_Info()

    if id not in USERS:
        res=dict(msg='등록된 사용자가 없습니다', errorcode='9000')
        return json.dumps(res, ensure_ascii=False, encoding="utf-8")
    elif not USERS[id].can_login(passwd):
        res=dict(msg='비밀번호가 틀렸습니다', errorcode='9100')
        return json.dumps(res, ensure_ascii=False, encoding="utf-8")
    else:
        username =USERS[id].get_name().encode('utf-8')
        res=dict(msg='로그인 성공하였습니다', errorcode='0000',name=username)
        return json.dumps(res, ensure_ascii=False, encoding="utf-8")

    
@app.route('/search', methods=['GET','POST'])
def show_Select():
    user = current_user;
    entries = us.show_All()
    return json.dumps(entries, ensure_ascii=False, encoding="utf-8")

@app.route('/api/registUser', methods=['GET', 'POST'])
def user_Regist():
    id = request.form['id']
    passwd = request.form['passwd']
    name = request.form['name']
    USERS = us.user_Info()
    if id in USERS:
        res=dict(msg='이미 등록 된 사용자가 있습니다', errorcode='9200')
    else:
        try:
            us.regist_User(id,passwd,name)
            res=dict(msg='등록처리 완료', errorcode='0000')
        except Exception as e:
            logger.error('오류발생:'+ e)
            res=dict(msg='등록 처리중 알수 없는 오류 발생', errorcode='9300')

    return json.dumps(res, ensure_ascii=False, encoding="utf-8")

@app.route('/regist', methods=['GET', 'POST'])
def regist_Form():
    return render_template('regist.html')

if __name__ == '__main__':
    with open('conf/config.json', 'r') as f:
        config = json.load(f)

    logger.setLevel(config['LOG_LEVEL'])
    app.run(debug=True, host="0.0.0.0")




