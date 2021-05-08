import json
from django.test import Client, TestCase


class MyTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        from userdb.models import CourseDesigner as CD
        CD.objects.create(username="admin", password="123456", fullname="admin")
        pass

    def tearDown(self):
        pass

    def test_empty_username_or_password(self):
        # Test receive no name and password
        response = self.client.post("/login/", {'username': '', 'password': ''})
        resp_dict = json.loads(response.content)
        # print(resp_dict)
        # assert if the code in the dict
        self.assertIn("code", resp_dict)
        # compare the code value 1001
        code = resp_dict.get("code")
        self.assertEqual(code, 1001)
        msg = resp_dict.get('message')
        self.assertEqual(msg, "Parameter incomplete!")

        # Test only receive name
        response = self.client.post("/login/", {"username": "admin", "password": ''})
        # response data
        resp_dict = json.loads(response.content)
        # use assert to verify
        self.assertIn("code", resp_dict)
        # compare the code value 1001
        code = resp_dict.get("code")
        self.assertEqual(code, 1001)
        # return message
        msg = resp_dict.get('message')
        self.assertEqual(msg, "Parameter incomplete!")

        # Test only receive password
        response = self.client.post("/login/", {"username": "", "password": '12345'})
        # response data
        resp_dict = json.loads(response.content)
        # use assert to verify
        self.assertIn("code", resp_dict)
        # compare the code value 1001
        code = resp_dict.get("code")
        self.assertEqual(code, 1001)
        # return message
        msg = resp_dict.get('message')
        self.assertEqual(msg, "Parameter incomplete!")

    def test_wrong_name_password(self):
        # Test receive wrong name and password
        response = self.client.post("/login/", {"username": "admin2", "password": '12345'})
        resp_dict = json.loads(response.content)
        # print(resp_dict)
        # assert if the code in the dict
        self.assertIn("code", resp_dict)
        # compare the code value 1001
        code = resp_dict.get("code")
        self.assertEqual(code, 1002)
        msg = resp_dict.get('message')
        self.assertEqual(msg, "Not correct username or password!")

    def test_correct_name_password(self):
        # Test receive correct name and password
        response = self.client.post("/login/", {'username': 'admin', 'password': '123456'})
        resp_dict = json.loads(response.content)
        # assert if the code in the dict
        self.assertIn('code', resp_dict)
        # compare the code value 1001
        code = resp_dict.get('code')
        self.assertEqual(code, 0)
        msg = resp_dict.get('message')
        self.assertEqual(msg, 'Success!')

    def test_search_empty_keywords(self):
        # Test receive correct name and password
        response = self.client.get("/search/", {'keywords': ''})
        resp_dict = json.loads(response.content)
        # assert if the code in the dict
        self.assertIn('code', resp_dict)
        # compare the code value 1001
        code = resp_dict.get('code')
        self.assertEqual(code, 1001)
        msg = resp_dict.get('message')
        self.assertEqual(msg, 'No keywords!')

    def test_search_valid_keywords(self):
        # Test receive correct name and password
        response = self.client.get("/search/", {'keywords': 'test string'})
        resp_dict = json.loads(response.content)
        # assert if the code in the dict
        self.assertIn('code', resp_dict)
        # compare the code value 1001
        code = resp_dict.get('code')
        self.assertEqual(code, 0)
        msg = resp_dict.get('message')
        self.assertEqual(msg, 'Search success!')


if __name__ == '__main__':
    TestCase()

# TestCase.main()
