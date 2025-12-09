# Buildozer / Android Fix Script – README

**Datei:** `build_fix.sh`  
**Zweck:** Repariert Buildozer-/Android-SDK-Probleme unter WSL schnell und ohne erneute große Downloads.

---

## ⭐ Zweck des Scripts

Das Script behebt typische Fehler beim Android-Build:

- Falsche oder veraltete Java-Version (setzt Java 17)
- Fehlender oder falsch platzierter `sdkmanager`
- Fehlerhafte Android-SDK-Struktur
- Abstürze bei „Installing/updating SDK platform tools“
- Verhindert erneute 2–3 GB Downloads

---

## 🛠️ Installation & Ausführung

### 1. Script speichern

```bash
nano build_fix.sh
```

Inhalt einfügen → speichern.

### 2. Ausführbar machen

```bash
chmod +x build_fix.sh
```

### 3. Ausführen

```bash
bash build_fix.sh
```

---

## 📌 Wann sollte ich das Script ausführen?

Wenn Buildozer z. B. meldet:

- `sdkmanager is not installed`
- `UnsupportedClassVersionError`
- Build hängt bei SDK-Tools
- Buildozer will unnötig große Dateien erneut laden

---

## 📂 Was das Script ändert

| Bereich | Änderung |
|--------|----------|
| Java | installiert Java 17 und setzt es als Standard |
| Alte Java-Versionen | werden entfernt |
| Android SDK | korrigiert die cmdline-tools Struktur |
| sdkmanager | wird korrekt platziert & ausführbar gemacht |
| SDK-Komponenten | aktualisiert Plattform-Tools & Build-Tools |

---

## 🚀 Nach erfolgreichem Fix

Zum Projekt navigieren:

```bash
cd /mnt/c/Users/bensc/Desktop/IT/Projekte/python_ide_android
```

APK bauen:

```bash
buildozer -v android debug
```

---

## ❓ FAQ

### Wird etwas gelöscht?
Nur veraltetes Java und fehlerhafte SDK-Strukturen.

### Kann das Script mehrfach ausgeführt werden?
Ja, es ist sicher und wiederholbar.

### Warum Java 17?
Weil moderne Android Tools damit kompiliert wurden.

---

## ❤️ Hinweis
Wenn du möchtest, erstelle ich dir zusätzlich:

- ein Diagnose-Script  
- ein Clean-Script  
- eine README für dein Python-IDE-Projekt  
