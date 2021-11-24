import sys
from 数独 import ui
from PyQt5.QtWidgets import QApplication, QDialog


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建QApplication类的实例
    mainWindow = QDialog()
    myUI = ui.Ui_Dialog()
    myUI.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())  # 进入程序的主循环、并通过exit函数确保主循环安全结束
