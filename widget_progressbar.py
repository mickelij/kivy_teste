from kivy.app import App 
from kivy.uix.progressbar import progressbar

class MinhaApp(App):
    def build(self):
        return progressbar(value=50)
    
if __name__ == "__main__":
    MinhaApp().run()
