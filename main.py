from kivymd.app import MDApp
from kivy.lang import Builder
import json
import requests
<<<<<<< Updated upstream

class Apps(MDApp):

    url = "https://datateste-e5171-default-rtdb.firebaseio.com/.json"

    def patch(self, JSON):
        to_database = json.loads(JSON)
        requests.patch(url = self.url, json = to_database)

    def build(self):
        return Builder.load_file("main.kv")
=======


class Apps(MDApp):
    url = 'https://datateste-e5171-default-rtdb.firebaseio.com/.json'
    def build(self):
        return Builder.load_file("main.kv")

    def patch(self, JSON):
        to_database = json.loads(JSON)
        requests.patch(url = self.url, json = to_database)

>>>>>>> Stashed changes
    
if __name__ == '__main__':
    Apps().run()

#{"Parent":{"Child1": "Value", "Child2": "Value"}}