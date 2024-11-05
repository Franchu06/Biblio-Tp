from PyQt5 import QtWidgets, QtGui, QtCore
from database import connect_db

class ClienteApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(480, 200, 1000, 600)
        self.setWindowTitle('Catálogo de Libros')
        self.setStyleSheet(open("styles.css").read())

        layout = QtWidgets.QVBoxLayout()

        self.catalogo_label = QtWidgets.QLabel('Catálogo de Libros', self) 
        self.catalogo_label.setObjectName("catalogoLabel") 
        layout.addWidget(self.catalogo_label)

        self.buscar_input = QtWidgets.QLineEdit(self)
        self.buscar_input.setPlaceholderText('Buscar libros...')
        layout.addWidget(self.buscar_input)

        self.buscar_button = QtWidgets.QPushButton('Buscar', self)
        self.buscar_button.clicked.connect(self.buscar_libro)
        layout.addWidget(self.buscar_button)

        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        layout.addWidget(self.scroll_area)

        self.catalogo_widget = QtWidgets.QWidget()
        self.catalogo_layout = QtWidgets.QGridLayout(self.catalogo_widget)
        self.catalogo_layout.setContentsMargins(0, 0, 0, 0)
        self.catalogo_layout.setSpacing(5)
        self.scroll_area.setWidget(self.catalogo_widget)

        self.setLayout(layout)

        self.mostrar_catalogo()

    def mostrar_catalogo(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, autor, categoria FROM libros")
        libros = cursor.fetchall()

        for i in reversed(range(self.catalogo_layout.count())):
            self.catalogo_layout.itemAt(i).widget().setParent(None)

        for libro in libros:
            libro_card = self.crear_libro_card(libro)
            self.catalogo_layout.addWidget(libro_card)

    def crear_libro_card(self, libro):
        card = QtWidgets.QWidget()
        card.setObjectName("libro-card")
        card_layout = QtWidgets.QVBoxLayout(card)

        nombre_label = QtWidgets.QLabel(libro[0])
        nombre_label.setStyleSheet("font-size: 25px; color: #007BFF; margin-bottom: 8px; border-color: black;")
        card_layout.addWidget(nombre_label)

        autor_label = QtWidgets.QLabel(f"Autor: {libro[1]}")
        autor_label.setStyleSheet("margin-bottom: 4px;")
        card_layout.addWidget(autor_label)

        categoria_label = QtWidgets.QLabel(f"Categoría: {libro[2]}")
        card_layout.addWidget(categoria_label)

        return card

    def buscar_libro(self):
        termino = self.buscar_input.text().lower()
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, autor, categoria FROM libros WHERE LOWER(nombre) LIKE %s OR LOWER(autor) LIKE %s OR LOWER(categoria) LIKE %s", 
                       (f'%{termino}%', f'%{termino}%', f'%{termino}%'))
        libros = cursor.fetchall()

        for i in reversed(range(self.catalogo_layout.count())):
            self.catalogo_layout.itemAt(i).widget().setParent(None)

        for libro in libros:
            libro_card = self.crear_libro_card(libro)
            self.catalogo_layout.addWidget(libro_card)
