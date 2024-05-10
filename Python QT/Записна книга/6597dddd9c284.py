from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from json import *

app = QApplication([])


window = QWidget()
window.setWindowTitle("Телефонний довідник")
window.resize(900, 600)

h=QHBoxLayout()
v1=QVBoxLayout()
v2=QVBoxLayout()

label1=QLabel("Добавити пользователя")
label2=QLabel("Знайти пользователя")

q1=QLineEdit()
text1=QTextEdit()
b1=QPushButton("Додати")

q2=QComboBox()
text2=QTextEdit()
text2.setReadOnly(True)
b2=QPushButton("Показати")


v1.addWidget(label1)
v1.addWidget(q1)
v1.addWidget(text1)
v1.addWidget(b1)

v2.addWidget(label2)
v2.addWidget(q2)
v2.addWidget(text2)
v2.addWidget(b2)

h.addLayout(v1)
h.addLayout(v2)
window.setLayout(h)

tlist={"name":"0000"}






def plus():
    name=q1.text()
    q2.addItem(name)
    info=text1.toPlainText()
    tlist[name]=info
    with open("phones.json", "w") as file:
        dump(tlist, file)
    print(tlist)

b1.clicked.connect(plus)

def search():
    a=q2.currentIndex()
    print(a)
    text2.setPlainText(tlist[q2.itemText(a)])

b2.clicked.connect(search)

with open("phones.json", "r") as file:
    tlist=load(file)
    for name in tlist:
        q2.addItem(name)


window.show()
app.exec_()
