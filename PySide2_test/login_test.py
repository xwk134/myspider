from PySide2.QtWidgets import QApplication, QMessageBox, QTextBrowser
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, Qt
from PySide2.QtGui import QIcon

class Stats():
    def __init__(self):
        qfile_stats = QFile("E:/myspider/PySide2_test/login.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()
        self.ui = QUiLoader().load(qfile_stats)

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    # 加载 icon
    app.setWindowIcon(QIcon('logo.ico'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
