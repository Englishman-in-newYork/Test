import json
import requests


def create_user(url, user_param):
    request = requests.post(url, json=user_param)
    date = request.status_code
    if date == 200:
        return "User " + user_param["username"] + " created"
    elif date == 401:
        return "Eror"


print(create_user("https://petstore.swagger.io/v2/user/", {"id": 12,
                                                           "username": "oleg80",
                                                           "firstName": "olegaaa",
                                                           "lastName": "vasilevvv",
                                                           "email": "olegoleg@gmail.com",
                                                           "password": "alehandro01",
                                                           "phone": "12121212121",
                                                           "userStatus": 3}))


def get_user_by_username(url, username):
    request = requests.get(url + username)
    if request.status_code == 200:
        return "User " + username + " founded"


print(get_user_by_username("https://petstore.swagger.io/v2/user/", "oleg80"))


def loggin(url, username, password):
    responce = requests.get(url + username + "$password=" + password)
    if responce.status_code == 200:
        return "User " + username + " has been loggined"


print(loggin('https://petstore.swagger.io/v2/user/login?username=', "valek", "12345"))


def logout(url):
    responce = requests.get(url)
    if responce.status_code == 200:
        return "Logout success"


print(logout('https://petstore.swagger.io/v2/user/logout'))


def create_users_array(url, users_array):
    request = requests.post(url, json=users_array)
    if request.status_code == 200:
        return "Users added"


print(create_users_array('https://petstore.swagger.io/v2/user/createWithArray', [{
    "id": 8,
    "username": "ali",
    "firstName": "ali",
    "lastName": "bali",
    "email": "bali@mail.com",
    "password": "aaaaaaaa",
    "phone": "129",
    "userStatus": 8
},
    {
        "id": 7,
        "username": "vakabaka",
        "firstName": "Bakanets",
        "lastName": "alalal",
        "email": "baka@google.com",
        "password": "12345678",
        "phone": "234234",
        "userStatus": 7
    }]))


def change_user_info(url, user, param):
    request = requests.put(url + user, json=param)
    if request.status_code == 200:
        return "Change success"


print(change_user_info("https://petstore.swagger.io/v2/user/", "oleg80", {"id": 1,
                                                                          "username": "ivanivanov",
                                                                          "firstName": "ivan",
                                                                          "lastName": "sinicin",
                                                                          "email": "ivan@gmail.com",
                                                                          "password": "strings",
                                                                          "phone": "12314234",
                                                                          "userStatus": 2}))


def delete_user(url, username):
    delete_request = requests.delete(url + username)
    responce = delete_request.status_code
    if responce == 200:
        return "User has been deleted"


print(delete_user("https://petstore.swagger.io/v2/user/", "ivanivanov"))
