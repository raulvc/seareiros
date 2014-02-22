# -*- coding: UTF-8 -*-
from PySide import QtCore

from PySide.QtGui import QApplication, QDialog

import sys
import logging
from src.login import Login
from src.main import MainWindow


# Logging configuration for this file
logging.basicConfig(filename="seareiros.log",
                    format="""%(asctime)-s: %(name)-s - %(levelname)-s - %(module)-s - Line %(lineno)-6d \n %(message)s""")
logger = logging.getLogger(__name__)
    
def main():

    # application specifics
    app = QApplication(sys.argv)

    # login dialog
    login_dialog = Login()
    if login_dialog.exec_() == QDialog.Accepted:
        # validation complete, open main interface
        window = MainWindow(login_dialog.get_username())
        window.showMaximized()
        # solves mainwindow focusing on windows/xfce
        app.setActiveWindow(window)
        # start main loop
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()



