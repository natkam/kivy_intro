import kivy

kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        self.title = "Ceci n'est pas une application"
        return Label(text="Hello world", font_size=36, bold=True)

    def on_start(self):
        print("YAY! started!!!")
        super().on_start()

    def on_stop(self):
        print("STOP, DOH")
        super().on_stop()


if __name__ == "__main__":
    MyApp().run()
