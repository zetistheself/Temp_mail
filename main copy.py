import sys
from mailtm import Email
import os
import requests
import json
import threading
import time
import shutil


from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import typing
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Temp_Mail(object):
    def setupUi(self, Temp_Mail):
        Temp_Mail.setObjectName("Temp_Mail")
        Temp_Mail.resize(1280, 720)
        Temp_Mail.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(Temp_Mail)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(330, 60, 941, 641))
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
        self.too_fast_label.setGeometry(QtCore.QRect(1070, 10, 131, 31))
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
        self.message_button = QtWidgets.QPushButton(self.centralwidget)
        self.message_button.setGeometry(QtCore.QRect(310, 340, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        self.message_button.setFont(font)
        self.message_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.message_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.message_button.setStyleSheet("")
        self.message_button.setText("")
        self.message_button.setObjectName("message_button")
        self.scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll.setGeometry(QtCore.QRect(30, 60, 261, 631))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        self.scroll.setFont(font)
        self.scroll.setWidgetResizable(False)
        self.scroll.setObjectName("scroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 259, 629))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
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


class MainWindow(QMainWindow, Ui_Temp_Mail):
    def __init__(self):
        self.clear_cache()
        super().__init__()
        uic.loadUi('uci.ui', self)
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
        self.proc_exec = False
        self.message_count = 0
        self.check_proccess = threading.Thread(target=self.check_messages, args=(self.mail.address,), daemon=True)
        self.check_proccess.start()
        self.message_button.clicked.connect(lambda: self.show_message('test.html'))
        self.copy_button.clicked.connect(self.copy)
        self.copy_button.setToolTip('Click To Copy!📍')
        self.RefreshButton.clicked.connect(self.refresh)
        self.widget = QWidget()                 
        self.vbox = QVBoxLayout()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)  
    
    def check_messages(self, mail):
        while True:
            if self.proc_exec == False:
                address = mail
                param = {
                        "address": address,
                        "password": "nonepassword"
                    }
                r = requests.post('https://api.mail.tm/token', json=param)
                x = json.dumps(r.json())
                y = json.loads(x)
                header = {
                    "authorization": f'Bearer {y["token"]}'
                }
                r = requests.get('https://api.mail.tm/messages', headers=header)
                mails = json.loads(r.text)
                if str(mails['hydra:member']) != '[]':
                    if self.message_count != len(mails['hydra:member']):
                        between = len(mails['hydra:member']) - self.message_count
                        for message in range(0, between):
                            id = mails['hydra:member'][message]['id']
                            r = requests.get(f'https://api.mail.tm/messages/{id}', headers=header)
                            x = json.dumps(r.json())
                            y = json.loads(x)
                            html = '<HTML><BODY><meta charset="utf-8">' + str(y['html'][0])[y['html'][0].find('<BODY>') + 6:]
                            with open(f'cache/{self.message_count + 1}.html', 'w') as f:
                                f.write(html)
                            self.object = QPushButton(self)
                            self.object.setText(str(self.message_count + 1))
                            self.object.clicked.connect(lambda: self.show_message(str(self.message_count + 1) + '.html'))
                            self.object.move(50, 50)
                        self.message_count += between
                else:
                    pass
            else:
                break
            time.sleep(5)


    def show_message(self, file_name):
        html_file = open('test.html', encoding='utf-8')
        path = os.path.abspath(file_name)
        print(path)
        self.textBrowser.setUrl(QUrl(f'file:{path}'))
        html_file.close()

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
            self.label.setText(self.mail.address)
        except Exception:
            self.too_fast_label.setText('Too fast!')
        self.clear_cache()

    def copy(self):
        cb = QApplication.clipboard()
        cb.clear()
        cb.setText(self.mail.address)
    
    def clear_cache(self):
        shutil.rmtree('cache')
        os.mkdir('cache')

    def close(self):
        app.exec_()
        self.proc_exec = True
        self.clear_cache()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(ex.close())