[app]

title = Benaconda
package.name = benaconda
package.domain = org.bensc

source.dir = .
source.main = main.py

version = 0.1

requirements = python3,kivy==2.3.0,pygments

orientation = portrait

fullscreen = 0
titlebar = 1
source.include_exts = py,png,jpg,kv,atlas


[android]

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.bootstrap = sdl2
android.copy_libs = 1
android.enable_keyboard = 1


[buildozer]
log_level = 2
warn_on_root = 1

