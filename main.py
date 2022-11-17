from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from firebase import firebase
from kivy.core.window import Window

sm = MDScreenManager()

class TLCard(MDCard):
    pass


class InitialScreen(MDScreen):
    pass

class SignUpScreen(MDScreen):
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

class LoginScreen(MDScreen):
    def verify_data(self, email, password):
        from firebase import firebase

        firebase = firebase.FirebaseApplication('https://testando-ae5b2-default-rtdb.firebaseio.com/', None)
        result = firebase.get('https://testando-ae5b2-default-rtdb.firebaseio.com/Users', '')

        for i in result.keys():
            if result[i]['Email'] == email:
                if result[i]['Password'] == password:
                    self.ids.lbl.text = 'foi'
                    return True
            else:
                self.ids.lbl.text = 'nao foi'


class TimeLineScreen(MDScreen):
    pass
class AboutScreen(MDScreen):
    pass

class ForgetPassWordScreen(MDScreen):
        def rst_pswrd(self, email, password):
            from firebase import firebase

            firebase = firebase.FirebaseApplication('https://testando-ae5b2-default-rtdb.firebaseio.com/', None)
            result = firebase.get('https://testando-ae5b2-default-rtdb.firebaseio.com/Users', '')

            for i in result.keys():
                dados = {'Password': password}
                if result[i]['Email'] == email and result[i]['Password'] != password:
                    firebase.patch(f'https://testando-ae5b2-default-rtdb.firebaseio.com/Users/{i}', dados)
                    self.ids.lbrec.text = 'Senha recuperada com sucesso'

class NewPostScreen(MDScreen):
    def new_post(self,titulo,texto):
        MDApp.get_running_app().root.ids.timeline_id.ids.box_timeline.add_widget(
                TLCard(
                    MDLabel(
                        text=titulo),
                    MDLabel(
                        text=texto),
                    size_hint=(.9,None),
                    height=200,
                    md_bg_color=(1,1,1,1),
                    pos_hint={"center_x": .5}
                    )
                )

sm.add_widget(NewPostScreen(name="newpost"))
sm.add_widget(InitialScreen(name="initial"))
sm.add_widget(SignUpScreen(name="signup"))
sm.add_widget(LoginScreen(name="login"))
sm.add_widget(TimeLineScreen(name="timeline"))
sm.add_widget(AboutScreen(name="about"))
sm.add_widget(ForgetPassWordScreen(name="recpaswrd"))


class Apps(MDApp):
    def build(self):
        Window.size = (400, 600)
        self.theme_cls.material_style = "M3"
        return Builder.load_file("main.kv")
 
if __name__ == '__main__':
    Apps().run()
