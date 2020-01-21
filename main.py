import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.label import Label


class FormScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2
        self.add_widget(Label(text="Say your name!"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Now say something more:"))
        self.more = TextInput(multiline=False)
        self.add_widget(self.more)



class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        self.title = "PONG! - Ceci n'est pas une application"
        return PongGame()

    def on_start(self):
        print("YAY! started!!!")
        super().on_start()

    def on_stop(self):
        print("STOP, DOH")
        super().on_stop()


if __name__ == "__main__":
    PongApp().run()
