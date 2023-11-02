import sys
from mailtm import Email
import os
import requests
import json
import time
import shutil


from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import typing
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QGraphicsOpacityEffect)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
    

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
                    if str(mails['hydra:member']) != '[]':
                        if self.mainwindow.message_count != len(mails['hydra:member']):
                            between = len(mails['hydra:member']) - self.mainwindow.message_count
                            for message in range(0, between):
                                id = mails['hydra:member'][message]['id']
                                r = requests.get(f'https://api.mail.tm/messages/{id}', headers=header)
                                if r.status_code == 200:
                                    x = json.dumps(r.json())
                                    y = json.loads(x)
                                    html = '<HTML><BODY><meta charset="utf-8">' + str(y['html'][0])[y['html'][0].find('<BODY>') + 6:]
                                    with open(f'cache/{self.mainwindow.message_count + 1}.html', 'w') as f:
                                        f.write(html)
                                self.mainwindow.message_count += between
                                if self.mainwindow.message_count <= 8:
                                    if  self.mainwindow.message_count == 1:
                                        self.founded.emit()
                                    elif self.mainwindow.message_count == 2:
                                        self.mainwindow.message_button_1.show()
                                    elif  self.mainwindow.message_count == 3:
                                        self.mainwindow.message_button_1.show()
                                    elif  self.mainwindow.message_count == 4:
                                        self.mainwindow.message_button_1.show()
                                    elif  self.mainwindow.message_count == 5:
                                        self.mainwindow.message_button_1.show()
                                    elif  self.mainwindow.message_count == 6:
                                        self.mainwindow.message_button_1.show()
                                    elif  self.mainwindow.message_count == 7:
                                        self.mainwindow.message_button_1.show()
                                    elif  self.mainwindow.message_count == 8:
                                        self.mainwindow.message_button_1.show()
                    else:
                        pass
            else:
                break
            time.sleep(5)
        


class MainWindow(QMainWindow):
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
        self.first_message = True
        r = requests.post('https://api.mail.tm/token', json=param)
        if r.status_code == 200:
            x = json.dumps(r.json())
            y = json.loads(x)
            self.copy_button.setText(self.mail.address)
            self.proc_exec = False
            self.message_count = 0
            self.mailthread = MailCheckThread(self)
            self.mailthread.start()
            self.mailthread.founded.connect(self.mytest)
            self.message_button_1.clicked.connect(lambda: self.show_message('test.html'))
            self.copy_button.clicked.connect(self.copy)
            self.copy_button.setToolTip('Click To Copy!📍')
            self.RefreshButton.clicked.connect(self.refresh)
            self.message_button_1.hide()
            self.message_button_2.hide()
            self.message_button_3.hide()
            self.message_button_4.hide()
            self.message_button_5.hide()
            self.message_button_6.hide()
            self.message_button_7.hide()
            self.message_button_8.hide()
            self.scroll.hide()
            self.textBrowser.hide()
            self.opacity_effect = QGraphicsOpacityEffect()
            self.opacity_effect.setOpacity(0.3)
            self.empty_mail_label.setGraphicsEffect(self.opacity_effect)
        else:
            time.sleep(1)
            self.__init__()
    
    def mytest(self):
        self.message_button_1.show()
        self.scroll.show()
        self.empty_mail_icon.hide()
        self.empty_mail_label.hide()
        self.textBrowser.show()

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
            self.copy_button.setText(self.mail.address)
            self.show_message('clear.html')
            self.clear_cache()
        except Exception:
            self.too_fast_label.setText('Too fast!')

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