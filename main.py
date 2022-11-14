from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from firebase import firebase
from kivy.core.window import Window

sm = MDScreenManager()

class InitialScreen(MDScreen):
    pass

class SignUpScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    pass

class TimeLineScreen(MDScreen):
    pass
 
class AboutScreen(MDScreen):
    pass

class ForgetPassWordScreen(MDScreen):
    pass


sm.add_widget(InitialScreen(name="initial"))
sm.add_widget(SignUpScreen(name="signup"))
sm.add_widget(LoginScreen(name="login"))
sm.add_widget(TimeLineScreen(name="timeline"))
sm.add_widget(AboutScreen(name="about"))
sm.add_widget(ForgetPassWordScreen(name="recpaswrd"))


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

    def rst_pswrd(self, email, password):
        from firebase import firebase

        firebase = firebase.FirebaseApplication('https://testando-ae5b2-default-rtdb.firebaseio.com/', None)
        result = firebase.get('https://testando-ae5b2-default-rtdb.firebaseio.com/Users', '')

        for i in result.keys():
            dados = {'Password': password}
            if result[i]['Email'] == email and result[i]['Password'] != password:
                firebase.patch(f'https://testando-ae5b2-default-rtdb.firebaseio.com/Users/{i}', dados)
                return 'troca'


    def build(self):
        Window.size = (400, 600)

        return Builder.load_file("main.kv")
 
if __name__ == '__main__':
    Apps().run()

# result = firebase.get('https://testando-ae5b2-default-rtdb.firebaseio.com/Users', '')
# print(result)
