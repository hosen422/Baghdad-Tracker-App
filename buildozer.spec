[app]
title = AlMandoub
package.name = almandoub
package.domain = org.hosen422
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# المتطلبات الأساسية الصافية
requirements = python3,kivy==2.3.0,plyer

orientation = portrait
fullscreen = 0

# قفل التحديثات التلقائية العشوائية للسيرفر
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a

# السطر السحري لمنع انهيار الـ Bootstrap الخاص بـ SDL2
p4a.branch = master

[buildozer]
log_level = 1
warn_on_root = 1
