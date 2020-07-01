
from PySide2.QtWidgets import QApplication, QMainWindow
from logica_proyecto import MainWindow

if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec_()
