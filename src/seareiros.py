# -*- coding: UTF-8 -*-

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
    if Login().exec_() == QDialog.Accepted:
        # validation complete, open main interface
        window = MainWindow()
        window.showMaximized()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()



