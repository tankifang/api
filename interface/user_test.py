# -*- coding: utf-8 -*-

import unittest
import requests
import os, sys
from product_test import product
#from db_fixture import test_data

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

token = "20180000000000TEST-MEMBER-TEST"

base_url = "https://m.yanss.cn/api/v1/user/"

class user(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
        #print(self.result)

    def test_token_to_member(self):
        querystring = dict()
        querystring["token"] = token
        response = requests.request("GET", base_url + "tokenToMember",  params=querystring)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')

    def test_index_coupon(self):
        brandId =product().test_index()
        payload = "{\n\t\"token\":\""+token+"\"\n,\"brandId\":\""+brandId+"\"}\n"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url + "index/coupon", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')


    def test_find_coupon_list(self):
        brandId =product().test_index()
        payload = "{\n\t\"token\":\""+token+"\"\n,\"brandId\":\""+brandId+"\"}\n"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url + "findCouponList", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')

    def test_find_exchanges(self):
        brandId =product().test_index()
        payload = "{\n\t\"token\":\""+token+"\"\n,\"brandId\":\""+brandId+"\"}\n"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url + "findExchanges", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')

    def test_find_address_list(self):
        payload = "{\n\t\"token\":\""+token+"\"\n}\n"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url + "findAddressList", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')

    def test_find_address_list_1(self):
        brandId =product().test_index()
        payload = "{\n\t\"token\":\""+token+"\"\n,\"brandId\":\""+brandId+"\"}\n"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url + "findAddressList", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')

    def test_insert_address(self):
        payload = "{\n\t\"addressId\":0,\n\t\"lat\":0.0,\n\t\"lng\":0.0," \
                  "\n\t\"memberAddress\":{\n\t\t\"address\":\"湖北省武汉市江夏区\"," \
                  "\n\t\t\"addressDetail\":\"金融港现代森林小镇\",\n\t\t\"addressId\":0," \
                  "\n\t\t\"addressName\":\"森林小镇\",\n\t\t\"isDefault\":0," \
                  "\n\t\t\"lat\":30.485193,\n\t\t\"lng\":114.404681,\n\t\t\"receiverName\":\"yanshis\"," \
                  "\n\t\t\"receiverPhone\":\"12345678910\",\n\t\t\"receiverSex\":0," \
                  "\n\t\t\"status\":0,\n\t\t\"storeId\":0\n\t\t\n\t},\n\t\"token\":\""+token+"\"\n\t\n}"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url + "insertAddress", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], u'插入成功')
        addressId = self.result["data"]
        return  addressId

    def test_updata_address(self):
        addressId = self.test_insert_address()
        payload = "\n{\n\t\"memberAddress\":\n\t{\n\t\"addressId\":\""+addressId+"\"," \
                "\n\t\t\"receiverName\":\"维他奶\"," \
                "\n\t\t\"receiverPhone\":\"17344444444\",\n\t\t\"receiverSex\":0," \
                "\n\t\t\"address\":\"湖北省武汉市江夏区\"\n\t\t,\"addressDetail\":\"金融港现代森林小镇\"," \
                "\n\t\t\"addressName\":\"jiangxia\",\n\t\t\"isDefault\":1,\n\t\t\"lng\":0," \
                "\n\t\t\"lat\":0\n\t\t\n\t},\n\t\"token\":\""+token+"\"\n\t\n}"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url + "updataAddress", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')

    def test_delete_address(self):
        addressId = self.test_insert_address()
        payload = "{\n\t\"addressId\":\""+bytes(addressId)+"\",\n\t\"token\":\""+token+"\"\n}\n"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url + "deleteAddress", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')



    def test_feed_back(self):
        payload = "{\n\t\"token\":\""+token+"\"\n,\"content\":\"test123456\"}\n"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url + "feedback", data=payload, headers=headers)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')

if __name__ == '__main__':
#    test_data.init_data()
    unittest.main()

