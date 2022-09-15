'''
Writer:UNDERDOG
Time:..
'''
import sys

from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10)) # 提示框字体
        self.setToolTip('IS <b>QWidget</b> widget') # 创建提示框
        b = QPushButton('button',self) # 创建按钮
        b.setToolTip('is <b>QWidget</b> widget') # 创建按钮的提示框
        b.resize(b.sizeHint()) # 使用推荐的大小
        b.move(50,50)

        # 退出按钮
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(400, 50)

        # 主窗口
        self.center()  # 或自定义 self.setGeometry(1000,500, 500, 400)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('./img/title.ico'))
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 主窗口矩形
        cp = QDesktopWidget().availableGeometry().center()  # 显示器绝对值，屏幕中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):    # 重写点X关闭的方法
        reply = QMessageBox.question(self, 'Message!',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
