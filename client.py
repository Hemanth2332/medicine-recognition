import requests


def send_img():
    img = {"file": open("test_image/test3.jpg", "rb")}
    params = {"user_id": "user_id_7"}
    url = "http://127.0.0.1:8000/api/image"
    content = requests.post(url=url, files=img, params=params)
    print(content.json())


def del_data():
    med_data = {"data":"medicine2"}

    header = {"accept": "application/json","Content-Type": "application/json"}

    res = requests.post("http://127.0.0.1:8000/api/del_med_data",
                        params={"user_id": "user_id_9"},
                        json=med_data, 
                        headers=header,
                        )
    print(res.json())


def add_data():
    med_data = {"data":{"test": "just a test"}}

    header = {"accept": "application/json","Content-Type": "application/json"}

    res = requests.post("http://127.0.0.1:8000/api/update_med_data",
                        params={"user_id": "user_id_7"},
                        json=med_data, 
                        headers=header,
                        )
    print(res.json())


def update_data():
    med_data = {"data":{"medicine2": "1-2-3-4"}}

    header = {"accept": "application/json","Content-Type": "application/json"}

    res = requests.post("http://127.0.0.1:8000/api/update_med_data",
                        params={"user_id": "user_id_9"},
                        json=med_data, 
                        headers=header,
                        )
    print(res.json())


def create_user():
    res = requests.post("http://127.0.0.1:8000/api/create_user", params={"user_id": "user_id_9"})
    print(res.json())


def del_user():
    res = requests.post("http://127.0.0.1:8000/api/delete_user", params={"user_id": "user_id_9"})
    print(res.json())

def user():
    res = requests.post("https://6b04-111-93-231-194.ngrok-free.app/", params={"user_id": "hello this is a test by mugu"})
    print(res.json())


send_img()