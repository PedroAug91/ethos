from kivymd.app import MDApp
from kivy.lang import Builder
from firebase import firebase
from kivy.core.window import Window
import json
import requests

class Apps(MDApp):
    def send_data(self, name, email, password):
        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://testando-ae5b2-default-rtdb.firebaseio.com/', None)

        if '@' in email and '.com' in email or '.br' in email:
            data = {
                'Name': name,
                'Email': email,
                'Password': password
            }
            firebase.post('https://testando-ae5b2-default-rtdb.firebaseio.com/Users', data)
            return 'emailcorreto'
        else:
            return 'emailinva'

    def verify_data(self, email, password):
        from firebase import firebase

        firebase = firebase.FirebaseApplication('https://testando-ae5b2-default-rtdb.firebaseio.com/', None)
        result = firebase.get('https://testando-ae5b2-default-rtdb.firebaseio.com/Users', '')

        for i in result.keys():
            if result[i]['Email'] == email:
                if result[i]['Password'] == password:
                    return 'tudocerto'

    def build(self):
        Window.size = (400, 600)

        return Builder.load_file("main.kv")
 
if __name__ == '__main__':
    Apps().run()

# result = firebase.get('https://testando-ae5b2-default-rtdb.firebaseio.com/Users', '')
# print(result)