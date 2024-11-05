from PyQt5 import QtWidgets
from rol_selector import RolSelector

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    rol_selector_app = RolSelector()
    rol_selector_app.show()
    app.exec_()