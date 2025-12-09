
# 🐍 Benaconda – Python IDE für Android (Kivy + Buildozer + WSL2)

Ein vollständiges Tutorial, wie man unter **Windows** mit **WSL2** und **Buildozer** eine Android-App aus Python baut.

---

## 📌 Über das Projekt

Benaconda ist eine einfache, mobile Python-IDE für Android.  
Der Editor läuft in Kivy und kann Python-Code direkt auf dem Gerät ausführen.

Features:

- Eingabefeld für Python-Code  
- Ausgabefenster (verschwindet per Touch oder ESC)  
- Schriftgröße einstellbar  
- Mintgrünes UI  
- Bluetooth-Maus + Bluetooth-Tastatur kompatibel  
- Läuft komplett offline  
- Baubar als APK für Android

---

# 🚀 Wie man unter Windows + WSL2 eine Android-App mit Buildozer baut

Dieses Tutorial beschreibt Schritt für Schritt den funktionierenden Weg — inklusive aller Stolperfallen.

---

# 1️⃣ Voraussetzungen

### Auf Windows installieren:
- Windows 10/11  
- WSL2 aktiviert  
- Ubuntu aus dem Microsoft Store  

### In Ubuntu installieren:
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
sudo apt install -y openjdk-17-jdk unzip zip
```

---

# 2️⃣ Wichtig: Projekt NICHT auf /mnt/c bauen!

Buildozer funktioniert nicht zuverlässig auf Windows-Dateisystemen.

Typische Fehler:

- sdkmanager not found  
- Symlink-Probleme  
- Gradle-Build hängt  
- python-for-android findet Dateien nicht  

👉 **Lösung:** Projekt ins Linux-Dateisystem kopieren:

```bash
cp -r /mnt/c/Users/<USERNAME>/Desktop/IT/Projekte/python_ide_android ~/python_ide_android
cd ~/python_ide_android
```

---

# 3️⃣ Virtuelle Umgebung (optional)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 4️⃣ Buildozer installieren

```bash
pip install buildozer
pip install cython
```

---

# 5️⃣ Buildozer initialisieren

```bash
buildozer init
```

Dies erzeugt die Datei `buildozer.spec`.

---

# 6️⃣ Android SDK/NDK installieren

```bash
buildozer android debug
```

Buildozer lädt automatisch:

- Android SDK  
- Android NDK  
- Gradle  
- python-for-android  

Falls `sdkmanager` nicht gefunden wird → siehe nächsten Abschnitt.

---

# 7️⃣ Fehlerfix: sdkmanager nicht gefunden

**Symptom:**
```
sdkmanager path ".../android-sdk/tools/bin/sdkmanager" does not exist
```

**Ursache:**  
Neue Android SDKs besitzen kein `/tools/`-Verzeichnis mehr.

**Fix:**

```bash
mkdir -p ~/.buildozer/android/platform/android-sdk/tools/bin
ln -s ~/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/sdkmanager ~/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager
ln -s ~/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/avdmanager ~/.buildozer/android/platform/android-sdk/tools/bin/avdmanager
```

Danach:

```bash
buildozer android debug
```

---

# 8️⃣ Build starten

```bash
cd ~/python_ide_android
buildozer android debug
```

Das Ergebnis liegt dann in:

```
~/python_ide_android/bin/benaconda-0.1-arm64-v8a_armeabi-v7a-debug.apk
```

---

# 9️⃣ GitHub Upload (WSL + SSH)

```bash
cd ~/python_ide_android
git init
```

`.gitignore` erstellen:

```
.buildozer/
.venv/
bin/
__pycache__/
*.apk
```

Dann:

```bash
git add .
git commit -m "Initial Benaconda IDE commit"
```

SSH-Key erzeugen:

```bash
ssh-keygen -t ed25519 -C "you@example.com"
cat ~/.ssh/id_ed25519.pub
```

Den Key bei GitHub einfügen:  
**GitHub → Settings → SSH and GPG keys → New SSH key**

Dann:

```bash
git remote add origin git@github.com:MilesBenDyson/python_ide_android.git
git branch -M main
git push -u origin main
```

---

# 🔟 Ordnerstruktur

```
python_ide_android/
│
├── main.py
├── buildozer.spec
├── benaconda.png
├── README.md
├── build_fix_setup.sh
│
├── .gitignore
├── .git/
│
└── (automatisch ignoriert)
    ├── .buildozer/
    ├── .venv/
    ├── bin/
```

---

# 🧪 APK installieren

```bash
adb install benaconda-0.1-arm64-v8a_armeabi-v7a-debug.apk
```

oder manuell aufs Android-Gerät kopieren.

---

# 🎉 Fertig!

Du hast jetzt ein vollständiges Build-System, um:

- Python-Apps zu erstellen  
- APKs zu bauen  
- Fehler zu vermeiden  
- dein Projekt über GitHub zu verwalten  

Viel Spaß mit **Benaconda** 🐍🔥
