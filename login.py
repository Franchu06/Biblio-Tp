from PyQt5 import QtWidgets
from database import connect_db
from cliente import ClienteApp
from empleado import EmpleadoApp

class LoginApp(QtWidgets.QWidget):
    def __init__(self, rol):
        super().__init__()
        self.rol = rol
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(680, 200, 400, 300)
        self.setWindowTitle(f'Login - {self.rol.capitalize()}')
        self.setStyleSheet(open("styles.css").read())

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel(f'Login - {self.rol.capitalize()}', self)
        self.label.setObjectName("header")
        layout.addWidget(self.label)

        self.user_input = QtWidgets.QLineEdit(self)
        self.user_input.setPlaceholderText('Usuario')
        layout.addWidget(self.user_input)
        
        self.pass_input = QtWidgets.QLineEdit(self)
        self.pass_input.setPlaceholderText('Contraseña')
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        layout.addWidget(self.pass_input)
        
        self.login_button = QtWidgets.QPushButton('Ingresar', self)
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)

    def abrir_pantalla_completa(self):
        self.showFullScreen()


    def login(self):
        usuario = self.user_input.text()
        contraseña = self.pass_input.text()

        conn = connect_db()
        cursor = conn.cursor()

        if self.rol == 'empleado':
            cursor.execute("SELECT * FROM empleados WHERE usuario=%s AND contraseña=%s AND tipo='empleado'", (usuario, contraseña))
        elif self.rol == 'cliente':
            cursor.execute("SELECT * FROM clientes WHERE usuario=%s AND contraseña=%s", (usuario, contraseña))
        
        resultado = cursor.fetchone()

        if resultado:
            if self.rol == 'empleado' and resultado[7] == 'empleado':
                self.empleado_panel()
            elif self.rol == 'cliente':
                self.cliente_panel()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Rol incorrecto seleccionado.")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Usuario o contraseña incorrecta")

    def empleado_panel(self):
        self.empleado_app = EmpleadoApp()
        self.empleado_app.show()
        self.close()

    def cliente_panel(self):
        self.cliente_app = ClienteApp()
        self.cliente_app.show()
        self.close()
