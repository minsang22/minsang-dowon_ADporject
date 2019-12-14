import sys
from PyQt5.QtWidgets import *


class Lunch (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 200, 600, 650)
        self.setWindowTitle("오점먹?")
        self.school_Result = QTextEdit()
        self.random_Result = QTextEdit(self)
        self.random_Result.setFixedHeight(40)
        self.food_Result = QTextEdit(self)
        # 버튼 코드
        schoolButton = QPushButton("학식")
        chinaButton = QPushButton("중식")
        japanButton = QPushButton("일식")
        koreaButton = QPushButton("한식")
        bunsikButton = QPushButton("분식")
        fastFoodButton = QPushButton("패스트 푸드")
        randomButton = QPushButton("랜덤")

        # Hbox1
        Hbox1 = QHBoxLayout()
        Hbox1.addWidget(self.school_Result, 100)

        # Hbox2
        Hbox2 = QHBoxLayout()
        Hbox2.addWidget(schoolButton)
        Hbox2.addWidget(chinaButton)
        Hbox2.addWidget(japanButton)
        Hbox2.addWidget(koreaButton)
        Hbox2.addWidget(bunsikButton)
        Hbox2.addWidget(fastFoodButton)

        Hbox3 = QHBoxLayout()
        Hbox3.addWidget(randomButton)
        Hbox3.addWidget(self.random_Result, 100)

        Hbox4 = QHBoxLayout()
        Hbox4.addWidget(self.food_Result, 100)

        # Vbox3 코드
        Vbox = QVBoxLayout()
        Vbox.addLayout(Hbox1)
        Vbox.addLayout(Hbox2)
        Vbox.addLayout(Hbox3)
        Vbox.addLayout(Hbox4)

        # 수평 정렬 코드
        self.setLayout(Vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    today_lunch = Lunch()
    today_lunch.show()
    sys.exit(app.exec_())

