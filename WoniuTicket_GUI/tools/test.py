# import logging
# logger = logging.getLogger(__name__)
# logger.setLevel(level = logging.INFO)
# handler = logging.FileHandler("log.txt")
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
# handler.setFormatter(formatter)
#
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
#
# logger.addHandler(handler)
# logger.addHandler(console)
#
# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")

# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.implicitly_wait(10)
# a = None
# b = 1
# if not None:
#     print(1)
# else:
#     print(2)
import requests

url1 = 'http://192.172.4.60:9000/adminservice/login.do'
data = {"username":"admin","password":"123456","captcha":"123"}
session = requests.session()
resp = session.post(url1 , data)
print(resp.text)
print(resp.status_code)


url2 = 'http://192.172.4.60:9000/adminservice/admins.do'
data2 = {"username":"5" , "realname":"2" , "telephone":"2" , "email":"zz@qq.com" , "password":"1" , "status":"0"}
resp2 = session.post(url2 , data2)
print(resp2.text)

url3 = 'http://192.172.4.60:9000/adminservice/admins/delete/7'
resp3 = session.delete(url3)
print(resp3.text)

url4 = 'http://192.172.4.60:9000/adminservice/admins?page=1&limit=20'
resp4 = session.get(url4)
print(resp4.text)


