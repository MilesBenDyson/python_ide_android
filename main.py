from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.uix.settings import Settings
import io
import sys

Window.clearcolor = (0.85, 0.95, 0.90, 1)


class BenacondaApp(App):
    editor_font_size = NumericProperty(16)
    output_font_size = NumericProperty(16)

    def build(self):
        self.settings_cls = Settings

        root = BoxLayout(orientation='vertical', spacing=5, padding=5)

        # ------------------------------
        # TOP-BAR mit Settings Icon
        # ------------------------------
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        top_bar.add_widget(Label(size_hint_x=1))

        settings_button = Button(
            text="⚙",
            font_size=24,
            size_hint=(None, None),
            size=(50, 50)
        )
        settings_button.bind(on_press=lambda x: self.open_settings())
        top_bar.add_widget(settings_button)

        # ------------------------------
        # EDITOR
        # ------------------------------
        self.editor = TextInput(
            multiline=True,
            font_size=self.editor_font_size,
            size_hint_y=1,
            hint_text="Python-Code hier eingeben..."
        )

        # ------------------------------
        # RUN BUTTON
        # ------------------------------
        run_button = Button(
            text="Code ausführen",
            height=60,
            size_hint_y=None,
            font_size=18
        )
        run_button.bind(on_press=self.run_code)

        # ------------------------------
        # OUTPUT – versteckt am Anfang
        # ------------------------------
        self.output = TextInput(
            multiline=True,
            readonly=True,
            font_size=self.output_font_size,
            size_hint_y=0.5,
            opacity=0
        )
        self.output_visible = False

        self.output.bind(on_touch_down=self.hide_output)
        Window.bind(on_key_down=self.key_handler)

        root.add_widget(top_bar)
        root.add_widget(self.editor)
        root.add_widget(run_button)
        root.add_widget(self.output)

        return root

    # ------------------------------
    # OUTPUT EIN-/AUSBLENDEN
    # ------------------------------
    def show_output(self):
        self.output.opacity = 1
        self.output_visible = True

    def hide_output(self, *args):
        self.output.opacity = 0
        self.output.text = ""
        self.output_visible = False

    def key_handler(self, window, key, scancode, codepoint, modifiers):
        # "Back" auf Android
        if key == 27:
            if self.output_visible:
                self.hide_output()
            else:
                App.get_running_app().stop()
            return True

    # ------------------------------
    # CODE AUSFÜHREN
    # ------------------------------
    def run_code(self, instance):
        code = self.editor.text

        # saubere Umgebung für exec
        local_env = {}

        temp_out = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = temp_out

        try:
            exec(code, {"__builtins__": __builtins__}, local_env)
            result = temp_out.getvalue()
        except Exception as e:
            result = f"Fehler: {e}"
        finally:
            sys.stdout = old_stdout

        self.output.text = result or "(keine Ausgabe)"
        self.show_output()

    # ------------------------------
    # SETTINGS
    # ------------------------------
    def build_config(self, config):
        config.setdefaults("fonts", {
            "editor_font": 16,
            "output_font": 16
        })

    def build_settings(self, settings):
        json_settings = """
[
    {
        "type": "numeric",
        "title": "Schriftgröße Editor",
        "section": "fonts",
        "key": "editor_font"
    },
    {
        "type": "numeric",
        "title": "Schriftgröße Ausgabe",
        "section": "fonts",
        "key": "output_font"
    }
]
"""
        settings.add_json_panel("Einstellungen", self.config, data=json_settings)

    def on_config_change(self, config, section, key, value):
        # Schriftgrößen LIVE aktualisieren
        if section == "fonts" and key == "editor_font":
            self.editor.font_size = int(value)
        if section == "fonts" and key == "output_font":
            self.output.font_size = int(value)


if __name__ == "__main__":
    BenacondaApp().run()
