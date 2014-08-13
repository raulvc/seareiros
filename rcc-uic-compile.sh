#!/bin/bash
pyside-rcc res/icons.qrc -o src/lib/ui/icons_rc.py
pyside-uic src/lib/ui/login.ui -o src/lib/ui/ui_login.py
pyside-uic src/lib/ui/main.ui -o src/lib/ui/ui_main.py
pyside-uic src/lib/ui/form_activity.ui -o src/lib/ui/ui_form_activity.py
pyside-uic src/lib/ui/form_associate.ui -o src/lib/ui/ui_form_associate.py
pyside-uic src/lib/ui/form_book.ui -o src/lib/ui/ui_form_book.py
pyside-uic src/lib/ui/oform_product.ui -o src/lib/ui/ui_oform_product.py
pyside-uic src/lib/ui/generic_dock.ui -o src/lib/ui/ui_generic_dock.py
pyside-uic src/lib/ui/generic_search.ui -o src/lib/ui/ui_generic_search.py
pyside-uic src/lib/ui/generic_select.ui -o src/lib/ui/ui_generic_select.py
pyside-uic src/lib/ui/overview.ui -o src/lib/ui/ui_overview.py
pyside-uic src/lib/ui/pendencies.ui -o src/lib/ui/ui_pendencies.py
pyside-uic src/lib/ui/loading.ui -o src/lib/ui/ui_loading.py
