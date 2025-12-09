from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.settings import SettingsWithSidebar
from kivy.config import ConfigParser

from kivy.uix.codeinput import CodeInput
from pygments.lexers import PythonLexer


class PythonIDE(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        app = App.get_running_app()

        # Editor mit Syntax Highlighting
        self.editor = CodeInput(
            lexer=PythonLexer(),
            tab_width=4,
            font_size=16,
            size_hint_y=0.65,
            auto_indent=True,
            keyboard_mode="managed" if app.use_internal_keyboard else "system",
        )
        self.editor.text = "# Schreibe deinen Python-Code hier\nprint('Hallo Ben!')"
        self.add_widget(self.editor)

        # Ausgabe-Feld
        self.output = TextInput(
            text="Ausgabe erscheint hier...",
            multiline=True,
            readonly=True,
            font_size=16,
            size_hint_y=0.25
        )
        self.add_widget(self.output)

        # RUN-Button
        run_button = Button(
            text="Code ausführen",
            size_hint_y=0.15,
            font_size=20
        )
        run_button.bind(on_press=self.run_code)
        self.add_widget(run_button)

    def run_code(self, *_):
        import sys, io

        code = self.editor.text
        backup = sys.stdout
        sys.stdout = io.StringIO()

        try:
            exec(code, {})
            output = sys.stdout.getvalue()
        except Exception as e:
            output = "Fehler:\n" + str(e)

        sys.stdout = backup
        self.output.text = output


class PythonIDEApp(App):

    use_internal_keyboard = True

    def build(self):
        self.settings_cls = SettingsWithSidebar()
        return PythonIDE()

    def build_config(self, config):
        config.setdefaults("keyboard", {
            "use_internal": True
        })

    def build_settings(self, settings):
        settings.add_json_panel(
            "Einstellungen",
            self.config,
            data="""
            [
                {
                    "type": "bool",
                    "title": "Interne Handy-Tastatur benutzen",
                    "desc": "Wenn deaktiviert → nur externe Tastatur.",
                    "section": "keyboard",
                    "key": "use_internal"
                }
            ]
            """
        )

    def on_config_change(self, config, section, key, value):
        if section == "keyboard" and key == "use_internal":
            self.use_internal_keyboard = value == "1"
            self.stop()
            self.run()


if __name__ == "__main__":
    PythonIDEApp().run()
