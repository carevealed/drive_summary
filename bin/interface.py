__author__ = 'CAVPP'
#!/usr/bin/python

import sys
from PySide.QtCore import *
from PySide.QtGui import *
import time



class windowForm(QDialog):

    def __init__(self, parent=None):
        super(windowForm, self).__init__(parent)
        self.displaySummary = QTextBrowser()
        self.lineedit = QLineEdit("Here is the Summary of the drive")

        self.displaySummary.append("HAHAHAHAH")

        layout = QVBoxLayout()
        layout.addWidget(self.displaySummary)
        layout.addWidget(self.lineedit)

        self.setLayout(layout)
        self.setWindowTitle("Summary")
        pass

def main():
    # app = QApplication(sys.argv)
    #
    # label = QLabel("Hello World")
    # label.setWindowFlags(Qt.SplashScreen)
    # label.show()
    # QTimer.singleShot(10000, app.quit)
    # # time.sleep(2)
    # app.exec_()
    app = QApplication(sys.argv)
    mainWindow1 = windowForm()
    mainWindow1.show()
    app.exec_()


if __name__ == "__main__":
    main()