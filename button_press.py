from kivy.app import App 
from kivy.uix.button import Button

def botao_pressionado(instance):
    print("botão pressionado")

class MinhaApp(App):
    def build(self):
        btn = Button(text=' não clique aqui por favor', size_hint=(0.5, 0.2))
        btn.bind(on_press=botao_pressionado)
        return btn
    
if __name__ == "__main__":
    MinhaApp().run()
