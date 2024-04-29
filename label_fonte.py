from kivy.app import App 
from kivy.uix.label import Label 


class MinhaApp(App):
    def build(self):
        return Label(text='Bob esponja calça quadrada', font_size=100)
    
    
if __name__ == "__main__":
    MinhaApp().run()    
