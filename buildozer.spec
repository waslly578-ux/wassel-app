[app]
title = Al-Wassel
package.name = alwassel
package.domain = org.alwassel
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# المتطلبات الأساسية لتطبيقك (معدلة بدقة)
requirements = python3, kivy==2.1.0, kivymd==1.1.1, pillow, requests, urllib3

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0

# دعم المعالجات الحديثة
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# أيقونة التطبيق
icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
