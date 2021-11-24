import sys
import test
import ui
from PyQt5.QtWidgets import QApplication, QDialog


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建QApplication类的实例
    mainWindow = QDialog()
    ui = ui.Ui_Dialog()
    ui.setupUi(mainWindow)
    mainWindow.show()
    print(ui.init_arr())
    test.Solve.solve(ui.init_arr())
    sys.exit(app.exec_())  # 进入程序的主循环、并通过exit函数确保主循环安全结束
