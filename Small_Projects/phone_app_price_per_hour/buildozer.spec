[app]

# (str) Title of your application
title = Цена на час

# (str) Package name
package.name = price_per_hour_phone

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (str) Source code filename
source.include_exts = py

# (str) Application versioning (method 1)
version = 0.1

# (int) Android API to use
osx.python_version = 3

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 28

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 28

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching.
# android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# android.add_src = src

# (list) Android AAR archives to add (currently works only with sdl2_gradle
# bootstrap)
# android.add_aars = foo.aar

# (list) Gradle dependencies to add (currently works only with sdl2_gradle
# bootstrap)
# android.gradle_dependencies = some.package:some.thing, another.package:another.thing

# (list) Packaging options. You can specify custom parameters to add to the
# android, ios and other (for other platform) packaging. See:
# https://python-for-android.readthedocs.io/en/latest/toolchain/#packaging-options
# for options
# android.p4a_add_custom_prm = mycustomprm=mycustomvalue

# (str) Android entry point
android.entrypoint = task_app.py

# (str) iOS entry point
# ios.entrypoint =

# (list) List of .so files to add to the libs (android)
# android.add_libs_armeabi = libs/armeabi/libexample.so
# android.add_libs_arm64_v8a = libs/arm64-v8a/libexample.so
# android.add_libs_x86 = libs/x86/libexample.so
# android.add_libs_x86_64 = libs/x86_64/libexample.so

# (str) iOS framework dirs (space separated list)
# ios.frameworks =

# (str) iOS extra plist entries
# ios.plist =

# (list) Excluded files and folders (like the .git folder)
# exclude-files = README.md, .gitignore, .git/**

# (list) List of exclusions using pattern matching
# exclude_dirs = tests, bin, .git, venv, assets/**

# (str) Application icon (.png or .jpg)
icon.filename = icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) Kivy version to use
# kivy_version = 1.11.1

# (str) iOS SDK to use
# ios.sdk = 10.0

# (str) Android NDK version to use
# android.ndk = 17c

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path =

# (str) Android entry point (app instead of gui)
# android.entrypoint = app

# (str) Android app theme, default one is the Kivy version
# android.app_theme = "@android:style/Theme.NoTitleBar"

# (str) Android app description
# android.description = Your description

# (str) Android key store password
# android.keystore.password = mypassword

# (str) Android key alias
# android.keystore.alias = mykey

# (str) Android key store for release
# android.keystore = mykeystore.keystore

# (str) Android key store type (default JKS)
# android.keystore.type = jks

# (str) Android key store alias (default keyalias)
# android.keystore.alias = keyalias

# (str) Android key store alias password (default same as keystore password)
# android.keystore.alias_password = mypassword

# (bool) Use the Ren'Py android project
# android.renpy = False
