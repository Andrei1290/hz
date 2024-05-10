from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget

from memo_app import app
from Memo_data import *
from memo_main_layout import *
from memo_card_layout import *
from memo_edit_layout import *
from random import shuffle

main_width, main_height = 1000, 450
card_width, card_height = 600, 500 
time_unit = 1000



questions_listmodel = QuestionListModel()
frm_edit = QuestionEdit(0, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3)
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
frm_card = 0
timer = QTimer()
win_card = QWidget()
win_main = QWidget()

def testlist():
    frm = Question('Яблокo', 'apple', 'application', 'pinapple', 'apply')
    questions_listmodel.form_list.append(frm)
    frm = Question ('Дom', 'house', 'horse', 'hurry', 'hour')
    questions_listmodel.form_list.append(frm)
    frm = Question ('Mbiшb', 'mouse', 'mouth', 'muse', 'museum')
    questions_listmodel.form_list.append(frm)
    frm = Question('чиcлo', 'number', 'digit', 'amount', 'summary')
    questions_listmodel.form_list.append(frm)

def set_card():
    win_card=QWidget() 
    win_card.resize(card_width, card_height) 
    win_card.move(300, 300) 
    win_card.setWindowTitle("Memory card")
    win_card.setLayout(layout_card) 

def sleep_card():
    win_card.hide()
    timer.setInterval(time_unit * btn_Minutes.value())
    timer.start()

def show_card():
    win_card.show()
    timer.stop()




text_wrong = "Вірно"
text_correct = "HE1вiрно" 

#frm = Form("Питання1?", "Правильна відповідь", "Відповідь невірна", "Відповідь невірна", "Відповідь невірна")
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)


testlist()
set_card()


win_main.show()
app.exec_()