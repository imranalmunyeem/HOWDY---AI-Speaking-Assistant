
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QDialog
import cv2
import face_recognition
import numpy as np
import os

from secondWindowGUI import Ui_MainWindow


def nameList(nameofImg):
    if nameofImg.startswith('GP',0):
        return "GP Muthu"
    elif nameofImg.startswith("Steve", 0):
        return "Steve Rogers"
    elif nameofImg.startswith("Natasha",0):
        return "Natasha Romanoff"
    elif nameofImg.startswith("Tony",0):
        return "Tony Stark"
    elif nameofImg.startswith("Thor",0):
        return "Thor"
    elif nameofImg.startswith("Karthick",0):
        return "Karthick"


class Ui_SecondWindow(QDialog):
    def __init__(self):
        super(Ui_SecondWindow, self).__init__()
        self.name = None
        self.mainui = Ui_MainWindow()
        self.mainui.setupUi(self)

        self.mainui.exitButton.clicked.connect(self.close)
        self.mainui.loginButton.clicked.connect(self.sendToLoginScreen)

        self.Videocapture_ = None
        self.image = None

        self.runSlot()


    def sendToLoginScreen(self):
        from loginWndow import Ui_LoginPage
        self.loginPage = Ui_LoginPage()
        self.loginPage.show()
        self.close()

    def runSlot(self):
        print("Clicked Run")
        self.Videocapture_ = "testsubj.mov"
        self.startVideo(self.Videocapture_)
        print("Video Played")

    @pyqtSlot()
    def startVideo(self, camera_name):
        print("video capture started")
        if len(camera_name) == 1:
            self.capture = cv2.VideoCapture(int(camera_name))
        else:
            self.capture = cv2.VideoCapture(camera_name)
        self.timer = QTimer(self)  # Create Timer
        path = 'images'
        if not os.path.exists(path):
            os.mkdir(path)
        # known face encoding and known face name list
        images = []  # images of faces
        self.class_names = []  # names of Images
        self.encode_list = []  # encodings of faces
        self.TimeList1 = []
        self.TimeList2 = []
        photoList = os.listdir(path)

        # print(attendance_list)
        for cl in photoList:
            currentImage = cv2.imread(f'{path}/{cl}')
            images.append(currentImage)
            self.class_names.append(os.path.splitext(cl)[0])
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(img)
            encodes_cur_frame = face_recognition.face_encodings(img, boxes)[0]
            # encode = face_recognition.face_encodings(img)[0]
            self.encode_list.append(encodes_cur_frame)
        print("Encoded Images successfully")
        self.timer.timeout.connect(self.update_frame)  # Connect timeout to the output function
        self.timer.start(10)  # sends the timeout() signal at x=40ms
        print("Video capture ended")

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.displayImage(self.image, self.encode_list, self.class_names, 1)


    def displayImage(self, image, encode_list, class_names, window=1):
        image = cv2.resize(image, (640, 480))
        try:
            image = self.face_rec_(image, encode_list, class_names)
        except Exception as e:
            print(e)
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.mainui.videoLabel.setPixmap(QPixmap.fromImage(outImage))
            self.mainui.videoLabel.setScaledContents(True)
            if self.name == "Karthick":
                self.connectJarvisMainWindow()
                self.timer.stop()

    def face_rec_(self, frame, encode_list_known, class_names):

        faces_cur_frame = face_recognition.face_locations(frame)
        encodes_cur_frame = face_recognition.face_encodings(frame, faces_cur_frame)

        for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
            match = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=0.50)
            face_dis = face_recognition.face_distance(encode_list_known, encodeFace)
            self.name = "unknown"
            best_match_index = np.argmin(face_dis)
            # print("s",best_match_index)
            if match[best_match_index]:
                self.name = class_names[best_match_index]
                self.name = nameList(self.name)
                y1, x2, y2, x1 = faceLoc
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # cv2.rectangle(frame, (x1, y2 + 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, self.name, (x1 - 6, y2 + 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

        return frame



    def connectJarvisMainWindow(self):
        from subprocess import call
        self.close()
        call(["python", 'JARVISmainfile.py'])
