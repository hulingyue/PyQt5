import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        # 创建一个网格布局和设置组件之间的间距。

        grid.addWidget(title, 1, 0)  # 第一行 第一列
        grid.addWidget(titleEdit, 1, 1)  # 第一行 第二列

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)  # 第三行 第一列
        grid.addWidget(reviewEdit, 3, 1, 5, 1)  # 第三行 第二列 - 第五行 第二列

        self.setLayout(grid)  # 确定生成布局

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())