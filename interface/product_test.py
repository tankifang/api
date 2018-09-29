# -*- coding: utf-8 -*-

import unittest
import requests
import os, sys
#from db_fixture import test_data

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

base_url = "https://m.yanss.cn/api/v1/product/"

class product(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_near_area(self):
        querystring = {"lng":"114.399596","lat":"30.506067"}
        response = requests.request("GET", base_url + "findNearArea",  params=querystring)
        self.result = response.json()
        cityId = self.result['data']['cityId']
        return cityId
        self.assertEqual(self.result['message'], 'success')

    def test_index(self):
        cityId = self.test_find_near_area()
        querystring = dict()
        querystring["cityId"] = cityId
        response = requests.request("GET", base_url + "index",  params=querystring)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')
        brandId = self.result['data']['brands'][0]["brandId"]
        return brandId

    def test_find_brand(self):
        brandId = self.test_index()
        payload = "{\n\t\"brandId\":\""+brandId+"\"\n}\n"
        headers = {'Content-Type': "application/json",'Cache-Control': "no-cache"}
        response = requests.request("POST", base_url + "findBrand", data=payload, headers=headers)
        self.result = response.json()
        pid = self.result['data']['sellWell'][0]['pid']
        return pid
        self.assertEqual(self.result['message'], 'success')

    def test_detail(self):
        pid = self.test_find_brand()
        querystring = dict()
        querystring["pid"] = pid
        response = requests.request("GET",base_url + "detail",  params=querystring)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')
        brandId = self.result['data']['brandId']
        return brandId

    def test_find_recommend(self):
        brandId = self.test_detail()
        querystring = dict()
        querystring["brandId"] = brandId
        response = requests.request("GET",base_url + "findRecommend",  params=querystring)
        self.result = response.json()
        self.assertEqual(self.result['message'], 'success')

    def runTest(self):
        pass


if __name__ == '__main__':
#    test_data.init_data()
    unittest.main()

