import unittest
from crud_requests import *


class CrudTests(unittest.TestCase):
    def test_create_user(self):
        result = create_user("https://petstore.swagger.io/v2/user/", {"id": 12,
                                                                      "username": "oleg70",
                                                                      "firstName": "olegaaa",
                                                                      "lastName": "vasilevvv",
                                                                      "email": "olegoleg@gmail.com",
                                                                      "password": "alehandro01",
                                                                      "phone": "12121212121",
                                                                      "userStatus": 3})
        self.assertTrue(result == "User oleg70 created")

    def test_get_user_by_username(self):
        result = get_user_by_username("https://petstore.swagger.io/v2/user/", "oleg70")
        self.assertTrue(result == "User oleg70 founded")

    def test_loggin(self):
        result = loggin('https://petstore.swagger.io/v2/user/login?username=', "just_oleg", "12345")
        self.assertTrue(result == "User just_oleg has been loggined")

    def test_logout(self):
        result = logout('https://petstore.swagger.io/v2/user/logout')
        self.assertTrue(result == "Logout success")

    def test_create_users_array(self):
        result = create_users_array('https://petstore.swagger.io/v2/user/createWithArray', [{
            "id": 9,
            "username": "Vasiaaaaa",
            "firstName": "Vasia",
            "lastName": "Petrov",
            "email": "petrov@mail.com",
            "password": "1234321",
            "phone": "23423423423",
            "userStatus": 1
        },
            {
                "id": 10,
                "username": "vakabaka",
                "firstName": "Viktor",
                "lastName": "Varlamov",
                "email": "varlamov@google.com",
                "password": "12345678",
                "phone": "234234",
                "userStatus": 0
            }])
        self.assertTrue = (result == "Users added")

    def test_change_user_info(self):
        result = change_user_info("https://petstore.swagger.io/v2/user/", "oleg30", {"id": 1,
                                                                                     "username": "ivanivanov",
                                                                                     "firstName": "ivan",
                                                                                     "lastName": "sinicin",
                                                                                     "email": "ivan@gmail.com",
                                                                                     "password": "strings",
                                                                                     "phone": "12314234",
                                                                                     "userStatus": 2})
        self.assertTrue(result == "Change success")

    def test_delete_user(self):
        result = delete_user("https://petstore.swagger.io/v2/user/", "vakabaka")
        self.assertTrue(result == "User has been deleted")

    if __name__ == '__main__':
        unittest.main()
