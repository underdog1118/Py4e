'''
Writer:UNDERDOG
Time:..
'''
import sys
import untitled
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == __main__:
    app = QApplication(sys.argv)
    maiwindow = QMainWindow()
    ui = untitled.Ui_MainWindow()
    #ui.setupUi(maiwindow)
    maiwindow.show()
    sys.exit(app.exec_())