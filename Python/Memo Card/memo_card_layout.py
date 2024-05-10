from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from memo_main_window import *






def show_result():
    ''' показати панель відповідей '''
    RadioGroupBox.hide()
    AnsGroupBox.show()

def show_question():
    ''' показати панель запитань '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("OK")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

layout_line1 = QHBoxLayout() # кнопки для переключения между режимами
layout_line2 = QHBoxLayout() # вопрос
layout_line3 = QHBoxLayout() # варианты ответов или результат теста
layout_line4 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1) # разрыв между кнопками делаем по возможности длиннее
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(btn_Minutes)
layout_line1.addWidget(QLabel('минут')) # нам не нужна переменная для этой надписи

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line4.addStretch(1)

# Теперь созданные 4 строки разместим друг под другой:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)