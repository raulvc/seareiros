#!/bin/bash
pyside-rcc res/icons.qrc -o src/lib/ui/icons_rc.py
pyside-uic src/lib/ui/login.ui -o src/lib/ui/ui_login.py
pyside-uic src/lib/ui/main.ui -o src/lib/ui/ui_main.py
pyside-uic src/lib/ui/add_associate.ui -o src/lib/ui/ui_add_associate.py
pyside-uic src/lib/ui/add_book.ui -o src/lib/ui/ui_add_book.py
pyside-uic src/lib/ui/overview.ui -o src/lib/ui/ui_overview.py
