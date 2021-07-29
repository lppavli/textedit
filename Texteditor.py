
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        self.menu_7 = QtWidgets.QMenu(self.menubar)
        self.menu_7.setObjectName("menu_7")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.new_2 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_2.setIcon(icon)
        self.new_2.setObjectName("new_2")
        self.open = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open.setIcon(icon1)
        self.open.setObjectName("open")
        self.save = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon2)
        self.save.setPriority(QtWidgets.QAction.NormalPriority)
        self.save.setObjectName("save")
        self.print = QtWidgets.QAction(MainWindow)
        self.print.setCheckable(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print.setIcon(icon3)
        self.print.setObjectName("print")
        self.print_page = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/print_page.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_page.setIcon(icon4)
        self.print_page.setObjectName("print_page")
        self.PDF = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PDF.setIcon(icon5)
        self.PDF.setObjectName("PDF")
        self.exit = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon6)
        self.exit.setObjectName("exit")
        self.copy = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copy.setIcon(icon7)
        self.copy.setObjectName("copy")
        self.cut = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cut.setIcon(icon8)
        self.cut.setObjectName("cut")
        self.paste = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paste.setIcon(icon9)
        self.paste.setObjectName("paste")
        self.undo = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo.setIcon(icon10)
        self.undo.setObjectName("undo")
        self.redo = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redo.setIcon(icon11)
        self.redo.setObjectName("redo")
        self.font = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.font.setIcon(icon12)
        self.font.setObjectName("font")
        self.color = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.color.setIcon(icon13)
        self.color.setObjectName("color")
        self.bold = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bold.setIcon(icon14)
        self.bold.setObjectName("bold")
        self.italic = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.italic.setIcon(icon15)
        self.italic.setObjectName("italic")
        self.underline = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.underline.setIcon(icon16)
        self.underline.setObjectName("underline")
        self.left = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icons/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left.setIcon(icon17)
        self.left.setObjectName("left")
        self.center = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.center.setIcon(icon18)
        self.center.setObjectName("center")
        self.right = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icons/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right.setIcon(icon19)
        self.right.setObjectName("right")
        self.justify = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icons/justify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.justify.setIcon(icon20)
        self.justify.setObjectName("justify")
        self.time = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("icons/time.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.time.setIcon(icon21)
        self.time.setObjectName("time")
        self.date = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("icons/date.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.date.setIcon(icon22)
        self.date.setObjectName("date")
        self.marker = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("icons/marker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.marker.setIcon(icon23)
        self.marker.setObjectName("marker")
        self.about = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about.setIcon(icon24)
        self.about.setObjectName("about")
        self.menu.addAction(self.new_2)
        self.menu.addAction(self.open)
        self.menu.addAction(self.save)
        self.menu.addSeparator()
        self.menu.addAction(self.print)
        self.menu.addAction(self.print_page)
        self.menu.addAction(self.PDF)
        self.menu.addAction(self.exit)
        self.menu_2.addAction(self.copy)
        self.menu_2.addAction(self.cut)
        self.menu_2.addAction(self.paste)
        self.menu_2.addSeparator()
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.undo)
        self.menu_2.addAction(self.redo)
        self.menu_3.addAction(self.font)
        self.menu_3.addAction(self.color)
        self.menu_4.addAction(self.bold)
        self.menu_4.addAction(self.italic)
        self.menu_4.addAction(self.underline)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.left)
        self.menu_4.addAction(self.center)
        self.menu_4.addAction(self.right)
        self.menu_4.addAction(self.justify)
        self.menu_5.addAction(self.time)
        self.menu_5.addAction(self.date)
        self.menu_6.addAction(self.marker)
        self.menu_7.addAction(self.about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.toolBar.addAction(self.new_2)
        self.toolBar.addAction(self.open)
        self.toolBar.addAction(self.save)
        self.toolBar.addAction(self.print)
        self.toolBar.addAction(self.print_page)
        self.toolBar.addAction(self.PDF)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.copy)
        self.toolBar.addAction(self.cut)
        self.toolBar.addAction(self.paste)
        self.toolBar.addAction(self.undo)
        self.toolBar.addAction(self.redo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.font)
        self.toolBar.addAction(self.color)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.bold)
        self.toolBar.addAction(self.italic)
        self.toolBar.addAction(self.underline)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.left)
        self.toolBar.addAction(self.center)
        self.toolBar.addAction(self.right)
        self.toolBar.addAction(self.justify)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.time)
        self.toolBar.addAction(self.date)
        self.toolBar.addAction(self.marker)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.about)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Super- Блокнот"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Правка"))
        self.menu_3.setTitle(_translate("MainWindow", "Формат"))
        self.menu_4.setTitle(_translate("MainWindow", "Стили"))
        self.menu_5.setTitle(_translate("MainWindow", "Дата и время"))
        self.menu_6.setTitle(_translate("MainWindow", "Выделитель"))
        self.menu_7.setTitle(_translate("MainWindow", "Справка"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.new_2.setText(_translate("MainWindow", "Создать"))
        self.open.setText(_translate("MainWindow", "Открыть"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.print.setText(_translate("MainWindow", "Печать"))
        self.print_page.setText(_translate("MainWindow", "Параметры печати"))
        self.PDF.setText(_translate("MainWindow", "Экспорт в PDF"))
        self.exit.setText(_translate("MainWindow", "Выход"))
        self.copy.setText(_translate("MainWindow", "Копировать"))
        self.cut.setText(_translate("MainWindow", "Вырезать"))
        self.paste.setText(_translate("MainWindow", "Вставить"))
        self.undo.setText(_translate("MainWindow", "Отменить ввод"))
        self.redo.setText(_translate("MainWindow", "Повторить ввод"))
        self.font.setText(_translate("MainWindow", "Шрифт"))
        self.color.setText(_translate("MainWindow", "Цвет"))
        self.bold.setText(_translate("MainWindow", "Жирный"))
        self.italic.setText(_translate("MainWindow", "Курсив"))
        self.underline.setText(_translate("MainWindow", "Подчеркивание"))
        self.left.setText(_translate("MainWindow", "По левому краю"))
        self.center.setText(_translate("MainWindow", "По центру"))
        self.right.setText(_translate("MainWindow", "По правому краю"))
        self.justify.setText(_translate("MainWindow", "По ширине"))
        self.time.setText(_translate("MainWindow", "Время"))
        self.date.setText(_translate("MainWindow", "Дата"))
        self.marker.setText(_translate("MainWindow", "Выделитель текста"))
        self.about.setText(_translate("MainWindow", "О программе"))

