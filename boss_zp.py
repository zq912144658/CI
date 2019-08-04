#coding=utf-8

import unittest
import requests
import warnings

class TestA(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.url = "https://passport.abcfintech.com/sso/email/login"
        self.s = requests.session()
        self.g = globals()

    def test_a(self):
        params = {"email":"15710025146@163.com",
                  "password":"qwerty12345"
                   }
        #self.s.headers.update({"Cookie":self.cookie})
        result = self.s.post(url=self.url,data=params)
        print(result.json())
        token = "$2a$10$kL6Cxa.4Hd/VNEAkYUpKSuzSibFs4S/"
        self.assertEqual(result.json()['data']['token'],token)
        token = result.json()['data']['token']
        self.g["token"] = token
        self.g['ticket'] = result.json()['data']['ticket']
        self.g['userId'] = result.json()['data']['userId']
        return token

    # def test_b(self):
    #     '''用例a'''
    #     result_a = "$2a$10$kL6Cxa.4Hd/VNEAkYUpKSuzSibFs4S/"    # 用例a的返回值
    #     # 返回值先给全部办理，存到字典对应key,  个劳保丝
    #     a = self.g["a"]
    #     print(a)
    #     self.assertEqual(result_a,a)

    def test_c(self):
        '''用例b'''
        account_url = "https://passport.abcfintech.com/sso/getTokenByTicket"
        params = {"ticket":self.g['ticket'],
                  "userId":self.g['userId']}
        account = self.s.get(url=account_url,params=params).json()
        print(account)

if __name__ == '__main__':
    unittest.main()