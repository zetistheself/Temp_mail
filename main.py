import sys
from mailtm import Email
import os
import requests
import json
import time
import shutil


from PyQt5 import QtCore, uic, QtNetwork
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import typing
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QGraphicsOpacityEffect, QDialog)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 310, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius: 20px;\n"
"background-color: black;\n"
"color: white")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 30, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 90, 191, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/1496957-200.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate("Dialog", "No internet connection!"))


class Ui_Temp_Mail(object):
    def setupUi(self, Temp_Mail):
        Temp_Mail.setObjectName("Temp_Mail")
        Temp_Mail.resize(1313, 686)
        Temp_Mail.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(Temp_Mail)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(320, 150, 991, 621))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        self.textBrowser.setFont(font)
        self.textBrowser.setAccessibleName("")
        self.textBrowser.setStyleSheet("border: 2px, solid black")
        self.textBrowser.setObjectName("textBrowser")
        self.Inbox_text = QtWidgets.QLabel(self.centralwidget)
        self.Inbox_text.setGeometry(QtCore.QRect(0, 10, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(25)
        self.Inbox_text.setFont(font)
        self.Inbox_text.setToolTip("")
        self.Inbox_text.setStyleSheet("")
        self.Inbox_text.setAlignment(QtCore.Qt.AlignCenter)
        self.Inbox_text.setObjectName("Inbox_text")
        self.RefreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.RefreshButton.setGeometry(QtCore.QRect(1180, 0, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(40)
        self.RefreshButton.setFont(font)
        self.RefreshButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RefreshButton.setStyleSheet("border-radius: 0px;")
        self.RefreshButton.setObjectName("RefreshButton")
        self.too_fast_label = QtWidgets.QLabel(self.centralwidget)
        self.too_fast_label.setGeometry(QtCore.QRect(1070, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.too_fast_label.setFont(font)
        self.too_fast_label.setStyleSheet("color: red;")
        self.too_fast_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.too_fast_label.setObjectName("too_fast_label")
        self.scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll.setGeometry(QtCore.QRect(20, 50, 281, 621))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        self.scroll.setFont(font)
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(False)
        self.scroll.setObjectName("scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 629))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 0, 261, 621))
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 261, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vbox = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setObjectName("vbox")
        self.scroll.setWidget(self.scrollAreaWidgetContents)
        self.copy_button = QtWidgets.QPushButton(self.centralwidget)
        self.copy_button.setGeometry(QtCore.QRect(340, 10, 671, 41))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(25)
        self.copy_button.setFont(font)
        self.copy_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copy_button.setToolTip("")
        self.copy_button.setToolTipDuration(-1)
        self.copy_button.setWhatsThis("")
        self.copy_button.setAccessibleName("")
        self.copy_button.setAccessibleDescription("")
        self.copy_button.setStyleSheet("*{\n"
"    background-color: rgba(10, 0, 0, 0);\n"
"}\n"
"*:hover{\n"
"    color:blue;\n"
"}")
        self.copy_button.setText("")
        self.copy_button.setObjectName("copy_button")
        self.empty_mail_label = QtWidgets.QLabel(self.centralwidget)
        self.empty_mail_label.setGeometry(QtCore.QRect(200, 170, 921, 151))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.empty_mail_label.setFont(font)
        self.empty_mail_label.setObjectName("empty_mail_label")
        self.empty_mail_icon = QtWidgets.QLabel(self.centralwidget)
        self.empty_mail_icon.setGeometry(QtCore.QRect(540, 330, 221, 211))
        font = QtGui.QFont()
        font.setPointSize(200)
        self.empty_mail_icon.setFont(font)
        self.empty_mail_icon.setObjectName("empty_mail_icon")
        Temp_Mail.setCentralWidget(self.centralwidget)

        self.retranslateUi(Temp_Mail)
        QtCore.QMetaObject.connectSlotsByName(Temp_Mail)

    def retranslateUi(self, Temp_Mail):
        _translate = QtCore.QCoreApplication.translate
        Temp_Mail.setWindowTitle(_translate("Temp_Mail", "Temp_Mail"))
        self.Inbox_text.setText(_translate("Temp_Mail", "📨Inbox messages:"))
        self.RefreshButton.setToolTip(_translate("Temp_Mail", "Get new mail"))
        self.RefreshButton.setText(_translate("Temp_Mail", "🔄"))
        self.too_fast_label.setText(_translate("Temp_Mail", "Too fast!"))
        self.empty_mail_label.setText(_translate("Temp_Mail", "              Your email is empty.\n"
"Try to make some friend in real life."))
        self.empty_mail_icon.setText(_translate("Temp_Mail", "📭"))


class CheckConnectivity(QtCore.QObject):
    def __init__(self):
        try:
            r = requests.get("https://www.google.com/")
            ex = MainWindow()
            ex.show()
        except:
            ex = InternetLose()
            ex.show()


class InternetLose(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.exit)
        self.label_2.setPixmap(QPixmap('images/connection_lose_image'))
    
    def exit(self):
        sys.exit()


class MailCheckThread(QThread):
    founded = pyqtSignal()
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow

    def run(self):
        while True:
            print('working')
            if self.mainwindow.proc_exec == False:
                address = self.mainwindow.mail.address
                param = {
                        "address": address,
                        "password": "nonepassword"
                    }
                r = requests.post('https://api.mail.tm/token', json=param)
                if r.status_code == 200:
                    x = json.dumps(r.json())
                    y = json.loads(x)
                    header = {
                        "authorization": f'Bearer {y["token"]}'
                    }
                    r = requests.get('https://api.mail.tm/messages', headers=header)
                    if r.status_code == 200:
                        mails = json.loads(r.text)
                    else:
                        print('error')
                        time.sleep(2)
                    if str(mails['hydra:member']) != '[]':
                        if self.mainwindow.message_count != len(mails['hydra:member']):
                            between = len(mails['hydra:member']) - self.mainwindow.message_count
                            for message in range(0, between):
                                id = mails['hydra:member'][message]['id']
                                r = requests.get(f'https://api.mail.tm/messages/{id}', headers=header)
                                if r.status_code == 200:
                                    json_dumps = json.dumps(r.json())
                                    json_text = json.loads(json_dumps)
                                    html = '<HTML><BODY><meta charset="utf-8">' + str(json_text['html'][0])[json_text['html'][0].find('<BODY>') + 6:]
                                    with open(f'cache/{self.mainwindow.message_count + 1}.html', 'w') as f:
                                        f.write(html)
                                    self.mainwindow.message_count += 1
                                    from_address = json_text['from']['address']
                                    from_name = json_text['from']['name']
                                    receaved_at = json_text['createdAt']
                                    file_name = f'{self.mainwindow.message_count}.html'
                                    subject = json_text['subject']
                                    self.mainwindow.hydra.append({
                                        'from_address': from_address,
                                        'from_name': from_name,
                                        'receaved_at': receaved_at,
                                        'file_name': file_name,
                                        'subject': subject,
                                    })
                                self.founded.emit()
                    else:
                        pass
            else:
                break
            time.sleep(5)


class MainWindow(QMainWindow, Ui_Temp_Mail):
    def __init__(self):
        self.clear_cache()
        super().__init__()
        self.setupUi(self)
        self.too_fast_label.setText('')
        self.mail = Email()
        self.hydra = []
        self.mail.register(password="nonepassword")
        param = {
            "address": self.mail.address,
            "password": "nonepassword"
            }
        self.first_message = True
        self.vbox = QVBoxLayout(self) 
        self.vbox.setAlignment(Qt.AlignTop)
        self.scroll.setWidgetResizable(True)
        r = requests.post('https://api.mail.tm/token', json=param)
        if r.status_code == 200:
            x = json.dumps(r.json())
            y = json.loads(x)
            self.copy_button.setText(self.mail.address)
            self.proc_exec = False
            self.message_count = 0
            self.mailthread = MailCheckThread(self)
            self.mailthread.start()
            self.mailthread.founded.connect(self.create_button)
            self.copy_button.clicked.connect(self.copy)
            self.copy_button.setToolTip('Click To Copy!📍')
            self.RefreshButton.clicked.connect(self.refresh)
            self.scroll.hide()
            self.textBrowser.hide()
            self.opacity_effect = QGraphicsOpacityEffect()
            self.opacity_effect.setOpacity(0.3)
            self.empty_mail_label.setGraphicsEffect(self.opacity_effect)
        else:
            time.sleep(1)
            self.__init__()
    
    def create_button(self):
        print(self.hydra)
        self.scroll.show()
        self.empty_mail_icon.hide()
        self.empty_mail_label.hide()
        self.textBrowser.show()
        self.widget.deleteLater()
        self.widget = QWidget()
        self.vbox = QVBoxLayout(self) 
        self.vbox.setAlignment(Qt.AlignTop)
        self.scroll.setWidget(self.widget)
        for message in range(len(self.hydra) - 1, -1, -1):
            button = QPushButton(f'{self.hydra[message]["subject"]}\nFrom: {self.hydra[message]["from_address"]}\nReceaved at: {self.hydra[message]["receaved_at"][:10].split("-")[2]}/{self.hydra[message]["receaved_at"][:10].split("-")[1]}/{self.hydra[message]["receaved_at"][:10].split("-")[0]} ({int(self.hydra[message]["receaved_at"][11:16].split(":")[0]) + 3}:{self.hydra[message]["receaved_at"][11:16].split(":")[1]})')
            button.clicked.connect(self.show_message)
            button.setMinimumHeight(80)
            button.setToolTip(str(message))
            button.setToolTipDuration(0)
            button.setMaximumWidth(270)
            button.setStyleSheet("QPushButton { text-align: left; }")
            self.vbox.addWidget(button)
            self.widget.setLayout(self.vbox)
            self.scroll.setWidget(self.widget)

    def show_message(self):
        if self.hydra == []:
            path = os.path.abspath(f'clear.html')
            self.textBrowser.setUrl(QUrl(f'file:{path}'))
            return
        sender = self.sender().toolTip()
        path = os.path.abspath(f'cache/{int(sender) + 1}.html')
        self.textBrowser.setUrl(QUrl(f'file:{path}'))

    def refresh(self):
        try:
            self.too_fast_label.setText('')
            self.mail = Email()
            self.mail.register(password="nonepassword")
            param = {
                "address": self.mail.address,
                "password": "nonepassword"
                }
            r = requests.post('https://api.mail.tm/token', json=param)
            x = json.dumps(r.json())
            y = json.loads(x)
            self.copy_button.setText(self.mail.address)
            self.hydra = []
            self.show_message()
            self.widget.deleteLater()
            self.widget = QWidget()
            self.vbox = QVBoxLayout(self) 
            self.clear_cache()
            self.scroll.hide()
            self.textBrowser.hide()
            self.empty_mail_icon.show()
            self.empty_mail_label.show()
        except Exception:
            self.too_fast_label.setText('Too fast!')

    def copy(self):
        cb = QApplication.clipboard()
        cb.clear()
        cb.setText(self.mail.address)
    
    def clear_cache(self):
        shutil.rmtree('cache')
        os.mkdir('cache')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ic = MainWindow()
    ic.show()
    sys.exit(app.exec_())