from furiousatoms import io
from fury import window, utils
from PySide2 import QtWidgets
from furiousatoms.structure import bbox
from PySide2.QtGui import QIcon


"""
    Ui_box class creates a widget for building box and water
"""
class Ui_box(QtWidgets.QMainWindow): #QWidget

    def __init__(self, app_path=None, parent=None):
        super(Ui_box, self).__init__(parent)
        self.box = io.load_ui_widget("box.ui")
        self.v_layout = QtWidgets.QVBoxLayout()
        self.v_layout.addWidget(self.box)
        self.setCentralWidget(self.box)
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
        self.box.pushButton_build_box.clicked.connect(self.box_builder_callback)
        self.box.pushButton_build_box.clicked.connect(lambda:self.close())


    def initial_box_dim(self, box_lx, box_ly, box_lz):
        self.box.SpinBox_lx.setValue(box_lx)
        self.box.SpinBox_ly.setValue(box_ly)
        self.box.SpinBox_lz.setValue(box_lz)

    def box_builder_callback(self):
        active_window = self.win.active_mdi_child()
        SM = active_window.universe_manager
        box_lx = float(self.box.SpinBox_lx.text())
        box_ly = float(self.box.SpinBox_ly.text())
        box_lz = float(self.box.SpinBox_lz.text())
        SM.box_lx, SM.box_ly, SM.box_lz = box_lx, box_ly, box_lz
        if SM.bbox_actor:
            active_window.scene.rm(SM.bbox_actor)
        SM.bbox_actor, _ = bbox(box_lx, box_ly, box_lz, colors=SM.box_color, linewidth=2, fake_tube=True)
        active_window.scene.add(SM.bbox_actor)
        utils.update_actor(SM.bbox_actor)
        SM.bbox_actor.GetMapper().GetInput().GetPointData().GetArray('colors').Modified()
        active_window.render()
        active_window.show()