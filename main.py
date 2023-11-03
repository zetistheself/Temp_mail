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


class CheckConnectivity(QtCore.QObject):
    def __init__(self):
        try:
            r = requests.get("https://www.google.com/")
            ex = MainWindow()
            ex.show()
        except:
            ex = InternetLose()
            ex.show()


class InternetLose(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('internet_lose.ui', self)
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
                                    json_dumps = json.dumps(r.json())
                                    json_text = json.loads(json_dumps)
                                    html = '<HTML><BODY><meta charset="utf-8">' + str(json_text['html'][0])[json_text['html'][0].find('<BODY>') + 6:]
                                    with open(f'cache/{self.mainwindow.message_count + 1}.html', 'w') as f:
                                        f.write(html)
                                print(json_text)
                                self.mainwindow.message_count += between
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
        


class MainWindow(QMainWindow):
    def __init__(self):
        self.clear_cache()
        super().__init__()
        uic.loadUi('uci.ui', self)
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
        self.scroll.setWidgetResizable(True)
        self.vbox.setAlignment(Qt.AlignTop)
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
    
    def mytest(self):
        self.scroll.show()
        self.empty_mail_icon.hide()
        self.empty_mail_label.hide()
        self.textBrowser.show()
        self.widget = QWidget()
        for message in range(len(self.hydra) - 1, -1, -1):
            button = QPushButton(f'{self.hydra[message]["subject"]}\nFROM: {self.hydra[message]["from_address"]}')
            button.clicked.connect(lambda: self.show_message("cache/" + self.hydra[message]["file_name"]))
            button.setMinimumHeight(100)
            button.setStyleSheet("QPushButton { text-align: left; }")
            self.vbox.addWidget(button)
            self.widget.setLayout(self.vbox)
            self.scroll.setWidget(self.widget)

    def show_message(self, file_name):
        html_file = open('test.html', encoding='utf-8')
        path = os.path.abspath(file_name)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ic = CheckConnectivity()
    sys.exit(app.exec_())