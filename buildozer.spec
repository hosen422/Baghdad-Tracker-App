[app]
title = AlMandoub
package.name = almandoub
package.domain = org.hosen422
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# المتطلبات النظيفة بدون إصدار بايثون فرعي يسبب قفل السيرفر
requirements = python3,kivy==2.3.0,plyer

orientation = portrait
fullscreen = 0

# إعدادات الأندرويد المستقرة
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a
android.skip_apk_rescale = 1

[buildozer]
log_level = 2
warn_on_root = 1
