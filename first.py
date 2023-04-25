import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout,self).__init__(**kwargs)
        # Grid
        self.cols=1
        self.row_force_default=True
        self.row_default_height=120
        # Creating another grid
        self.top_grid=GridLayout(
        row_force_default=True,
        row_default_height=50,
        col_force_default=True,
        col_default_width=100
        )
        self.top_grid.cols=2
        
        # Define name
        self.top_grid.add_widget(Label(text="Name:",
                        # size_hint_y=None,
                        # height=50,
                        # size_hint_x=None,
                        # width=100
                                       
                                       ))
        self.name=TextInput(multiline=True,
                        # size_hint_y=None,
                        # height=50,
                        # size_hint_x=None,
                        # width=150
                            
                            )
        self.top_grid.add_widget(self.name)
        # Define Favorite food
        self.top_grid.add_widget(Label(text="Favorite Color"))
                        # size_hint_y=None,
                        # height=50,
                        # size_hint_x=None,
                        # width=100))
        self.food=TextInput(multiline=False,
                        #     size_hint_y=None,
                        # height=50,
                        # size_hint_x=None,
                        # width=150
                            )
        self.top_grid.add_widget(self.food)
        # Adding button to the page
        self.add_widget(self.top_grid)
        
        self.btn=Button(text="Submit",font_size=32,
                        size_hint_y=None,
                        height=50,
                        size_hint_x=None,
                        width=120

                        )
        
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.press)
    def press(self,instance):
        name=self.name.text
        food=self.food.text
        # Printing the result
        # print(f'your name is {name} and your favorite color is {food}')
        self.add_widget(Label(text=f'your name is {name} and your favorite color is {food}'))
        # Clear the input fields
        self.name.text=''
        self.food.text=''

        

class MyClass(App):
    def build(self):
        return MyGridLayout()
MyClass().run()

