"""
QCheckBox复选框控件，它有两个状态:打开和关闭，他是一个带有文本标签（Label）的控件。复选框常用于表示程序中可以启用或禁用的功能。
"""
import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.cb = QCheckBox('Show title', self)
        self.cb.move(20, 20)
        self.cb.toggle()
        # 我们有设置窗口标题, 所以我们也必须检查复选框。默认情况下, 没有设置窗口标题和也没有勾选复选框。
        self.cb.stateChanged.connect(self.changeTitle)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(100, 100)

        redb.clicked[bool].connect(self.clickEvent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')

    def clickEvent(self):
        source = self.sender()

        if source.text() == "Red":
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')
        self.cb.toggle()
        # 在除了CheckBox之外的地方修改CheckBox值，更新UI


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

