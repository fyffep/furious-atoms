from furiousatoms import io
from fury import window
from PySide2 import QtWidgets
from PySide2.QtGui import QIcon
import os
from fury.data.fetcher import _get_file_data


class Ui_remote_file(QtWidgets.QMainWindow):

    def __init__(self, app_path=None, parent=None):
        super(Ui_remote_file, self).__init__(parent)
        self.ui_widget = io.load_ui_widget("remote_file.ui")
        self.v_layout = QtWidgets.QVBoxLayout()
        self.v_layout.addWidget(self.ui_widget)
        self.setCentralWidget(self.ui_widget)
        self.setLayout(self.v_layout)
        self.resize(225, 202)
        self.scene = window.Scene()
        self.setWindowIcon(QIcon(io.get_resources_file("splash.png")))
        self.showm = window.ShowManager(scene=self.scene, order_transparent=True)
        self.init_settings()
        self.create_connections()

    def init_settings(self):
        pass

    def create_connections(self):
        self.ui_widget.pushButton_download.clicked.connect(self.download_callback)
        self.ui_widget.pushButton_download.clicked.connect(lambda:self.close())

    def download_callback(self):
        url = self.ui_widget.PlainTextEdit_url.toPlainText()
        
        fname = "user-download.pdb"
        folder = "./furious-atoms-downloads/"
        if not os.path.exists(folder):
            print("Creating new folder %s" % (folder))
            os.makedirs(folder)

        fullpath = os.path.join(folder, fname)
        print('Downloading "%s" to %s from url %s' % (fname, folder, url))
        _get_file_data(fullpath, url)

        if os.path.exists(fullpath):
            self.win.open(fullpath)
        else:
            print("Warning: The file from the URL "+url+" could not be downloaded.")