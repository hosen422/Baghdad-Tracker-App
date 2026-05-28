[app]
title = AlMandoub
package.name = almandoub
package.domain = org.hosen422
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# المتطلبات الصافية والمستقرة
requirements = python3,kivy==2.3.0,plyer

orientation = portrait
fullscreen = 0

# تقييد المترجم على حزم مستقرة تمنع استهلاك ذاكرة السيرفر
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a

[buildozer]
# تحويل السجلات إلى مستودع صامت لمنع طرد السيرفر للمهمة
log_level = 1
warn_on_root = 1
