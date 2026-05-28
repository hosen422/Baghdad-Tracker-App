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

# إجبار التوجيه المباشر والمنع الصارم لأي عملية تخمين
android.api = 33
android.minapi = 21
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-ndk
android.build_tools_version = 33.0.1
android.ndk_api = 21
android.archs = arm64-v8a

# قفل الأداة على التثبيت المحلي الخاص بـ pip لمنع قفز الإصدارات
p4a.source_dir = 

[buildozer]
log_level = 1
warn_on_root = 1
