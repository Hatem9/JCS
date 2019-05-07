import os
import sqlite3
import glob
import errno
import PyPDF2
from docx import Document
from PyQt5 import QtCore, QtGui, QtWidgets
from Second_screen import Ui_Form6
from update import Ui_Form11
from all_applicants import Ui_Form13
from Last_interface import Ui_Form100


connection = sqlite3.connect("C:\\Users\lenovo\Desktop\main_project\FinalDataBase.sqlite")
cursor2 = connection.cursor()




class Ui_Form3(object):

    def openmainWindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form6()
        self.ui.setupUi(self.window)
        self.window.show()

    def openmainWindow2(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form11()
        self.ui.setupUi(self.window)
        self.window.show()

    def openmainWindow3(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form13()
        self.ui.setupUi(self.window)
        self.window.show()

    def openmainWindow4(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form100()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(788, 598)
        Form.setMaximumSize(QtCore.QSize(788, 598))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 213, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 191, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 213, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 191, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 213, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 191, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Form.setPalette(palette)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 295, 461, 41))
        self.horizontalLayoutWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_2.setAutoRepeatDelay(300)
        self.pushButton_2.setAutoRepeatInterval(100)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setAutoRepeatInterval(100)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, 0, 811, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\lenovo\Desktop\main_project\Capture.PNG"))
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(674, 552, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setItalic(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(Form.close)
        self.pushButton_3.clicked.connect(self.openmainWindow)
        self.pushButton_2.clicked.connect(self.openmainWindow2)
        self.pushButton_4.clicked.connect(self.openmainWindow3)
        self.pushButton.clicked.connect(self.openmainWindow4)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Welcome to Main Page"))
        self.pushButton_2.setText(_translate("Form", "Account"))
        self.pushButton_4.setText(_translate("Form", "Applicants"))
        self.pushButton_3.setText(_translate("Form", "Jobs"))
        self.pushButton.setText(_translate("Form", "Setting"))
        self.pushButton_5.setText(_translate("Form", "Logout"))

###############################################################################
os.chdir('C:\\Users\lenovo\Desktop\Folder2')


for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    path = open("C:\\Users\lenovo\Desktop\Folder2\\" + file_name + file_ext, "rb")
    pdfReader = PyPDF2.PdfFileReader(path)
    pageObj = pdfReader.getPage(0)
    r = pageObj.extractText()
    f = open("C:\\Users\lenovo\Desktop\Folder1" + "\\" + file_name + ".txt", "w")
    f.write(r)

################################################################################
os.chdir('C:\\Users\lenovo\Desktop\Folder4')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    path = Document("C:\\Users\lenovo\Desktop\Folder4\\" + file_name + file_ext)
    f = open("C:\\Users\lenovo\Desktop\Folder1" + "\\" + file_name + ".txt", "w")
    for para in path.paragraphs:
        f.write(para.text)
        f.write("\n")

################################################################################

path = 'C:\\Users\lenovo\Desktop\Folder1\*.txt'

cursor2.execute("SELECT Name from Job")

result = cursor2.fetchall()

cursor2.execute("SELECT Words From Lib")

final = cursor2.fetchall()

M = []

for i in final[0]:
    M.append(i)

for i in final[1]:
    M.append(i)

for i in final[2]:
    M.append(i)

for i in final[3]:
    M.append(i)

for i in final[4]:
    M.append(i)

for i in final[5]:
    M.append(i)


for i in final[6]:
    M.append(i)

for i in final[7]:
    M.append(i)

for i in final[8]:
    M.append(i)

for i in final[9]:
    M.append(i)

for i in final[10]:
    M.append(i)

strx0 = M[0].split("/")
strx1 = M[1].split("/")
strx2 = M[2].split("/")
strx3 = M[3].split("/")
strx4 = M[4].split("/")
strx5 = M[5].split("/")
strx6 = M[6].split("/")
strx7 = M[7].split("/")
strx8 = M[8].split("/")
strx9 = M[9].split("/")
strx10 = M[10].split("/")


c = ""
c1 = ""
c2 = ""
b = ""
b1 = ""
b2 = ""
a = ""
a1 = ""
a2 = ""
NAME = ""
Date_of_Birth = ""
Birthplace = ""
nationality = ""
phone = ""
E_mail = ""
religion = ""
Qualtification = ""
University = ""
major = ""
Sex = ""
grade = ""
experence = "0"
jname = ""
p1 = ""
p2 = ""

files = glob.glob(path)

for name in files:

    try:
        with open(name) as f:
            number = 0
            for i in f:


                str0 = i.split(" in ")
                str1 = i.split("  ")
                str2 = i.split(": ")
                str3 = i.split(", ")
                str4 = i.split("from")
                str5 = i.split(".")
                str6 = i.split("/")
                str7 = i.split("-")

                U1 = 0
                U2 = 0


                for i2 in strx0:
                    if i.__contains__(i2) and not (i.__contains__("Dr") or i.__contains__("DR") or i.__contains__("dr")):
                        NAME = str2[1]

                if i.__contains__("DR") or i.__contains__("Dr") or i.__contains__("dr"):
                    NAME = str5[1]

                for i2 in strx5:
                    if i.__contains__(i2):
                        E_mail = str2[1]

                for i2 in strx1:
                    if i.__contains__(i2):
                        Date_of_Birth = str2[1]

                for i2 in strx2:
                    if i.__contains__(i2):
                        Birthplace = str2[1]

                for i2 in strx3:
                    if i.__contains__(i2):
                        nationality = str2[1]

                for i2 in strx4:
                    if i.__contains__(i2):
                        phone = str2[1]

                for i2 in strx6:
                    if i.__contains__(i2):
                        religion = str2[1]

                for i2 in strx10:
                    if i.__contains__(i2):
                        Sex = str2[1]

                if i.__contains__("I want"):
                    jname = str2[1]
                    jname = jname[:-1]
                    ###################################################
                    ###################################################
                    ###################################################

                if (i.__contains__("Bachelor") or i.__contains__("bachelor") or i.__contains__("B.Sc") or
                    i.__contains__("BSc") or i.__contains__("BSC")) \
                        and not (i.__contains__("master") or i.__contains__("Master")) \
                        and not (i.__contains__("phd") or i.__contains__("PHD") or
                                 i.__contains__("ph.D.")):
                    a = "BSC"


                if (i.__contains__("master") or i.__contains__("Master") or i.__contains__("MSC") or
                    i.__contains__("mcs")
                    or i.__contains__("MASTER")) and not (i.__contains__("phd") or i.__contains__("PHD") or
                                                          i.__contains__("ph.D.")):
                    b = "MSC"


                if i.__contains__("phd") or i.__contains__("PHD") or i.__contains__("ph.D."):

                    c = "PHD"

                    ########################################################################################
                    ########################################################################################

                if ((i.__contains__("Bachelor") or i.__contains__("bachelor") or i.__contains__("B.Sc") or
                     i.__contains__("BSc") or i.__contains__("BSC")) \
                    and not (i.__contains__("master") or i.__contains__("Master")) \
                    and not (i.__contains__("phd") or i.__contains__("PHD") or i.__contains__("ph.D."))) \
                        and (i.__contains__("in")):
                    a2 = str0[1]
                    if a2.__contains__("from"):
                        m = a2.split(" from ")
                        a1 = m[1]
                        a2 = m[0]

                if ((i.__contains__("master") or i.__contains__("Master") or i.__contains__("MSC") or
                     i.__contains__("mcs")
                     or i.__contains__("MASTER") or i.__contains__("M. SC")) and not (i.__contains__("phd") or
                                                                                      i.__contains__("PHD") or
                                                                                      i.__contains__("ph.D."))) \
                        and (i.__contains__("in")):

                    b2 = str0[1]
                    if b2.__contains__("from"):
                        m = b2.split(" from ")
                        b1 = m[1]
                        b2 = m[0]

                if (i.__contains__("phd") or i.__contains__("PHD")) or i.__contains__("ph.D.") and \
                        (i.__contains__("in")):
                    c2 = str0[1]
                    if c2.__contains__("from"):
                        m = c2.split(" from ")
                        c1 = m[1]
                        c2 = m[0]

                r = 0
                n1 = ""
                #print(result)




                W = ["Programmer","Web developer"]

                for n in W:

                    if i.__contains__(n):
                        #print(i)
                        Ji = 20


                #print(jname)
                for n in result:
                    for n2 in n:

                        if i.__contains__(n2) and not i.__contains__("I want"):


                            if n2 == jname:
                                #print(i)
                                r = r + 1
                                if i.__contains__("/"):
                                    p1 = str6[2]
                                    p2 = str6[-1]
                                elif i.__contains__("."):
                                    p1 = str5[2]
                                    p2 = str5[-1]
                                elif i.__contains__("now") or i.__contains__("Till now") or \
                                        i.__contains__("till now") or i.__contains__("TILL NOW") or \
                                        i.__contains__("Till Now"):
                                    p2 = 2019
                #print(str(p1))

                p1 = str(p1)
                str8 = p1.split(" ")
                p1 = str8[0]
                #print(p1)
                #print(p2)

                if (p1 != '') and (p2 != ''):
                    p1 = int(p1)
                    p2 = int(p2)
                    #print(p2 - p1)
                    experence2 = int(p2) - int(p1)
                    experence = str(experence2)

                ########################################################################################
                ########################################################################################

            if c.__contains__("PHD"):
                Qualtification = c
                University = c1
                major = c2

            elif b.__contains__("MSC"):
                Qualtification = b
                University = b1
                major = b2

            elif a.__contains__("BSC"):
                Qualtification = a
                University = a1
                major = a2


    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
    #experence = "0"
    cursor3 = connection.cursor()
    cursor3.execute("INSERT INTO Applicant VALUES ('" + NAME + "','" + Date_of_Birth + "','" +
                    Birthplace + "','" + nationality + "','" + phone + "','" + E_mail + "','" + religion + "','" +
                    Qualtification + "','" + University + "','" + major + "'," + experence + ",'" + Sex + "','" +
                    jname + "')")
    connection.commit()
    NAME = ""
    Date_of_Birth = ""
    Birthplace = ""
    nationality = ""
    phone = ""
    E_mail = ""
    religion = ""
    Qualtification = ""
    University = ""
    major = ""
    jname = ""
    experence = "0"
    a = ""
    b = ""
    c = ""
#connection.commit()
connection.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

