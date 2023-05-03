#Arranges children in a vertical or horizontal box
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('boxlayout.kv')
class MyLayout(Widget):
    pass


# Class main
class MainClass(App):
    def build(self):
        return MyLayout()
MainClass().run()