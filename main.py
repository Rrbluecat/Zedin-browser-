from kivy.app import App
from kivy.uix.label import Label

class ZedinBrowser(App):
    def build(self):
        return Label(text='Zedin Browser')

if __name__ == '__main__':
    ZedinBrowser().run()
