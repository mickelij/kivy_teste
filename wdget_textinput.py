from kivy.app import App 
from kivy.uix.textinput import textinput 

class MinhaApp(App):
    def build(self):
        return textinput(text='Digite aqui')
    
if __name__ == "__main__":
    MinhaApp().run()
