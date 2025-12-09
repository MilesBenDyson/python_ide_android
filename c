[app]

# (str) Title of your application
title = Benaconda

# (str) Package name
package.name = benaconda

# (str) Package domain (needed for android/ios packaging)
package.domain = org.bensc

# (str) Source code where the main.py live
source.dir = .
source.main = main.py

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
# source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude
# source.exclude_exts = spec

# (list) List of directory to exclude
# source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py


# ---------------------------------------------------------
# (list) Application requirements (THE MOST IMPORTANT PART)
# ---------------------------------------------------------
requirements = python3==3.10,kivy==2.3.0,pygments

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientations
orientation = portrait

# (bool) Display the application name as title in the titlebar
titlebar = 1

# (bool) Fullscreen mode
fullscreen = 0

# (str) Source code encoding
source.encoding = utf-8


#
# ANDROID SECTION
#

[android]

# (str) Target Android API
android.api = 33

# (int) Minimum API your app will support
android.minapi = 24

# (str) Android NDK version
android.ndk = 25b

# (list) Supported architectures
android.archs = arm64-v8a

# (str) The bootstrap to use (only sdl2 for kivy)
android.bootstrap = sdl2

# (bool) Copy library instead of building recipes separately
android.copy_libs = 1

# (str) Gradle version (auto)
# android.gradle_version = 7.5

# (str) Android SDK directory (auto)
# android.sdk_path = ~/.buildozer/android/platform/android-sdk

# (str) NDK directory (auto)
# android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b

# (str) Presplash color (background)
# android.presplash_color = #FFFFFF

# (bool) Enable keyboard mode
android.enable_keyboard = 1

# (str) Additional Java jars to add
# android.add_jars = libs/some.jar

# (str) Add custom Java source folders
# android.add_src = src/java

# (str) Add Android manifest overrides
# android.manifest_placeholders = 


#
# IOS SECTION (unused)
#
[ios]
# ios.kivy_ios_dir = ../kivy-ios
# ios.project_dir = .


#
# BUILD SECTION
#
[buildozer]
log_level = 2
warn_on_root = 1

nano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7anano buildozer.spec
2. Diese Zeile finden:
ini
Code kopieren
archs = arm64-v8a, armeabi-v7a
oder manchmal:

ini
Code kopieren
# (str) The ARCHs of buildozer
arch = arm64-v8a, armeabi-v7a
