from PyQt5 import QtWidgets
from login import LoginApp
from register import RegisterApp

class RolSelector(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(480, 200, 800, 600)
        self.setWindowTitle('Seleccionar Rol')
        self.setStyleSheet(open("styles2.css").read())

        layout = QtWidgets.QVBoxLayout()
        
        self.formulario = QtWidgets.QWidget(self)
        self.formulario.setObjectName("background")

        self.label = QtWidgets.QLabel('Ingresar como Cliente/Empleado o Registrarse', self)
        layout.addWidget(self.label)

        self.cliente_button = QtWidgets.QPushButton('Cliente', self)
        self.cliente_button.clicked.connect(self.abrir_login_cliente)
        layout.addWidget(self.cliente_button)

        self.empleado_button = QtWidgets.QPushButton('Empleado', self)
        self.empleado_button.clicked.connect(self.abrir_login_empleado)
        layout.addWidget(self.empleado_button)

        self.registrar_button = QtWidgets.QPushButton('Registrarse como Cliente', self)
        self.registrar_button.clicked.connect(self.abrir_registro_cliente)
        layout.addWidget(self.registrar_button)

        self.setLayout(layout)

    def abrir_login_cliente(self):
        self.login_app = LoginApp(rol='cliente')
        self.login_app.show()
        self.close()

    def abrir_login_empleado(self):
        self.login_app = LoginApp(rol='empleado')
        self.login_app.show()
        self.close()

    def abrir_registro_cliente(self):
        self.register_app = RegisterApp(rol='cliente')
        self.register_app.show()
        self.close()
