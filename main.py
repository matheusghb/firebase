from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.core.window import Window
import firebase_admin
import requests
from firebase import firebase
from firebase_admin import credentials, auth
import pyrebase 

firebase = pyrebase.initialize_app('firebase_config.json')
cred_obj = firebase_admin.credentials.Certificate('firebase_config.json')
user = auth.sign_in_with_email_and_password('mistermquack124@gmail.com', 123456)
db = firebase.database()


Window.clearcolor = (1,1,1,1)
class Gerenciador(ScreenManager):
   pass

class Logado (Screen):
   pass

class Cadastro(Screen):
   pass

class Login(Screen):
   pass

class Login(App):
    def build(self):
        return Builder.load_file('main.kv')
    
    def Cadastrar(self):
      import json
      email = self.root.get_screen('cadastro').ids.email.text 
      senha = self.root.get_screen('cadastro').ids.senha.text

      user_data = {
         'E-mail': (email),
         'Senha': (senha)
      }

      firebase.post('login-9ce90-default-rtdb/Users', data=json.dumps(user_data))
      print('funcionou')
    

    def log(self):
      import json
      email = self.root.get_screen('login').ids.email.text
      senha = self.root.get_screen('login').ids.senha.text

      project_id = "login-9ce90"
      node_name = 'Users'
      
      url = f"https://{project_id}.firebaseio.com/{node_name}.json"
      
      user_data = {
         'E-mail': email,
         'Senha': senha
      }
      
      response = requests.post(url, data=json.dumps(user_data))
      print (response.status_code)

      if response.status_code in (200, 201):
         self.root.current = "logado"
      else:
         self.root.get_screen('login').ids.l.color = (1, 0, 0, 1)



if __name__ == "__main__":
 Login().run()