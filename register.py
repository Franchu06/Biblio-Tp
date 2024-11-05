from PyQt5 import QtWidgets, QtGui, QtCore
from database import connect_db

class RegisterApp(QtWidgets.QWidget):
    def __init__(self, rol):
        super().__init__()
        self.rol = rol
        self.init_ui()

    def init_ui(self):
        self.setGeometry(680, 200, 500, 600)
        self.setWindowTitle(f'Registrarse como {self.rol.capitalize()}')
        self.setStyleSheet(open("styles.css").read())

        layout = QtWidgets.QVBoxLayout()

        self.formulario = QtWidgets.QWidget(self)
        self.formulario.setObjectName("registerForm")

        form_layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel(f'Registro de {self.rol.capitalize()}', self)
        self.label.setObjectName("header")
        form_layout.addWidget(self.label)

        self.nombre_input = QtWidgets.QLineEdit(self.formulario)
        self.nombre_input.setPlaceholderText('Nombre')
        form_layout.addWidget(self.nombre_input)

        self.apellido_input = QtWidgets.QLineEdit(self.formulario)
        self.apellido_input.setPlaceholderText('Apellido')
        form_layout.addWidget(self.apellido_input)

        self.dni_input = QtWidgets.QLineEdit(self.formulario)
        self.dni_input.setPlaceholderText('DNI')
        form_layout.addWidget(self.dni_input)

        if self.rol == 'cliente':
            self.telefono_input = QtWidgets.QLineEdit(self.formulario)
            self.telefono_input.setPlaceholderText('Teléfono')
            form_layout.addWidget(self.telefono_input)
        else:
            self.direccion_input = QtWidgets.QLineEdit(self.formulario)
            self.direccion_input.setPlaceholderText('Dirección')
            form_layout.addWidget(self.direccion_input)

        self.usuario_input = QtWidgets.QLineEdit(self.formulario)
        self.usuario_input.setPlaceholderText('Usuario')
        form_layout.addWidget(self.usuario_input)

        self.contraseña_input = QtWidgets.QLineEdit(self.formulario)
        self.contraseña_input.setPlaceholderText('Contraseña')
        self.contraseña_input.setEchoMode(QtWidgets.QLineEdit.Password)
        form_layout.addWidget(self.contraseña_input)

        self.registrar_button = QtWidgets.QPushButton('Registrar', self.formulario)
        self.registrar_button.clicked.connect(self.registrar)
        form_layout.addWidget(self.registrar_button)

        self.formulario.setLayout(form_layout)
        layout.addWidget(self.formulario)

        self.setLayout(layout)


    def registrar(self):
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        dni = self.dni_input.text()
        usuario = self.usuario_input.text()
        contraseña = self.contraseña_input.text()

        conn = connect_db()
        cursor = conn.cursor()

        if self.rol == 'cliente':
            telefono = self.telefono_input.text()
            cursor.execute("INSERT INTO clientes (nombre, apellido, dni, telefono, usuario, contraseña) VALUES (%s, %s, %s, %s, %s, %s)",
                           (nombre, apellido, dni, telefono, usuario, contraseña))
        else:
            direccion = self.direccion_input.text()
            cursor.execute("INSERT INTO empleados (nombre, apellido, dni, direccion, usuario, contraseña, tipo) VALUES (%s, %s, %s, %s, %s, %s, 'empleado')",
                           (nombre, apellido, dni, direccion, usuario, contraseña))

        conn.commit()
        QtWidgets.QMessageBox.information(self, "Éxito", "Registro exitoso")
        self.close()
