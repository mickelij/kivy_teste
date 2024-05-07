from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import label 
from kivy.uix.button import Button
from kivy.uix.textinput import textinput

class MinhaApp(App):
    def build(self):
    
      layout_principal = BoxLayout(orientation = 'vertical')

      self.input_nome = textinput(hit_text='digite seu nome')
      layout_principal.add_widget(self.input_nome)

      botao_enviar = Button(text='enviar', on_press=self.exibir_mensagem)
      layout_principal.add_widget(botao_enviar)

      self.label_mensagem = label()
      layout_principal.add_widget(self.label_mensagem)

      return layout_principal
    
def exibir_mensagem(self, intance):
   nome_usuario = self.input_nome.text
   mensagem = f'olá {nome_usuario} você está avançando no kivy! parabéns.'
   self.label_mensagem.text = mensagem 

if __name__ == '__main__':
   MinhaApp().run()
