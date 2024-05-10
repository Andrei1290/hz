import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def button_clicked():
    print("Кнопка была нажата")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Создаем главное окно
    window = QWidget()
    window.setWindowTitle('Пример приложения с PyQt5')
    window.setGeometry(100, 100, 400, 200)  # Установите координаты и размер окна

    # Создаем кнопку и назначаем обработчик события клика
    button = QPushButton('Нажми меня', window)
    button.clicked.connect(button_clicked)

    # Отобразить окно
    window.show()

    # Запустить приложение
    sys.exit(app.exec_())
