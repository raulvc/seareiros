# -*- coding: UTF-8 -*-

from PySide.QtGui import QApplication, QDialog

import sys
import logging

# Logging configuration for this file
from src.login import Login
from src.main import MainWindow

logging.basicConfig(filename="seareiros.log", format="""%(asctime)-15s:
                    %(name)-18s - %(levelname)-8s - %(module)-15s - 
                    %(funcname)-20s - %(lineno)-6d - %(message)s""")
logger = logging.getLogger(name="main")
    
def main():
    # application specifics
    app = QApplication(sys.argv)

    # login dialog
    if Login().exec_() == QDialog.Accepted:
        # validation complete, open main interface
        window = MainWindow()
        window.showMaximized()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()



