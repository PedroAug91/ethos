from kivymd.app import MDApp
from kivy.lang import Builder
import json
import requests

class Apps(MDApp):

    url = "https://datateste-e5171-default-rtdb.firebaseio.com/.json"

    def patch(self, JSON):
        to_database = json.loads(JSON)
        requests.patch(url = self.url, json = to_database)

    def build(self):
        return Builder.load_file("main.kv")
    
if __name__ == '__main__':
    Apps().run()

#{"Parent":{"Child1": "Value", "Child2": "Value"}}