[app]
title = Al-Wassel Pro
package.name = alwasselpro
package.domain = org.alwassel
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# المتطلبات بناءً على كودك (أضفت sqlite3 وفتح الروابط)
requirements = python3, kivy==2.1.0, kivymd==1.1.1, pillow, sqlite3

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0

# ضروري جداً لتطبيقك لكي يرسل رسائل SMS
android.permissions = INTERNET, SEND_SMS

# دعم المعالجات
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
