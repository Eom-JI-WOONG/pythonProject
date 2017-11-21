# -*- coding: UTF-8 -*-
import  logging
import  logging.handlers
import re

#로거 인스턴스 생성
logger = logging.getLogger('systemLogger')


#로깅 레벨 셋팅
#logger.setLevel(logging.DEBUG)

#로그 포메터를 만든다
fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

#파일과 스트림 모두 출력 하도록 핸들러 생성
fileName = '../log/systemlog.log'
fileHandler = logging.handlers.TimedRotatingFileHandler(fileName, when="midnight", interval=1, encoding='utf-8')
streamHandler = logging.StreamHandler()

#formmater seting
fileHandler.setFormatter(fomatter)
streamHandler.setFormatter(fomatter)

#로거 인스턴스에 스트림 핸들러와 파일핸들러 추가
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)






