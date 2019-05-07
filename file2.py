import os
import sqlite3
import glob
import errno
import PyPDF2
from PyQt5 import QtCore, QtGui, QtWidgets
from userinterface_three import Ui_MainWindow2

connection = sqlite3.connect("C:\\Users\lenovo\Desktop\project\gp.sqlite")
cursor2 = connection.cursor()
#cursor2.execute("DELETE FROM Applicant")
###############################################################################

cursor2.execute("SELECT name FROM Job")
result2 = cursor2.fetchall()
cursor2.execute("SELECT jname FROM Applicant")
result3 = cursor2.fetchall()

ID2 = 0
J = []
for i in result2:
    D1 = 0
    for u in result3:
        if i == u:
            D1 = D1 + 1

    J.append(D1)

#c1 = input()
#c2 = input()

F = []


class Ui_Form(object):

    def openWindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1350, 690)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(440, 10, 611, 61))
        ####################
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(35)
        #font.setItalic(True)
        self.label.setFont(font)

        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(120, 130, 69, 22))
        self.comboBox.setObjectName("comboBox")

        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(40, 250, 1100, 150))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 450, 1100, 80))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox")

        self.pushButton_4 = QtWidgets.QLabel(self.groupBox)
        self.textEdit = QtWidgets.QLabel(self.groupBox)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 480, 70, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 480, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(460, 480, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(150, 480, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(350, 480, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(60, 300, 180, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_6")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 480, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 300, 50, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setEnabled(False)


        connection = sqlite3.connect("C:\\Users\lenovo\Desktop\project\gp.sqlite")
        cursor2 = connection.cursor()
        cursor2.execute("SELECT ID FROM Job")
        result = cursor2.fetchall()

        for x in result:
            self.comboBox.addItems(x)

        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(580, 130, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        cursor2.execute("SELECT name FROM Job")
        result = cursor2.fetchall()

        for x in result:
            self.comboBox_2.addItems(x)


        self.comboBox_2.currentIndexChanged.connect(self.selectionchange)
        self.comboBox.currentIndexChanged.connect(self.selectionchange2)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(470, 130, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(960, 130, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1250, 650, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(Form.close)

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(1170, 650, 75, 23))
        self.pushButton_5.setObjectName("pushButton")
        self.pushButton_5.setEnabled(False)

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(1150, 130, 51, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_3.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()

        self.pushButton_2.clicked.connect(self.selectionchange3)
        self.pushButton_3.clicked.connect(self.selectionchange4)
        self.pushButton_4.clicked.connect(self.selectionchange5)
        self.pushButton_5.clicked.connect(self.openWindow)
        #self.pushButton_5.clicked.connect()

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(250, 280, 500, 61))
        self.textEdit.setObjectName("textEdit")

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def selectionchange(self):

        X = self.comboBox_2.currentIndex()
        self.comboBox.setCurrentIndex(X)
        self.lineEdit.setText(str(J[X]))
        self.pushButton_4.setEnabled(True)

    def selectionchange2(self):

        X = self.comboBox.currentIndex()
        self.comboBox_2.setCurrentIndex(X)
        self.lineEdit.setText(str(J[X]))
        self.pushButton_4.setEnabled(True)




    def selectionchange3(self):
        self.pushButton_3.show()
        self.label_5.show()
        self.label_6.show()
        self.lineEdit_2.show()
        self.lineEdit_3.show()


    def selectionchange4(self):

        connection = sqlite3.connect("C:\\Users\lenovo\Desktop\project\gp.sqlite")
        cursor2 = connection.cursor()
        cursor2.execute("INSERT INTO Job VALUES ('" + self.lineEdit_2.text() + "','" + self.lineEdit_3.text() + "')")
        #connection.commit()
        #connection.close()


    def selectionchange5(self):

        self.pushButton_5.setEnabled(True)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Job Candidates Application"))
        self.label_2.setText(_translate("Form", "RefID"))
        self.label_3.setText(_translate("Form", "Job position"))
        self.label_4.setText(_translate("Form", "Number of Applcants"))
        self.pushButton.setText(_translate("Form", "Exit"))
        self.pushButton_5.setText(_translate("Form", "Next"))
        self.label_4.setText(_translate("Form", "Number of Applcants"))
        self.pushButton_2.setText(_translate("Form", "New Job"))
        self.label_5.setText(_translate("Form", "RefID"))
        self.label_6.setText(_translate("Form", "Job position"))
        self.label_7.setText(_translate("Form", "Required majors"))
        self.pushButton_3.setText(_translate("Form", "ADD"))
        self.pushButton_4.setText(_translate("Form", "ADD"))
        self.textEdit.setHtml(_translate("MainWindow2",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

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
################################################################################



path = 'C:\\Users\lenovo\Desktop\Folder1\*.txt'



cursor2.execute("SELECT name from Job")

result = cursor2.fetchall()

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
experence = ""
jname = ""
p1 = ""
p2 = ""





files = glob.glob(path)

for name in files:

    try:
        with open(name) as f:
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
                #Name = open("C:\\Users\lenovo\Desktop\main_project\Lib\\Name.txt", "r")
                #Namelines = []

                #for Line in Name:

                #    Namelines.append(Line)

                #strName = Namelines[0].split(",")
                #strName2 = Namelines[1].split(",")
                #strName3 = Namelines[2].split(",")
                #strName4 = Namelines[3].split(",")
                #strName5 = Namelines[4].split(",")
                #strName6 = Namelines[5].split(",")
                #strName7 = Namelines[6].split(",")
                #strName8 = Namelines[7].split(",")



                #print(len(strName2))
                #U1 = 0
                #while U1 < len(strName):
                #    if i.__contains__(strName[U1]):
                        #print(strName[U1])
                #        U1 = U1 + 1

                #while Namelines[0].__contains__(","):
                #    U2 = U2 + 1

                #while()

                #if i.__contains__(strName2[U1]):
                    #print(strName2[U1])
                #    U1 = U1 + 1

                
                    #Namelines.append(Line)

                #U1 = 0


                #if Namelines[0]:
                #    strName = Namelines[0].split(",")
                #    if i.__contains__(strName[U1]):
                #        U1 = U1 + 1
                #        name = str2[1]


                #if Namelines[1]:
                #    strName = Namelines[1].split(",")
                #    if i.__contains__(strName[U1]):
                #        E_mail = str2[1]


                #if Namelines[2]:
                #    strName = Namelines[2].split(",")
                #    if i.__contains__(strName[U1]):
                #        Date_of_Birth = str2[1]


                #if Namelines[3]:
                #    strName = Namelines[3].split(",")
                #    if i.__contains__(strName[U1]):
                #        Birthplace = str2[1]

                #if Namelines[4]:
                #    strName = Namelines[4].split(",")
                #    if i.__contains__(strName[U1]):
                #        nationality = str2[1]

                #if Namelines[5]:
                #    strName = Namelines[5].split(",")
                #    if i.__contains__(strName[U1]):
                #        phone = str2[1]

                #if Namelines[6]:
                #    strName = Namelines[6].split(",")
                #    if i.__contains__(strName[U1]):
                #        religion = str2[1]

                #if Namelines[7]:
                #    strName = Namelines[7].split(",")
                #    if i.__contains__(strName[U1]):
                #        Sex = str2[1]


                #if Namelines[8]:
                #    strName = Namelines[8].split(",")
                #    if i.__contains__(strName[U1]):
                #        nationality = str2[1]

                v = ["NAME"]
                if i.__contains__(v[0]) or i.__contains__("Name") or i.__contains__("my name is") and not \
                        (i.__contains__("Dr") or i.__contains__("DR") or i.__contains__("dr")):
                    name = str2[1]

                if i.__contains__("DR") or i.__contains__("Dr") or i.__contains__("dr"):
                    name = str5[1]

                if i.__contains__("e-mail") or i.__contains__("E-mail") or i.__contains__("mail"):
                    E_mail = str2[1]

                if i.__contains__("Date of Birth") or i.__contains__("date of birth") or \
                        i.__contains__("DATE OF BIRTH"):
                    Date_of_Birth = str2[1]

                if i.__contains__("place of birth") or i.__contains__("Place of Birth") \
                        or i.__contains__("PLACE OF BIRTH") or i.__contains__("birthplace") \
                        or i.__contains__("Birthplace") or i.__contains__("BIRTHPLACE"):
                    Birthplace = str2[1]

                if i.__contains__("nationality") or i.__contains__("Nationality") or \
                        i.__contains__("NATIONALITY"):
                    nationality = str2[1]
                if i.__contains__("phone") or i.__contains__("PHONE") or \
                        i.__contains__("Phone") or i.__contains__("Phone number"):
                    phone = str2[1]
                if i.__contains__("Religion") or i.__contains__("RELIGION") or \
                        i.__contains__("religion"):
                    religion = str2[1]

                if i.__contains__("SEX") or i.__contains__("sex") or i.__contains__("Gender") or \
                        i.__contains__("GENDER") or i.__contains__("gender"):
                    Sex = str2[1]

                    ########################################################################################
                    ########################################################################################

                if (i.__contains__("Bachelor") or i.__contains__("bachelor") or i.__contains__("B.Sc") or
                    i.__contains__("BSc")) \
                        and not (i.__contains__("master") or i.__contains__("Master")) \
                        and not (i.__contains__("phd") or i.__contains__("PHD") or
                                 i.__contains__("ph.D.")):
                    a = "BSC"

                if (i.__contains__("master") or i.__contains__("Master") or i.__contains__("MSC") or
                    i.__contains__("mcs")
                    or i.__contains__("MASTER")) and not (i.__contains__("phd") or i.__contains__("PHD") or
                                                          i.__contains__("ph.D.")):
                    b = "MSC"

                if i.__contains__("phd") or i.__contains__("PHD") or i.__contains__("ph.D.") \
                        or i.__contains__("PH.D."):
                    c = "PHD"

                    ########################################################################################
                    ########################################################################################

                if ((i.__contains__("Bachelor") or i.__contains__("bachelor") or i.__contains__("B.Sc") or
                     i.__contains__("BSc")) \
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
                # r1 = 1980
                for n in result:
                    # n1 = n[r]
                    if (i.__contains__("Web developer")):
                        jname = "Web developer"
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
                        p1 = str(p1)
                        str8 = p1.split(" ")
                        # R = str8.count()
                        p1 = int(str8[0])
                        # p2 = int(str8[0])
                        experence2 = int(p2) - int(p1)
                        experence = str(experence2)
                # if(i.__contains__(result[0])):
                #    jname = result[0]
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

    cursor3 = connection.cursor()
    cursor3.execute("INSERT INTO Applicant VALUES ('" + NAME + "','" + Date_of_Birth + "','" +
                   Birthplace + "','" + nationality + "','" + phone + "','" + E_mail + "','" + religion + "','" +
                   Qualtification + "','" + University + "','" + major + "','" + experence + "','" + Sex + "','" +
                    jname + "')")

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



    connection.commit()
    #connection.close()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
