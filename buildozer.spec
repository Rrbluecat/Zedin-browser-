[app]
title = Zedin Browser
package.name = zedinbrowser
package.domain = com.rrbluecat
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.1.0,android
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
