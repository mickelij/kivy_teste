from kivy.app import App
from kivy.uix.togglebutton import togglebutton 

class MinhaAPP(App):
    def build(self):
        return togglebutton(text='ligado', state='normal')
    
if __name__ == "__main__":
    MinhaAPP().run()
