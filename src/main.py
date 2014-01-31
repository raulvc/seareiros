# -*- coding: UTF-8 -*-

from PySide.QtGui import QApplication, QMessageBox

import sys
import logging

# Logging configuration for this file
from src.login import Login

logging.basicConfig(filename="seareiros.log", format="""%(asctime)-15s:
                    %(name)-18s - %(levelname)-8s - %(module)-15s - 
                    %(funcname)-20s - %(lineno)-6d - %(message)s""")
logger = logging.getLogger(name="main")
    
def main():
    # application specifics
    app = QApplication(sys.argv)

    # login dialog
    formLogin = Login()
    formLogin.show()
    
    app.exec_()

if __name__ == "__main__":
    main()



