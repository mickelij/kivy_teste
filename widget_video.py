from kivy.app import App 
from kivy.uix.video import Video

class MinhaApp(App):
    def build(self):
        return Video(source='caminho/para/video/seu/video.mp4')
    
if __name__ == "__name__":
    MinhaApp().run()
