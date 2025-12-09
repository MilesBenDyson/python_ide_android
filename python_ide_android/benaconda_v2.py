from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
from kivy.uix.settings import SettingsWithSidebar
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty
import sys
import io


class PythonIDE(BoxLayout):
    editor_font_size = NumericProperty(16)
    output_font_size = NumericProperty(16)
    output_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Hintergrundfarbe (Mintgrün)
        Window.clearcolor = (0.85, 0.95, 0.90, 1)

        # Editor
        self.editor = TextInput(
            text="# Schreibe deinen Python-Code hier\nprint('Hallo Ben!')",
            font_size=self.editor_font_size,
            size_hint_y=0.7,
            multiline=True,
        )

        editor_scroll = ScrollView(size_hint_y=0.7)
        editor_scroll.add_widget(self.editor)

        # RUN Button
        run_button = Button(
            text="Code ausführen",
            size_hint_y=0.1,
            font_size=18
        )
        run_button.bind(on_press=self.run_code)

        # Ausgabe-Feld
        self.output = TextInput(
            text="Ausgabe erscheint hier...",
            readonly=True,
            font_size=self.output_font_size,
            size_hint_y=0.2,
            background_color=(1, 1, 1, 1)
        )

        output_scroll = ScrollView(size_hint_y=0.2)
        output_scroll.add_widget(self.output)

        # Touch zum Löschen
        self.output.bind(on_touch_down=self.hide_output)

        # ESC-Taste zum Löschen
        Window.bind(on_key_down=self.key_handler)

        self.add_widget(editor_scroll)
        self.add_widget(run_button)
        self.add_widget(output_scroll)

    def run_code(self, *args):
        """Führt den Python-Code sicher aus."""
        code = self.editor.text
        sys_stdout = io.StringIO()

        try:
            sys.stdout = sys_stdout
            exec(code, {"__builtins__": __builtins__})
            result = sys_stdout.getvalue()
        except Exception as e:
            result = f"Fehler:\n{e}"
        finally:
            sys.stdout = sys.__stdout__

        self.output.text = result.strip() if result else "(Keine Ausgabe)"

    def hide_output(self, *args):
        self.output.text = ""
        return False

    def key_handler(self, window, key, *args):
        if key == 27:  # ESC
            self.output.text = ""
            return True
        return False


class PythonIDEApp(App):
    def build(self):
        self.settings_cls = SettingsWithSidebar()
        ide = PythonIDE()

        # Schriftgrößen beim Laden aus der config übernehmen
        cfg = self.config
        ide.editor_font_size = cfg.getint("editor", "font_size_editor")
        ide.output_font_size = cfg.getint("editor", "font_size_output")

        ide.editor.font_size = ide.editor_font_size
        ide.output.font_size = ide.output_font_size

        return ide

    def build_config(self, config):
        config.setdefaults("editor", {
            "font_size_editor": 16,
            "font_size_output": 16
        })

    def build_settings(self, settings):
        json_settings = """
        [
            {
                "type": "numeric",
                "title": "Schriftgröße Editor",
                "section": "editor",
                "key": "font_size_editor"
            },
            {
                "type": "numeric",
                "title": "Schriftgröße Ausgabe",
                "section": "editor",
                "key": "font_size_output"
            }
        ]
        """
        settings.add_json_panel("Einstellungen", self.config, data=json_settings)

    def on_config_change(self, config, section, key, value):
        ide = self.root
        if key == "font_size_editor":
            ide.editor_font_size = int(value)
            ide.editor.font_size = int(value)
        elif key == "font_size_output":
            ide.output_font_size = int(value)
            ide.output.font_size = int(value)


if __name__ == "__main__":
    PythonIDEApp().run()
