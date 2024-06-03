import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

class LinkOpener(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Buton oluştur
        btn = QPushButton('Linke Git', self)
        btn.clicked.connect(self.open_link)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # Pencere ayarları
        self.setGeometry(300, 300, 200, 150)
        self.setWindowTitle('Linke Yönlendirme')
        self.show()

    def open_link(self):
        # Belirtilen URL'yi aç
        QDesktopServices.openUrl(QUrl('https://www.youtube.com/'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LinkOpener()
    sys.exit(app.exec_())
