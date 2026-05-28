[app]
title = AlMandoub
package.name = almandoub
package.domain = org.hosen422
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy==2.3.0,plyer

orientation = portrait
fullscreen = 0

# قفل التحديثات بالكامل ليتطابق مع الـ SDK الممرر في ملف الـ YAML
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.1
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
p4a.branch = master

[buildozer]
log_level = 1
warn_on_root = 1
