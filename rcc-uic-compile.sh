#!/bin/bash
pyside-rcc res/icons.qrc -o src/lib/ui/icons_rc.py
pyside-uic src/lib/ui/login.ui -o src/lib/ui/ui_login.py
pyside-uic src/lib/ui/main.ui -o src/lib/ui/ui_main.py
