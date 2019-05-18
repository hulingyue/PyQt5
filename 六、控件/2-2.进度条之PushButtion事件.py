import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.CountBtn = QPushButton('计数Button', self)
        self.CountBtn.move(100, 100)
        self.CountBtn.clicked.connect(self.clickEvent)
        self.count = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def clickEvent(self):
        self.count = self.count + 1
        self.pbar.setValue(self.count)
        # 更新进度条


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())