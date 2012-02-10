#!/usr/bin/env python2
# coding: utf-8

import provider
from Contact import Contact
from contact_storage import ContactStorage
from similarity import areMergeable

from PyQt4 import QtGui,QtCore

import codecs
import sys

class MainWidget(QtGui.QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
                
        self.contact_storage = ContactStorage()
        
        # debug only
        contacts=[]
        #print contacts
        for contact in contacts:
            self.contact_storage.insert(contact)
        #contact1=Contact(name="bay",addidionalName="Alexander",familyName="Famname")
        #contact2=Contact(name="Alex Bers",addidionalName="AdditionalName",familyName="fam")
        
        #self.contact_storage.insert(contact1)
        #self.contact_storage.insert(contact2)
            
        # Инициализация пользовательского интерфейса
        self.resize(1000, 500)

        self.merge_checkbox = QtGui.QCheckBox('Merge similar contacts', self)
        self.merge_checkbox.setGeometry(5, 410,450,20)

        self.btn1 = QtGui.QPushButton('googlecsv', self)
        self.btn1.setGeometry(5, 440,100,50)
        self.btn1.pressed.connect(self.googlecsv_button_presed)
        
        self.btn2 = QtGui.QPushButton('thunderbirdcsv', self)
        self.btn2.setGeometry(205, 440,100,50)
        self.btn2.pressed.connect(self.thunderbirdcsv_button_presed)
        
        self.btn3 = QtGui.QPushButton('vkontakte', self)
        self.btn3.setGeometry(405, 440,100,50)
        self.btn3.pressed.connect(self.vkontakte_button_presed)
   
        self.btn4 = QtGui.QPushButton('facebook', self)
        self.btn4.setGeometry(605, 440,100,50)
        self.btn4.pressed.connect(self.facebook_button_presed)

        self.btn5 = QtGui.QPushButton('moikrug', self)
        self.btn5.setGeometry(805, 440,100,50)
        self.btn5.pressed.connect(self.moikrug_button_presed)
        
        self.search_field = QtGui.QLineEdit(self)
        self.search_field.setGeometry(205, 410, 200, 25)
        
        self.search_btn = QtGui.QPushButton(u"Искать", self)
        self.search_btn.setGeometry(405, 410,100,25)
        self.search_btn.pressed.connect(self.search_button_presed)
        
        #self.merge_checkbox.setChecked(True)
        self.merge_checkbox.stateChanged.connect(self.rebuild_contact_list)
        
        self.contact_list=QtGui.QTableWidget(self)
        self.contact_list.resize(1000,400)
        
        self.rebuild_contact_list()
                    
        self.center()
        self.setWindowTitle(u'Адресная книга')
        self.show()
        
    def center(self):
        "Перемещает своё окно в центр экрана"
        qr = self.frameGeometry()
        qr.moveCenter(QtGui.QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

    def rebuild_contact_list(self):
        "Перегенерация центральной таблицы"
        fieldNames = Contact.fieldNames

        contacts_num=self.contact_storage.count()
        
        self.contact_list.clearContents()
        self.contact_list.setSortingEnabled(True)
        self.contact_list.setColumnCount(len(fieldNames))
        self.contact_list.setHorizontalHeaderLabels(fieldNames)
        self.contact_list.setRowCount(contacts_num)

        for row in range(contacts_num):
            self.contact_list.showRow(row+1)
        
        for contact_num in range(contacts_num):
            contact=self.contact_storage.get_contact(contact_num)

            if self.contact_list.isRowHidden(contact_num):
                continue

            # проверка на то, есть ли с чем смержить
            mergelist=[]
            if self.merge_checkbox.isChecked():
                for contact_num_other in range(contact_num+1,contacts_num):
                    contact_other=self.contact_storage.get_contact(contact_num_other)
                    if areMergeable(contact, contact_other)==2:
                        mergelist.append(contact_num_other)
                        self.contact_list.hideRow(contact_num_other)
                
            for fieldnum,fieldname in enumerate(fieldNames):
                text=contact.__dict__[fieldname]

                for contact_num_other in mergelist:
                    contact_other=self.contact_storage.get_contact(contact_num_other)
                    othertext=contact_other.__dict__[fieldname]
                    if text !=othertext:
                        text+=" | " + contact_other.__dict__[fieldname]
                
                self.contact_list.setItem(contact_num,fieldnum,QtGui.QTableWidgetItem(text))
        
        self.contact_list.resizeColumnsToContents()

    def keyPressEvent(self,event):
        "Нажали клавишу"
        if event.key()==QtCore.Qt.Key_Delete:
            self.contact_storage.drop_contact_by_id(self.contact_list.currentRow)
         
    def googlecsv_button_presed(self):
        filename=QtGui.QFileDialog.getOpenFileName(self,"Open Image", "", "All files (*)")
        if not filename:
            return

        contacts=provider.importFromGoogleCSV(filename)
            
        for contact in contacts:
            self.contact_storage.insert(contact)
        self.rebuild_contact_list()
            
    def thunderbirdcsv_button_presed(self):
        filename=QtGui.QFileDialog.getOpenFileName(self,"Open Image", "", "All files (*)")
        if not filename:
            return
        
        contacts=provider.importFromThunderbirdCSV(filename)
        
        for contact in contacts:
            self.contact_storage.insert(contact)
        self.rebuild_contact_list()


    def vkontakte_button_presed(self):
        provider.importFromVKontakte_authorize()
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Enter the response of vk.com after your authorization: ')
            
        if not ok:
            return
            
        contacts=provider.importFromVKontakte(str(text))
        for contact in contacts:
            self.contact_storage.insert(contact)
        self.rebuild_contact_list()
    
    def facebook_button_presed(self):
        raise NotImplementedError
    
    def moikrug_button_presed(self):
        raise NotImplementedError
    
    def search_button_presed(self):
        self.contact_storage = self.contact_storage.search(self.search_field)
        self.rebuild_contact_list()
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    gui = MainWidget()
    ret=app.exec_()
    sys.exit(ret)
