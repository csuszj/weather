from Uiweather import Ui_Form
from PyQt5 import QtWidgets
import sys

class myui_form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(myui_form,self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = myui_form()
    ui.show()
    sys.exit(app.exec_())