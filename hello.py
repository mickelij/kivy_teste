from kivy.app import App
from kivy.uix.button import Button
class MyApp(App):
    def build(self):
        return Button(text= "OI, eu quero ser rica e morar em um apartamento em NY")
if __name__ == '__main__':
    MyApp().run() 
