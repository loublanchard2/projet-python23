from NatNetClient import NatNetClient
from PyQt5.QtCore import pyqtSignal, QObject, QTimer, pyqtSlot


class ClientVoliere(QObject):
    # signal for voliere data (AC_ID, pos_x, pos_y,pos_z, quat_a, quat_b, quat_c, quat_d)
    drone_data = pyqtSignal(int, float, float, float, float, float, float)

    def __init__(self):
        super().__init__()

        # create NatNetClient to retrieve data from Motion Tracking
        self.natnet = NatNetClient(rigidBodyListListener=self.receive_rigid_body_list)
        # start the server
        self.natnet.run()

    def stop(self):
        self.natnet.stop()

    def receive_rigid_body_list(self, rigidBodyList, stamp):
        for (ac_id, pos, quat, valid) in rigidBodyList:
            if valid:
                drone_data.emit(ac_id, pos[0], pos[1], pos[2], quat[0], quat[1], quat[2], quat[3])


if __name__ == "__main__":
    app = QApplication([])
    vvt = VvtvvtFlying()
    vvt.drone_data.connect(print)
    app.aboutToQuit.connect(vvt.stop)
    sys.exit(app.exec_())