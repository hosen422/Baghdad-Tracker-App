[app]
title = AlMandoub
package.name = almandoub
package.domain = org.hosen422

# تأكد أن ملفك الرئيسي في المجلد اسمه main.py تماماً
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 0.1
requirements = python3,kivy==2.3.0,plyer,hostpython3==3.11.11

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-ndk
android.build_tools_version = 33.0.1
android.ndk_api = 21

# تعديل هام: دعم المعماريات الشهيرة لمنع خطأ التطبيق ليس مثبتاً
android.archs = arm64-v8a, armeabi-v7a

android.skip_apk_rescale = 1
p4a.branch = release-2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
