#!/usr/bin/env python3

import sys, os

from PyQt5 import uic
from PyQt5.QtCore import (QDir, QStandardPaths, QDirIterator, QFileInfo,
	QUrl)
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtMultimedia import (QMediaPlayer, QMediaPlaylist,
	QMediaContent)

class Music(QMainWindow):
	def __init__(self, parent=None):
		super().__init__()
		uic.loadUi(QDir.current().absoluteFilePath('music.ui'), self)
		#print(QDir.current().absoluteFilePath('music.ui'))
		self.player = QMediaPlayer()
		self.playlist = QMediaPlaylist()
		self.player.setPlaylist(self.playlist)
		self.playMusicBtn.clicked.connect(self.player.play)
		self.pauseMusicBtn.clicked.connect(self.player.pause)
		self.stopMusicBtn.clicked.connect(self.player.stop)
		self.nextMusicBtn.clicked.connect(self.playlist.next)
		self.previousMusicButton.clicked.connect(self.playlist.previous)
		self.openFilesBtn.clicked.connect(self.openFiles)
		self.openDirectoryBtn.clicked.connect(self.openDir)
		self.playlist.currentMediaChanged.connect(self.updateLabels)
		self.show()

	def buildPlayList(self, fileNames):
		for name in fileNames:
			print(name)
			url = QUrl.fromLocalFile(name)
			self.playlist.addMedia(QMediaContent(url))
			#self.playlist.setPlaybackMode(QMediaPlaylist.Loop)


	def openFiles(self):
		#fileNames, _ = QFileDialog.getOpenFileNames(self, "Open Files")
		music = QStandardPaths.writableLocation(QStandardPaths.MusicLocation)
		path, _ = QFileDialog.getOpenFileName(self, "Open file", directory=music,
			options=QFileDialog.DontUseNativeDialog)
		print(type(path))
		print(path)
		self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))

		print(type(path))
		print(path)

	def openDir(self):
		#dir _ = QtGui.QFileDialog.getExistingDirectory(None, 'Select a directory:', 'C:\\', QtGui.QFileDialog.ShowDirsOnly)
		home = QStandardPaths.writableLocation(QStandardPaths.HomeLocation)
		d = QFileDialog.getExistingDirectory(caption="Choose Directory", directory=home,
			options=QFileDialog.DontUseNativeDialog)
		#print(x)
		files = os.listdir(d)
		#print(type(files))
		for i in files:
			path = os.path.join(d, i)
			self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(path)))
			#print('{} {}'.format(path, type(i)))
 
		#print(os.listdir(path=x))
		#self.buildPlayList(os.listdir(path=x))
		songCount = self.playlist.mediaCount()
		self.songsLoadedLbl.setText('Songs Loaded = {}'.format(songCount))

	def updateLabels(self, media=None):
		#print(media)
		self.statusBar().showMessage(str(media.canonicalUrl().fileName()))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Music()
	sys.exit(app.exec_())
