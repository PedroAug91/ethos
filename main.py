from kivymd.app import MDApp
from kivy.lang import Builder
from firebase import firebase
import json
import requests

class Apps(MDApp):

    def send_data(self, name, email, password):
        firebase = firebase.FirebaseApplication('https://testando-ae5b2-default-rtdb.firebaseio.com/', None)

        data = {
            'Name': name,
            'Email': email,
            'Password': password
        }

        firebase.post('https://testando-ae5b2-default-rtdb.firebaseio.com/Users', data)
    
    def verify_data(self, email, password):
        firebase = firebase.FirebaseApplication('https://testando-ae5b2-default-rtdb.firebaseio.com/', None)
        result = firebase.get('https://testando-ae5b2-default-rtdb.firebaseio.com/Users', '')

        for i in result.keys():
            if result[i]['Email'] == email:
                if result[i]['Password'] == password:
                    pass


    def build(self):
        return Builder.load_file("main.kv")
 
if __name__ == '__main__':
    Apps().run()

# result = firebase.get('https://testando-ae5b2-default-rtdb.firebaseio.com/Users', '')
# print(result)