try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui
import importlib
from . import config
from . import curveCreateUtil as ccut
import os
importlib.reload(config)
importlib.reload(ccut)

IMAGE_DIR = 'C:/Users/HP/Documents/maya/2024/scripts/Final_createCurveControl/PNG'

class CurveCreatorDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle("Curvec Control Creator")
		self.resize(300,550)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet(
			'''
				background-color: #03A6A1 ;
				color: white ;
				font-family: Broadway ;
				font-size: 16px;
			'''
		)

		#pngTopPart
		self.imageTopLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f'{IMAGE_DIR}/test2.png')
		scaledPixmap = self.imagePixmap.scaled(
			QtCore.QSize(300,100),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)

		self.imageTopLabel.setPixmap(scaledPixmap)
		self.imageTopLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addWidget(self.imageTopLabel, alignment=QtCore.Qt.AlignTop)


		#jntSelectionPart
		self.jntSelectLayout = QtWidgets.QVBoxLayout()
		self.mainLayout.addLayout(self.jntSelectLayout)

		#Label
		self.jntSelectLabel = QtWidgets.QLabel("Joint Selection :")
		self.jntSelectLabel.setStyleSheet(
			'''
				color: #FFE3BB;
				font-size: 18px;
			'''
		)
		self.jntSelectLayout.addWidget(self.jntSelectLabel)

		#radio
		self.radioHeirachy = QtWidgets.QRadioButton("Hierachy")
		self.radioHeirachy.setStyleSheet(
			'''
				QRadioButton::indicator:unchecked{
					border: 2px solid #FFE3BB;
				    border-radius: 8px;
				    background-color: #03A6A1;
				    width: 12px;
				    height: 12px;
				}
				QRadioButton::indicator:checked {
			        border: 2px solid #FF4F0F;
				    border-radius: 8px;
				    background-color: #FF4F0F;
				    width: 12px;
				    height: 12px;
				}
			'''
		)
		self.radioSelection = QtWidgets.QRadioButton("Selection")
		self.radioSelection.setStyleSheet(
			'''
				QRadioButton::indicator:unchecked{
					border: 2px solid #FFE3BB;
				    border-radius: 8px;
				    background-color: #03A6A1;
				    width: 12px;
				    height: 12px;
				}
				QRadioButton::indicator:checked {
			        border: 2px solid #FF4F0F;
				    border-radius: 8px;
				    background-color: #FF4F0F;
				    width: 12px;
				    height: 12px;
				}
			'''
		)
		self.jntSelectLayout.addWidget(self.radioHeirachy)
		self.jntSelectLayout.addWidget(self.radioSelection)

		self.groupType = QtWidgets.QButtonGroup()
		self.groupType.addButton(self.radioHeirachy)
		self.groupType.addButton(self.radioSelection)

		#namePart
		self.nameLayout = QtWidgets.QVBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)

		self.nameLabel = QtWidgets.QLabel("Name :")
		self.nameLabel.setStyleSheet(
			'''
				color: #FFE3BB;
				font-size: 18px;
			'''
		)
		self.nameLayout.addWidget(self.nameLabel)

		#Radio1
		self.matchJointRadio = QtWidgets.QRadioButton("Match Joint Name")
		self.matchJointRadio.setStyleSheet(
			'''
				QRadioButton::indicator:unchecked{
					border: 2px solid #FFE3BB;
				    border-radius: 8px;
				    background-color: #03A6A1;
				    width: 12px;
				    height: 12px;
				}
				QRadioButton::indicator:checked {
			        border: 2px solid #FF4F0F;
				    border-radius: 8px;
				    background-color: #FF4F0F;
				    width: 12px;
				    height: 12px;
				}
			'''
		)
		self.nameLayout.addWidget(self.matchJointRadio)

		#SupLayout
		self.nameInputLayout = QtWidgets.QHBoxLayout()

		#Radio2
		self.nameRadio = QtWidgets.QRadioButton("Name :")
		self.nameRadio.setStyleSheet(
			'''
				QRadioButton::indicator:unchecked{
					border: 2px solid #FFE3BB;
				    border-radius: 8px;
				    background-color: #03A6A1;
				    width: 12px;
				    height: 12px;
				}
				QRadioButton::indicator:checked {
			        border: 2px solid #FF4F0F;
				    border-radius: 8px;
				    background-color: #FF4F0F;
				    width: 12px;
				    height: 12px;
				}
			'''
		)
		self.nameInputLayout.addWidget(self.nameRadio)

		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet(
			'''
				QLineEdit{
					background-color: #F5DAA7;
					color: #FF4F0F;
					border-radius: 8px;
				}
			'''
		)
		self.nameInputLayout.addWidget(self.nameLineEdit)

		self.groupName = QtWidgets.QButtonGroup()
		self.groupName.addButton(self.matchJointRadio)
		self.groupName.addButton(self.nameRadio)

		#add Sub in main
		self.nameLayout.addLayout(self.nameInputLayout)


		#ShapePart
		self.shapeSelectLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.shapeSelectLayout)

		#shapeLabel
		self.shapeLabel = QtWidgets.QLabel("Shape :")
		self.shapeLabel.setStyleSheet(
			'''
				color: #FFE3BB;
			'''
		)
		self.shapeSelectLayout.addWidget(self.shapeLabel)

		#comboBox
		self.shapeSelectBox = QtWidgets.QComboBox()
		self.shapeSelectBox.addItems(config.Shape)
		self.shapeSelectBox.setStyleSheet(
			'''
				QComboBox {
                border-radius: 8px;
                padding: 5px;
                background-color: #FFE3BB;
                color: #FFA673;
                min-height: 30px;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-top-right-radius: 8px;
                border-bottom-right-radius: 8px;
                background-color: #FFE3BB;
            }

            QComboBox::down-arrow {
                image: none;
                width: 12px;
                height: 12px;
            }

            QComboBox:on
                padding-top: 5px;
                padding-left: 6px;
            }

            QComboBox QAbstractItemView {
                border: 1px solid #03A6A1;
                selection-background-color: #FFA673;
                selection-color: #FF4F0F;
                background-color: #FFE3BB;
                color: #FFA673;
                outline: 0;
            }

            QComboBox QAbstractItemView::item {
                padding: 5px;
                margin: 1px;
            }

            QComboBox QAbstractItemView::item:hover {
                background-color: #d6eaf8;
            }
			'''
		)
			#รอแก้คอมโบ
		self.shapeSelectLayout.addWidget(self.shapeSelectBox)


		#other Part
		self.otherLayout = QtWidgets.QVBoxLayout()
		self.mainLayout.addLayout(self.otherLayout)

		self.snapCheckBox = QtWidgets.QCheckBox(" Snap to Joint")
		self.mainLayout.addWidget(self.snapCheckBox)

		self.createGroup = QtWidgets.QCheckBox(" Create Group")
		self.mainLayout.addWidget(self.createGroup)

		self.creatMainControl = QtWidgets.QCheckBox(" Create Main Control")
		self.mainLayout.addWidget(self.creatMainControl)


		#ButtonPart
		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)

		#create
		self.createButton = QtWidgets.QPushButton("Create")
		self.buttonLayout.addWidget(self.createButton)
		self.createButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #FF4F0F;
					border-radius: 12px;
					font-weight: bold;
					color: #FFE3BB;
					padding: 4px;
				}
				QPushButton:hover{
					background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FF4F0F, stop:1 #FFA673);
					}
				QPushButton:pressed{
					background-color: FFE3BB;
					}

			'''
		)
		self.createButton.clicked.connect(self.onClickCreateCurve)

		#cancle
		self.cancelButton = QtWidgets.QPushButton("Cancel")
		self.buttonLayout.addWidget(self.cancelButton)
		self.cancelButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #FF4F0F;
					border-radius: 12px;
					font-weight: bold;
					color: #FFE3BB;
					padding: 4px;
				}
				QPushButton:hover{
					background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #FF4F0F, stop:1 #FFA673);
					}
				QPushButton:pressed{
					background-color: FFE3BB;
					}

			'''
		)
		self.cancelButton.clicked.connect(self.close)

		self.mainLayout.addStretch()

		
		#pngTopPart
		self.imagelBottonLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f'{IMAGE_DIR}/test2.png')
		scaledPixmap = self.imagePixmap.scaled(
			QtCore.QSize(300,100),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)

		self.imagelBottonLabel.setPixmap(scaledPixmap)
		self.imagelBottonLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.mainLayout.addStretch()

		self.mainLayout.addWidget(self.imagelBottonLabel, alignment=QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)

	def getUserSelection(self):

		#selectionPart
		if self.radioHeirachy.isChecked():
			select_mode = "Hierarchy"
		elif self.radioSelection.isChecked():
			select_mode = "Selection"
		else:
			select_mode = None

		#namePart
		if self.matchJointRadio.isChecked():
			name_mode = "Match Joint Name"
			custom_name = None
		elif self.nameRadio.isChecked():
			name_mode = "Custom"
			custom_name = self.nameLineEdit.text().strip() or None
		else:
			name_mode = None
			custom_name = None

		#shapePart
		shape_value = self.shapeSelectBox.currentText()

		#optionPart
		snap_to_joint = self.snapCheckBox.isChecked()
		create_group = self.createGroup.isChecked()
		create_main_control = self.creatMainControl.isChecked()

		data = {
			"Selection": select_mode,
			"Name": {
				"Mode": name_mode,
				"CustomName": custom_name
			},
			"Shape": shape_value,
			"Options": {
				"SnapToJoint": snap_to_joint,
				"CreateGroup": create_group,
				"CreateMainControl": create_main_control
			}
		}

		return data

	def onClickCreateCurve(self):
	    data = self.getUserSelection()
	    ccut.process_user_selection(data)

def run():
	global ui
	try:
		ui.close()
	except:
		pass
	ptr =wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = CurveCreatorDialog(parent=ptr)
	ui.show()