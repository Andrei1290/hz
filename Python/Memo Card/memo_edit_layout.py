from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from memo_app import app

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_from = QFormLayout()

layout_from.addRow('Питання:', txt_Question)
layout_from.addRow('Правильна відповідь:', txt_Answer)
layout_from.addRow('Не вірно', txt_Wrong1)
layout_from.addRow('Не вірно', txt_Wrong2)
layout_from.addRow('Не вірно', txt_Wrong3)