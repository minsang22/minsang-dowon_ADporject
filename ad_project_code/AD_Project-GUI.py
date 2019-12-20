import sys
from PyQt5.QtWidgets import *
import loadFood
import haksick
import random


class Lunch (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.display = QLineEdit('')
        self.display.setReadOnly(True)

    def initUI(self):
        self.setGeometry(100, 200, 700, 800)
        self.setWindowTitle("오점먹?")
        self.school_Result = QTextEdit(self)
        self.random_Result = QTextEdit(self)
        self.random_Result.setFixedHeight(19)
        self.food_Result = QTextEdit(self)

        # 버튼 코드
        schoolButton = QPushButton("교내")
        chinaButton = QPushButton("중식")
        japanButton = QPushButton("일식")
        koreaButton = QPushButton("한식")
        bunsikButton = QPushButton("분식")
        fastFoodButton = QPushButton("패스트푸드")
        clearButton = QPushButton("Clear")
        typeRandomButton = QPushButton("종류 랜덤")
        menuRandomButton = QPushButton("메뉴 랜덤")

        # Hbox1 코드
        Hbox1 = QHBoxLayout()
        Hbox1.addWidget(self.school_Result, 100)

        # Hbox2 코드
        Hbox2 = QHBoxLayout()
        Hbox2.addWidget(schoolButton)
        Hbox2.addWidget(chinaButton)
        Hbox2.addWidget(japanButton)
        Hbox2.addWidget(koreaButton)
        Hbox2.addWidget(bunsikButton)
        Hbox2.addWidget(fastFoodButton)
        Hbox2.addWidget(clearButton)

        # Hbox3 코드
        Hbox3 = QHBoxLayout()
        Hbox3.addWidget(typeRandomButton)
        Hbox3.addWidget(menuRandomButton)
        Hbox3.addWidget(self.random_Result, 100)

        # Hbox4 코드
        Hbox4 = QHBoxLayout()
        Hbox4.addWidget(self.food_Result, 100)

        # Vbox 코드
        Vbox = QVBoxLayout()
        Vbox.addLayout(Hbox1)
        Vbox.addLayout(Hbox2)
        Vbox.addLayout(Hbox3)
        Vbox.addLayout(Hbox4)

        # 수평 정렬 코드
        self.setLayout(Vbox)

        #이벤트 연결 코드
        schoolButton.clicked.connect(self.schoolClicked)
        chinaButton.clicked.connect(self.chinaClicked)
        japanButton.clicked.connect(self.japanClicked)
        koreaButton.clicked.connect(self.koreaClicked)
        bunsikButton.clicked.connect(self.bunsikClicked)
        fastFoodButton.clicked.connect(self.fastFoodClicked)
        clearButton.clicked.connect(self.clearClicked)
        typeRandomButton.clicked.connect(self.typeRandomClicked)
        menuRandomButton.clicked.connect(self.menuRandomClicked)

        #학식 & 레이아웃 설명 띄워주는 코드
        haksick_menu = haksick.haksick()
        self.school_Result.setText(str(haksick_menu.today_menu))
        self.food_Result.setText("음식 목록을 표시해 줄 레이아웃입니다 !")
        self.random_Result.setText("랜덤으로 골라진 음식을 표시해 줄 레이아웃입니다 !")


    finalmenu = ""
    cnt = 0

    school_cnt = 0
    china_cnt = 0
    japan_cnt = 0
    korea_cnt = 0
    bunsik_cnt = 0
    fastFood_cnt = 0

    def schoolClicked(self):
        school = loadFood.loadFood('교내.txt')
        if self.school_cnt == 0:
            self.school_cnt += 1
            if self.cnt == 0:
                self.finalmenu += school.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1

            else:
                self.finalmenu += '\n' + school.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1


    def chinaClicked(self):
        china = loadFood.loadFood('중식.txt')
        if self.china_cnt == 0 :
            self.china_cnt += 1
            if self.cnt == 0:
                self.finalmenu += china.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1

            else:
                self.finalmenu += '\n' + china.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1

    def japanClicked(self):
        japan = loadFood.loadFood('일식.txt')
        if self.japan_cnt == 0:
            self.japan_cnt += 1
            if self.cnt == 0:
                self.finalmenu += japan.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1

            else:
                self.finalmenu += '\n' + japan.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1

    def koreaClicked(self):
        korea = loadFood.loadFood('한식.txt')
        if self.korea_cnt == 0 :
            self.korea_cnt += 1
            if self.cnt == 0:
                self.finalmenu += korea.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1

            else:
                self.finalmenu += '\n' + korea.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1

    def bunsikClicked(self):
        bunsik = loadFood.loadFood('분식.txt')
        if self.bunsik_cnt == 0:
            self.bunsik_cnt += 1
            if self.cnt == 0:
                self.finalmenu += bunsik.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1

            else:
                self.finalmenu += '\n' + bunsik.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1

    def fastFoodClicked(self):
        fastFood = loadFood.loadFood('패스트푸드.txt')
        if self.fastFood_cnt == 0:
            self.fastFood_cnt += 1
            if self.cnt == 0:
                self.finalmenu += fastFood.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1

            else:
                self.finalmenu += '\n' + fastFood.menu_str
                self.food_Result.setText(self.finalmenu)
                self.cnt += 1

    def clearClicked(self):
        self.food_Result.setText("")
        self.finalmenu = ""
        self.cnt = 0
        self.school_cnt = 0
        self.china_cnt = 0
        self.japan_cnt = 0
        self.korea_cnt = 0
        self.bunsik_cnt = 0
        self.fastFood_cnt = 0

    def typeRandomClicked(self):
        self.cnt += 1
        foodtype = ['교내.txt', '분식.txt', '일식.txt', '패스트푸드.txt', '중식.txt', '한식.txt']
        menu_type = random.sample(foodtype, 1)
        menu_Kind = menu_type[0]
        typeRandom = loadFood.loadFood(menu_Kind)
        self.food_Result.setText(typeRandom.menu_str)

    def menuRandomClicked(self):

        finalrandom = ''

        if self.cnt == 0 :
            self.random_Result.setText(" 아직 골라둔 메뉴가 없습니다 ! ")

        else:
            while finalrandom == '' :
                random_list = self.finalmenu.split('\n')
                random_menu = random.sample(random_list, 1)
                finalrandom = random_menu[0]
                self.random_Result.setText(finalrandom)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    today_lunch = Lunch()
    today_lunch.show()
    sys.exit(app.exec_())
