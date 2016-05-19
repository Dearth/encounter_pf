#!/usr/bin/python

import sys
import sqlite3
from PyQt4 import QtGui, QtCore

class EncounterWidget(QtGui.QWidget):
	def __init__(self):
		super(EncounterWidget,self).__init__()

		self.initUI()

	def initUI(self):
		QtGui.QToolTip.setFont(QtGui.QFont("SansSerif",10))

		align = QtGui.QLabel("Alignment")
		align.setToolTip("Define the alignment of monsters considered for the encounter.")
		align_box = QtGui.QComboBox(self)
		align_box.addItem("Any")
		align_box.addItem("Any Evil")
		align_box.addItem("Any Good")
		align_box.addItem("Any Chaotic")
		align_box.addItem("Any Lawful")
		align_box.addItem("Any Neutral")
		align_box.addItem("Lawful Good")
		align_box.addItem("Neutral Good")
		align_box.addItem("Chaotic Good")
		align_box.addItem("Lawful Neutral")
		align_box.addItem("Neutral")
		align_box.addItem("Chaotic Neutral")
		align_box.addItem("Lawful Evil")
		align_box.addItem("Neutral Evil")
		align_box.addItem("Chaotic Evil")

		cr = QtGui.QLabel("CR")
		cr.setToolTip("Define the Maximum CR of an encounter.")
		cr_box = QtGui.QComboBox(self)
		cr_box.addItem("Any")
		cr_box.addItem("1/8")
		cr_box.addItem("1/6")
		cr_box.addItem("1/4")
		cr_box.addItem("1/3")
		cr_box.addItem("1/2")

		for i in range(1,31):
			cr_box.addItem(str(i))

		climate = QtGui.QLabel("Climate")
		climate.setToolTip("Define the climate of the encounter (includes Planes).")
		climate_box = QtGui.QComboBox(self)
		climate_box.addItem("Any")
		climate_box.addItem("Tropical")
		climate_box.addItem("Hot")
		climate_box.addItem("Warm")
		climate_box.addItem("Temperate")
		climate_box.addItem("Cold")
		climate_box.addItem("Abaddon")
		climate_box.addItem("The Abyss")
		climate_box.addItem("Akashic Record")
		climate_box.addItem("Astral Plane")
		climate_box.addItem("The Boneyard")
		climate_box.addItem("Dimension of Dreams")
		climate_box.addItem("Elemental Plane of Air")
		climate_box.addItem("Elemental Plane of Earth")
		climate_box.addItem("Elemental Plane of Fire")
		climate_box.addItem("Elemental Plane of Water")
		climate_box.addItem("Elysium")
		climate_box.addItem("Ethereal Plane")
		climate_box.addItem("Heaven")
		climate_box.addItem("Hell")
		climate_box.addItem("Limbo")
		climate_box.addItem("Negative Energy Plane")
		climate_box.addItem("Nirvana")
		climate_box.addItem("Positive Energy Plane")
		climate_box.addItem("Purgatory")
		climate_box.addItem("Shadow Plane")
		climate_box.addItem("Utopia")

		terrain = QtGui.QLabel("Terrain")
		terrain.setToolTip("Define the current terrain for the encounter.")
		terrain_box = QtGui.QComboBox(self)	
		terrain_box.addItem("Any")
		terrain_box.addItem("Air")
		terrain_box.addItem("Aquatic (any)")
		terrain_box.addItem("Coastline")
		terrain_box.addItem("Desert")
		terrain_box.addItem("Forest")
		terrain_box.addItem("Freshwater")
		terrain_box.addItem("Glacier")
		terrain_box.addItem("Hills")
		terrain_box.addItem("Jungle")
		terrain_box.addItem("Lake")
		terrain_box.addItem("Land (any)")
		terrain_box.addItem("Marsh")
		terrain_box.addItem("Mountains")
		terrain_box.addItem("Ocean")
		terrain_box.addItem("Plains")
		terrain_box.addItem("River")
		terrain_box.addItem("Ruins")
		terrain_box.addItem("Swamp")
		terrain_box.addItem("Underground")
		terrain_box.addItem("Urban")
		terrain_box.addItem("Volcano")
		
		monster_type = QtGui.QLabel("Monster Type")
		monster_type.setToolTip("Set the creature type of monsters in the encounter.")
		mt_box = QtGui.QComboBox(self)
		mt_box.addItem("Any")
		mt_box.addItem("Aberration")
		mt_box.addItem("Animal")
		mt_box.addItem("Construct")
		mt_box.addItem("Dragon")
		mt_box.addItem("Fey")
		mt_box.addItem("Humanoid")
		mt_box.addItem("Magical Beast")
		mt_box.addItem("Monstrous Humanoid")
		mt_box.addItem("Ooze")
		mt_box.addItem("Outsider")
		mt_box.addItem("Plant")
		mt_box.addItem("Undead")
		mt_box.addItem("Vermin")

		result = QtGui.QLabel("Results")
		results = QtGui.QTextEdit()
		results.setReadOnly(True)

		gen = QtGui.QPushButton("Generate", self)
		gen.setToolTip("Generate random encounter list")
		gen.resize(gen.sizeHint())

		grid = QtGui.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(cr, 1, 0)
		grid.addWidget(cr_box,2,0)

		grid.addWidget(align, 3, 0)
		grid.addWidget(align_box, 4, 0)

		grid.addWidget(climate, 5, 0)
		grid.addWidget(climate_box,6,0)

		grid.addWidget(terrain, 7, 0)
		grid.addWidget(terrain_box,8,0)

		grid.addWidget(monster_type, 9, 0)
		grid.addWidget(mt_box, 10, 0)

		grid.addWidget(gen, 11, 0)
		
		grid.addWidget(result,1,1)
		grid.addWidget(results,2,1,11,1)

		self.setLayout(grid)

		self.show()

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()

		self.initUI()

	def initUI(self):
		enc = EncounterWidget()

		self.setCentralWidget(enc)
		
		self.setGeometry(300,300,700,450)
		self.setWindowTitle("Encounter Generator")
		self.setWindowIcon(QtGui.QIcon("PathfinderRPGLogo_500.jpeg"))

		self.statusBar().showMessage("Ready")
		

		self.show()
		
def main():
	app = QtGui.QApplication(sys.argv)
	enc = MainWindow()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
