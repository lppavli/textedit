import sys

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFontDialog, QColorDialog
from Texteditor import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo, Qt, QTime, QDate


class MyWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.new_2.triggered.connect(self.fileNew)
        self.open.triggered.connect(self.openFile)
        self.save.triggered.connect(self.fileSave)
        self.print.triggered.connect(self.filePrint)
        self.print_page.triggered.connect(self.printPreveiw)
        self.PDF.triggered.connect(self.exportPdf)
        self.exit.triggered.connect(self.exitApp)
        self.copy.triggered.connect(self.copyText)
        self.paste.triggered.connect(self.pasteText)
        self.cut.triggered.connect(self.cutText)
        self.undo.triggered.connect(self.textEdit.undo)
        self.redo.triggered.connect(self.textEdit.redo)
        self.font.triggered.connect(self.fontDialog)
        self.color.triggered.connect(self.colorDialog)
        self.bold.triggered.connect(self.textBold)
        self.italic.triggered.connect(self.textItalic)
        self.underline.triggered.connect(self.textUnderline)
        self.left.triggered.connect(self.alignLeft)
        self.right.triggered.connect(self.alignRight)
        self.center.triggered.connect(self.alignCenter)
        self.justify.triggered.connect(self.alignJustify)
        self.time.triggered.connect(self.showTime)
        self.date.triggered.connect(self.showDate)
        self.setWindowIcon(QIcon('icons/edit.png'))
        self.marker.triggered.connect(self.markerText)
        self.about.triggered.connect(self.createDialog)

    def fileNew(self):
        self.textEdit.clear()

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Открыть файл', '')

        if filename[0]:
            f = open(filename[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

    def fileSave(self):
        filename = QFileDialog.getSaveFileName(self, 'Сохранить файл')

        if filename[0]:
            f = open(filename[0], 'w')

        with f:
            text = self.textEdit.toPlainText()
            f.write(text)
            QMessageBox.about(self, 'Сохранить файл', 'Файл успешно сохранен')

    def filePrint(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

    def printPreveiw(self):
        printer = QPrinter(QPrinter.HighResolution)
        review = QPrintPreviewDialog(printer, self)
        review.paintRequested.connect(self.printPreview)
        review.exec_()

    def printPreview(self, printer):
        self.textEdit.print_(printer)

    def exportPdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Сохранить в PDF", None, "PDF files (.pdf) ;; All Files")

        if fn != "":
            if QFileInfo(fn).suffix() == "":
                fn += '.pdf'
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(fn)
                self.textEdit.document().print_(printer)

    def exitApp(self):
        self.close()

    def copyText(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected

    def pasteText(self):
        self.textEdit.append(self.copiedText)

    def cutText(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected
        self.textEdit.cut()

    def fontDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def textBold(self):
        font = QFont()
        font.setBold(True)
        self.textEdit.setFont(font)

    def textItalic(self):
        font = QFont()
        font.setItalic(True)
        self.textEdit.setFont(font)

    def textUnderline(self):
        font = QFont()
        font.setUnderline(True)
        self.textEdit.setFont(font)

    def alignLeft(self):
        self.textEdit.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.textEdit.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.textEdit.setAlignment(Qt.AlignCenter)

    def alignJustify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)

    def showTime(self):
        time = QTime.currentTime()
        self.textEdit.setText(time.toString(Qt.DefaultLocaleLongDate))

    def showDate(self):
        date = QDate.currentDate()
        self.textEdit.setText(date.toString(Qt.DefaultLocaleLongDate))

    def markerText(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextBackgroundColor(color)

    def createDialog(self):
        self.dialog = QMessageBox.about(self, 'О программе', 'Это Super-блокнот')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())