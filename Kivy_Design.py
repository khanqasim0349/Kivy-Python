import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
class MyGridLayout(Widget):
    name=ObjectProperty(None)
    password=ObjectProperty(None)





    def press(self):
        name=self.name.text
        password=self.password.text
        print(f"name is {name} and password is {password}")
        # Clear the fields
        self.name.text=''
        self.password.text=''

class MyClass(App):
    def build(self):
        return MyGridLayout()
MyClass().run()