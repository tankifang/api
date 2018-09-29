# -*- coding: utf-8 -*-

import unittest
import requests
import os, sys
#from db_fixture import test_data

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

token = "20180000000000TEST-MEMBER-TEST"
base_url = "https://m.yanss.cn/api/v1/order/"

class order(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_list_user(self):
        payload = "{\n\t\"token\":\""+token+"\",\n\t\"orderStatus\":1," \
                  "\n\t\"currentPage\":1,\n\t\"pageSize\":15\n\t\n}"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url+"list/user", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')

    def test_dispath(self):
        payload = "{\"lat\":30.48668,\"lng\":114.39316,\"orderBrands\":[{\"brandId\":\"C430000B001\"," \
                  "\"brandImg\":\"https://image.yanss.cn/brand/c430000b001/logo.png\"," \
                  "\"brandName\":\"摇滚米粒\",\"isUseRice\":0,\"orderProducts\":[{\"boxPrice\":0.5," \
                  "\"count\":3,\"pid\":\"C430000B001P001\",\"price\":8.8,\"productName\":\"米单纯\"," \
                  "\"brandId\":\"C430000B001\",\"brandName\":\"摇滚米粒\"," \
                  "\"brandImg\":\"https://image.yanss.cn/brand/c430000b001/logo.png\",\"weight\":100," \
                  "\"lunchState\":0,\"showStatus\":0}],\"brandCoupon\":0}]}"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url+"dispatch", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')

    def test_dispatch_create(self):
        payload = "{\"token\":\""+token+"\",\"storeProducts\":[{\"storeId\":7," \
                  "\"pic\":\"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1522161727511&di=22b9e21b7efb8a2a3cfcd528b4502699&imgtype=0&src=http%3A%2F%2Fpic44.nipic.com%2F20140720%2F13280487_110503473960_2.jpg\"," \
                  "\"storeName\":\"宴十三·家常菜\",\"shipPrice\":\"4.08\",\"orderPrice\":\"31.98\",\"boxPrice\":\"1.50\"," \
                  "\"couponPrice\":0,\"productPrice\":\"26.40\",\"orderProducts\":[{\"boxPrice\":0.5,\"count\":3," \
                  "\"pid\":\"C430000B001P001\",\"price\":8.8,\"productName\":\"米单纯\",\"brandId\":\"C430000B001\"," \
                  "\"brandImg\":\"https://image.yanss.cn/brand/c430000b001/logo.png\",\"brandName\":\"摇滚米粒\"," \
                  "\"lunchState\":0,\"weight\":100,\"storeCount\":58997}]}],\"vouchers\":[],\"addressId\":10544," \
                  "\"cid\":\"\",\"dinnerCount\":1,\"orderPrice\":\"31.98\",\"shipPrice\":\"4.08\",\"boxPrice\":\"1.50\"," \
                  "\"couponPrice\":0,\"productPrice\":\"26.40\",\"appType\":1," \
                  "\"serviceTimeStr\":\"2018-08-22  12:09:42\",\"dinnerType\":1,\"orderType\":1," \
                  "\"memberRemark\":\"\",\"bookingType\":1}"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url+"dispatch/create", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')
        orderId = self.result["data"]["orderId"]
        return orderId

    # def test_check(self):
    #     querystring = dict()
    #     querystring["orderId"] = self.test_dispatch_create()
    #     headers = {'Cache-Control': "no-cache",}
    #     response = requests.request("GET", base_url_check, headers=headers, params=querystring)
    #     self.result = response.json()
    #     self.assertEqual(self.result["message"], 'success')

    def test_detail_unpaid(self):
        orderId = self.test_dispatch_create()
        payload = "{\n\t\"orderId\":\""+orderId+"\"\n\t\n}"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url+"detail/unpaid", data= payload, headers= headers)
        self.result = response.json()

    def test_unpaid_cancel(self):
        orderId = self.test_dispatch_create()
        payload = "{\n\t\"orderId\":\""+orderId+"\"\n\t\n}"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url+"unpaid/cancel", data= payload, headers= headers)
        self.result = response.json()

    def test_comments_user(self):
        orderId = self.test_dispatch_create()
        payload = "{\"token\":\""+token+"\",\"comments\":\"test123456\"," \
                   "\"orderId\":\""+orderId+"\",\"star\":5}"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url+"comments/user", data= payload, headers= headers)
        self.result = response.json()


    def runTest(self):
        pass


if __name__ == '__main__':
#    test_data.init_data()
    unittest.main()

