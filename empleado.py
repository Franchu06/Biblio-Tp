from PyQt5 import QtWidgets
from database import connect_db
from register import RegisterApp

class EmpleadoApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(680, 200, 630, 700)
        self.setWindowTitle('Gestión de Empleados y Libros')
        self.setStyleSheet(open("styles.css").read())

        layout = QtWidgets.QVBoxLayout()

        self.gestion_label = QtWidgets.QLabel('Gestión de Empleados y Libros', self)
        self.gestion_label.setObjectName("header")
        layout.addWidget(self.gestion_label)

        self.agregar_empleado_button = QtWidgets.QPushButton('Agregar Empleado', self)
        self.agregar_empleado_button.clicked.connect(self.agregar_empleado)
        layout.addWidget(self.agregar_empleado_button)

        self.eliminar_empleado_button = QtWidgets.QPushButton('Eliminar Empleado', self)
        self.eliminar_empleado_button.clicked.connect(self.mostrar_formulario_eliminar_empleado)
        layout.addWidget(self.eliminar_empleado_button)

        self.agregar_libro_button = QtWidgets.QPushButton('Agregar Libro', self)
        self.agregar_libro_button.clicked.connect(self.mostrar_formulario_libro)
        layout.addWidget(self.agregar_libro_button)

        self.actualizar_libro_button = QtWidgets.QPushButton('Actualizar Libro', self)
        self.actualizar_libro_button.clicked.connect(self.mostrar_formulario_actualizar_libro)
        layout.addWidget(self.actualizar_libro_button)

        self.eliminar_libro_button = QtWidgets.QPushButton('Eliminar Libro', self)
        self.eliminar_libro_button.clicked.connect(self.mostrar_formulario_eliminar_libro)
        layout.addWidget(self.eliminar_libro_button)
        
        self.setLayout(layout)
    
    def agregar_empleado(self):
        self.register_app = RegisterApp(rol='empleado')
        self.register_app.show()

    def mostrar_formulario_eliminar_empleado(self):
        self.formulario_eliminar_empleado = QtWidgets.QWidget()
        self.formulario_eliminar_empleado.setWindowTitle('Eliminar Empleado')
        self.formulario_eliminar_empleado.setGeometry(100, 100, 400, 200)
        self.formulario_eliminar_empleado.setStyleSheet(open("styles.css").read())

        layout = QtWidgets.QVBoxLayout()

        self.usuario_eliminar_input = QtWidgets.QLineEdit(self.formulario_eliminar_empleado)
        self.usuario_eliminar_input.setPlaceholderText('Usuario del Empleado')
        layout.addWidget(self.usuario_eliminar_input)

        self.eliminar_button = QtWidgets.QPushButton('Eliminar', self.formulario_eliminar_empleado)
        self.eliminar_button.clicked.connect(self.eliminar_empleado)
        layout.addWidget(self.eliminar_button)

        self.formulario_eliminar_empleado.setLayout(layout)
        self.formulario_eliminar_empleado.show()

    def eliminar_empleado(self):
        usuario = self.usuario_eliminar_input.text()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM empleados WHERE usuario=%s", (usuario,))
        conn.commit()

        QtWidgets.QMessageBox.information(self, "Éxito", "Empleado eliminado exitosamente")
        self.formulario_eliminar_empleado.close()

    def mostrar_formulario_libro(self):
        self.formulario_libro = QtWidgets.QWidget()
        self.formulario_libro.setWindowTitle('Agregar Nuevo Libro')
        self.formulario_libro.setGeometry(100, 100, 400, 300)
        self.formulario_libro.setStyleSheet(open("styles.css").read())

        layout = QtWidgets.QVBoxLayout()

        self.nombre_input = QtWidgets.QLineEdit(self.formulario_libro)
        self.nombre_input.setPlaceholderText('Nombre del Libro')
        layout.addWidget(self.nombre_input)

        self.autor_input = QtWidgets.QLineEdit(self.formulario_libro)
        self.autor_input.setPlaceholderText('Autor')
        layout.addWidget(self.autor_input)

        self.categoria_input = QtWidgets.QLineEdit(self.formulario_libro)
        self.categoria_input.setPlaceholderText('Categoría')
        layout.addWidget(self.categoria_input)

        self.agregar_button = QtWidgets.QPushButton('Agregar', self.formulario_libro)
        self.agregar_button.clicked.connect(self.agregar_libro)
        layout.addWidget(self.agregar_button)

        self.formulario_libro.setLayout(layout)
        self.formulario_libro.show()

    def agregar_libro(self):
        nombre = self.nombre_input.text()
        autor = self.autor_input.text()
        categoria = self.categoria_input.text()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO libros (nombre, autor, categoria) VALUES (%s, %s, %s)", 
                       (nombre, autor, categoria))
        conn.commit()
        
        QtWidgets.QMessageBox.information(self, "Éxito", "Libro agregado exitosamente")
        self.formulario_libro.close()

    def mostrar_formulario_actualizar_libro(self):
        self.formulario_actualizar_libro = QtWidgets.QWidget()
        self.formulario_actualizar_libro.setWindowTitle('Actualizar Libro')
        self.formulario_actualizar_libro.setGeometry(100, 100, 400, 300)
        self.formulario_actualizar_libro.setStyleSheet(open("styles.css").read())

        layout = QtWidgets.QVBoxLayout()

        self.id_input = QtWidgets.QLineEdit(self.formulario_actualizar_libro)
        self.id_input.setPlaceholderText('ID del Libro')
        layout.addWidget(self.id_input)

        self.nombre_input = QtWidgets.QLineEdit(self.formulario_actualizar_libro)
        self.nombre_input.setPlaceholderText('Nuevo Nombre del Libro')
        layout.addWidget(self.nombre_input)

        self.autor_input = QtWidgets.QLineEdit(self.formulario_actualizar_libro)
        self.autor_input.setPlaceholderText('Nuevo Autor')
        layout.addWidget(self.autor_input)

        self.categoria_input = QtWidgets.QLineEdit(self.formulario_actualizar_libro)
        self.categoria_input.setPlaceholderText('Nueva Categoría')
        layout.addWidget(self.categoria_input)

        self.actualizar_button = QtWidgets.QPushButton('Actualizar', self.formulario_actualizar_libro)
        self.actualizar_button.clicked.connect(self.actualizar_libro)
        layout.addWidget(self.actualizar_button)

        self.formulario_actualizar_libro.setLayout(layout)
        self.formulario_actualizar_libro.show()

    def actualizar_libro(self):
        libro_id = self.id_input.text()
        nombre = self.nombre_input.text()
        autor = self.autor_input.text()
        categoria = self.categoria_input.text()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE libros SET nombre=%s, autor=%s, categoria=%s WHERE id=%s", 
                       (nombre, autor, categoria, libro_id))
        conn.commit()
        
        QtWidgets.QMessageBox.information(self, "Éxito", "Libro actualizado exitosamente")
        self.formulario_actualizar_libro.close()

    def mostrar_formulario_eliminar_libro(self):
        self.formulario_eliminar_libro = QtWidgets.QWidget()
        self.formulario_eliminar_libro.setWindowTitle('Eliminar Libro')
        self.formulario_eliminar_libro.setGeometry(100, 100, 400, 200)
        self.formulario_eliminar_libro.setStyleSheet(open("styles.css").read())

        layout = QtWidgets.QVBoxLayout()

        self.id_input = QtWidgets.QLineEdit(self.formulario_eliminar_libro)
        self.id_input.setPlaceholderText('ID del Libro')
        layout.addWidget(self.id_input)

        self.eliminar_button = QtWidgets.QPushButton('Eliminar', self.formulario_eliminar_libro)
        self.eliminar_button.clicked.connect(self.eliminar_libro)
        layout.addWidget(self.eliminar_button)

        self.formulario_eliminar_libro.setLayout(layout)
        self.formulario_eliminar_libro.show()

    def eliminar_libro(self):
        libro_id = self.id_input.text()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM libros WHERE id=%s", (libro_id,))
        conn.commit()
        
        QtWidgets.QMessageBox.information(self, "Éxito", "Libro eliminado exitosamente")
        self.formulario_eliminar_libro.close()
