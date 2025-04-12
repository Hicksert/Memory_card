#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question 
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append(Question('Чему равен 1 байт?', '8 бит', '2 гигабайта', '32 бита', '1 бит'))
questions_list.append(Question('Зачем в компьютере процессор?', 'Обработка машинного кода', 'хранение памяти', 'вывидение картинки на экран', 'для охлаждения'))
questions_list.append(Question('Самый популярный язык программирования', 'Python', 'C++', 'C', 'JavaScript'))
questions_list.append(Question('Сколько планет в солнечной системе', '8', '5', '3', '9'))
questions_list.append(Question('5 в двоичной системе', '101', '5', '1', '1001'))
questions_list.append(Question('Картошка на польском языке:', 'ziemniak', 'potatoe', 'kartoshka', 'kartosh'))
questions_list.append(Question('В каком году был создан интернет', '1969', '2000', '1990', '1985'))
questions_list.append(Question('в каком году к власти пришли романовы?', '1613', '1554', '1718', '1400'))
app = QApplication([])
layout_card = QVBoxLayout()
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.setLayout(layout_card)
main_win.resize(400,300)
btn_answer1 = QRadioButton('1 вариант')
btn_answer2 = QRadioButton('2 вариант')
btn_answer3 = QRadioButton('3 вариант')
btn_answer4 = QRadioButton('4 вариант')
btn_ok = QPushButton('Ответить')
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)


lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов:')
layoutH1 = QHBoxLayout()
layoutV2 = QVBoxLayout()
layoutV3 = QVBoxLayout()
layoutH1.addWidget(lb_Question)
layoutV2.addWidget(btn_answer1)
layoutV2.addWidget(btn_answer2)
layoutV3.addWidget(btn_answer3)
layoutV3.addWidget(btn_answer4)
layoutH1.addLayout(layoutV2)
layoutH1.addLayout(layoutV3)
RadioGroupBox.setLayout(layoutH1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('ответ будет  тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
        print('Рейтинг:', (main_win.score/main_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно')
            print('Рейтинг:', (main_win.score/main_win.total*100), '%')
def show_correct(res):
    lb_Result.setText(res)
    show_result()


def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_ok():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()
    

btn_ok.clicked.connect(click_ok)
main_win.score = 0
main_win.total = 0
next_question()
main_win.show()
app.exec_()
























