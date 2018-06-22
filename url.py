# coding:utf-8
import requests,json
header = {"Content-Type":"application"}
url = "https://master-test.chinacscs.com:1010/v2/oauth/token"

url1 = "https://master-test.chinacscs.com:1010/v2/companies/1114/shareholderHistory"
header = {
          "Authorization":"Basic Y2xpZW50YXBwOjEyMzQ1Ng==",
          "Content-Type":"application/x-www-form-urlencoded"
          }
params = {
        "kaptcha":"bf2n",
        "grant_type":"password",
        "client_id":"clientapp",
        "username":"dc",
        "password":"Wanda123*",
}
param = json.dumps(params)
res = requests.post(url,params=param,headers=header)
# res1 = requests.get(url1)
# print res1.text
print res.text



