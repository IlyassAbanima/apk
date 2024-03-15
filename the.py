from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CalculatorApp(App):

    def build(self):
        self.equation = ''
        main_layout = BoxLayout(orientation='vertical')
        self.result_label = ResultLabel(text='', font_size=40)
        main_layout.add_widget(self.result_label)

        buttons_layout = BoxLayout(orientation='vertical')
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            row_layout = BoxLayout()
            for label in row:
                button = Button(text=label, on_press=self.on_button_press)
                row_layout.add_widget(button)
            buttons_layout.add_widget(row_layout)

        main_layout.add_widget(buttons_layout)
        return main_layout

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.result_label.text = str(eval(self.equation))
            except:
                self.result_label.text = 'Error'
            self.equation = ''
        elif instance.text == 'C':
            self.equation = ''
            self.result_label.text = ''
        else:
            self.equation += instance.text
            self.result_label.text = self.equation


class ResultLabel(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.disabled = True
        self.background_color = (1, 1, 1, 1)
        self.background_normal = ''
        self.background_down = ''
        self.height = 100
        self.text_size = self.size


if __name__ == '__main__':
    CalculatorApp().run()
