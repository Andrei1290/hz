from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

app.setStyleSheet('''QWidget
                  {background:green;
                    font-size: 20pt;
                    colour:green;}
                    QLineEdit { color: white }
                    QPushButton { background: lightgreen } ''')

cl = QWidget()
cl.setWindowTitle("Calculator")
cl.resize(350, 400)


plotEdit = QLineEdit()

#Вторая строка
bC = QPushButton("C")
bR = QPushButton("=")

#Третья строка
b1 = QPushButton("1")
b2 = QPushButton("2")
b3 = QPushButton("3")
bPlus = QPushButton("+")

#Четвёртая строка
b4 = QPushButton("4")
b5 = QPushButton("5")
b6 = QPushButton("6")
bMinus = QPushButton("-")

#Пятая строка
b7 = QPushButton("7")
b8 = QPushButton("8")
b9 = QPushButton("9")
bMnog = QPushButton("*")

#Шестая строка
bPR = QPushButton("%")
b0 = QPushButton("0")
bToch = QPushButton(".")
bDil = QPushButton("/")

line1=QHBoxLayout()
line1.addWidget(plotEdit)

line2=QHBoxLayout()
line2.addWidget(bC)
line2.addWidget(bR)

line3=QHBoxLayout()
line3.addWidget(b1)
line3.addWidget(b2)
line3.addWidget(b3)
line3.addWidget(bPlus)

line4=QHBoxLayout()
line4.addWidget(b4)
line4.addWidget(b5)
line4.addWidget(b6)
line4.addWidget(bMinus)

line5=QHBoxLayout()
line5.addWidget(b7)
line5.addWidget(b8)
line5.addWidget(b9)
line5.addWidget(bMnog)

line6=QHBoxLayout()
line6.addWidget(bPR)
line6.addWidget(b0)
line6.addWidget(bToch)
line6.addWidget(bDil)

line0=QVBoxLayout()
line0.addLayout(line1)
line0.addLayout(line2)
line0.addLayout(line3)
line0.addLayout(line4)
line0.addLayout(line5)
line0.addLayout(line6)

cl.setLayout(line0)

#Вторая Строка
def b1_click():
    plotEdit.insert("1")
    plotEdit.setAlignment(Qt.AlignRight)
b1.clicked.connect(b1_click)

def b2_click():
    plotEdit.insert("2")
    plotEdit.setAlignment(Qt.AlignRight)
b2.clicked.connect(b2_click)

def b3_click():
    plotEdit.insert("3")
    plotEdit.setAlignment(Qt.AlignRight)
b3.clicked.connect(b3_click)

def b4_click():
    plotEdit.insert("4")
    plotEdit.setAlignment(Qt.AlignRight)
b4.clicked.connect(b4_click)

def b5_click():
    plotEdit.insert("5")
    plotEdit.setAlignment(Qt.AlignRight)
b5.clicked.connect(b5_click)

def b6_click():
    plotEdit.insert("6")
    plotEdit.setAlignment(Qt.AlignRight)
b6.clicked.connect(b6_click)

def b7_click():
    plotEdit.insert("7")
    plotEdit.setAlignment(Qt.AlignRight)
b7.clicked.connect(b7_click)

def b8_click():
    plotEdit.insert("8")
    plotEdit.setAlignment(Qt.AlignRight)
b8.clicked.connect(b8_click)

def b9_click():
    plotEdit.insert("9")
    plotEdit.setAlignment(Qt.AlignRight)
b9.clicked.connect(b9_click)

def b0_click():
    plotEdit.insert("0")
    plotEdit.setAlignment(Qt.AlignRight)
b0.clicked.connect(b0_click)

def bToch_click():
    plotEdit.insert(".")
    plotEdit.setAlignment(Qt.AlignRight)
bToch.clicked.connect(bToch_click)

def bC_click():
    plotEdit.setText("")
bC.clicked.connect(bC_click)



def bPlus_click():
    global a,b
    a=float(plotEdit.text())
    b="+"
    plotEdit.setText("")
bPlus.clicked.connect(bPlus_click)

def bMinus_click():
    global a,b
    a=float(plotEdit.text())
    b="-"
    plotEdit.setText("")
bMinus.clicked.connect(bMinus_click)

def bMnog_click():
    global a,b
    a=float(plotEdit.text())
    b="*"
    plotEdit.setText("")
bMnog.clicked.connect(bMnog_click)

def bDil_click():
    global a,b
    a=float(plotEdit.text())
    b="/"
    plotEdit.setText("")
bDil.clicked.connect(bDil_click)

def bPR_click():
    global a,b
    a=float(plotEdit.text())
    b="%"
    plotEdit.setText("")
bPR.clicked.connect(bPR_click)



def bR_click():
    global a,b,c
    c=float(plotEdit.text())
    plotEdit.setText("")
    if b=="+":
        plotEdit.setText(str(a+c))
    if b=="-":
        plotEdit.setText(str(a-c))
    if b=="*":
        plotEdit.setText(str(a*c))
    if b=="/":
        plotEdit.setText(str(a/c))
    if b=="%":
        plotEdit.setText(str(a%c))
bR.clicked.connect(bR_click)

cl.show()
app.exec_()