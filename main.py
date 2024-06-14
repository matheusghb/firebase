from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.core.window import Window
import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('firebase_config.json')

Window.clearcolor = (1,1,1,1)
class Gerenciador(ScreenManager):
   pass

class Cadastro(Screen):
   pass

class Login(Screen):
   pass

class Login(App):
    def build(self):
        return Builder.load_file('main.kv')
    
    def Cadastrar(self):

      import requests
      import json
      from firebase_admin import db
      firebase_admin.initialize_app(cred_obj)

      email = self.root.get_screen('Cadastro').ids.email.text 
      senha = self.root.get_screen('Cadastro').ids.senha.text

      user_data = {
         'E-mail': (email),
         'Senha': (senha)
      }
      ref.child('users').push(user_data)
      print('funcionou')

      ref = db.reference ('/')
    
if __name__ == "__main__":
 Login().run()