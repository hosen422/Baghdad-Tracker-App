[app]
title = AlMandoub
package.name = almandoub
package.domain = org.hosen422
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
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
android.archs = arm64-v8a
android.skip_apk_rescale = 1

# إعادة تفعيل السحب التلقائي الآمن للنسخة المستقرة لإنشاء المجلد المفقود
p4a.branch = release-2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
