from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.webview import WebView

class Tarayici(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Üst bar
        self.ust_bar = BoxLayout(
            size_hint_y=None,
            height=50
        )
        
        # Adres çubuğu
        self.adres = TextInput(
            text='https://google.com',
            multiline=False,
            size_hint_x=0.8
        )
        
        # Git butonu
        self.git_btn = Button(
            text='Git',
            size_hint_x=0.2
        )
        self.git_btn.bind(on_press=self.sayfaya_git)
        
        self.ust_bar.add_widget(self.adres)
        self.ust_bar.add_widget(self.git_btn)
        
        # WebView
        self.webview = WebView(
            url='https://google.com',
            size_hint_y=1
        )
        
        self.add_widget(self.ust_bar)
        self.add_widget(self.webview)
    
    def sayfaya_git(self, instance):
        self.webview.url = self.adres.text

class ZedinBrowser(App):
    def build(self):
        return Tarayici()

if __name__ == '__main__':
    ZedinBrowser().run()
