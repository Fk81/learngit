#111
#直储商品下单
import http.client
import urllib
import re
import time
import random


fmt = '%Y-%m-%d %H:%M:%S'  # 定义时间显示格式
Date = time.strftime(fmt, time.localtime(time.time()))  # 把传入的元组按照格式，输出字符串

ele = {"method": "customer.order.purchase.add",
       "v": "1.0",
       "timestamp": Date,
       "customerid": "A1800015",
       "sign": "参数签名",
       "CustomerOrderId": "ZHSPV239171101142600002_1",
       "ProductId": "ED9100028",
       "TopupAccount": "cjj363700424",
       "TopupCount": 1,
       "TopupContent": {"OutSaleTotal": "",
                        "OutSaleIp": "116.205.13.50",
                        "ChargeGame": "*",
                        "ChargeRegion": "*",
                        "ChargeService": "*",
                        "ChargeType": "*",
                        "ChargePassword": "",
                        "CallBackUrl": ""}}

header={"Content-Type":"application/x-www-form-urlencoded"}
posts = urllib.parse.urlencode(ele)
conn = http.client.HTTPConnection("121.40.209.239:14005")
conn.request(method="POST",url="/Interface/Action",body=posts,headers=header)
response = conn.getresponse()
data = response.read().decode("utf-8")
print(data)

#获取下单订单号
orderId = re.findall(r"Data\"\:\"([^\"]+)\"",data)
print(orderId)
