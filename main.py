import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Диалог открытия файлов (и папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt # нужна константа Qt.KeepAspectRatio для изменения размеров с сохранением пропорций
from PyQt5.QtGui import QPixmap # оптимизированная для показа на экране картинка
 
from PIL import Image, ImageFilter
 
app = QApplication([])
win = QWidget()       
win.resize(700, 500) 
win.setWindowTitle('Easy Editor')
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()
 
btn_left = QPushButton("Лево")
btn_right = QPushButton("Право")
btn_flip = QPushButton("Зеркало")
btn_sharp = QPushButton("Резкость")
btn_bw = QPushButton("Ч/Б")
btn_blur = QPushButton("Блюр")
btn_contour= QPushButton("Контур")


row = QHBoxLayout()          
col1 = QVBoxLayout()         
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      
col1.addWidget(lw_files)     
col2.addWidget(lb_image, 95)
row_tools = QHBoxLayout()   
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_blur)
row_tools.addWidget(btn_contour)

col2.addLayout(row_tools)
 
row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)
 
win.show()
 
workdir = ''
 
def filter(files, extensions):
	result = []
	for filename in files:
		for ext in extensions:
			if filename.endswith(ext):
				result.append(filename)
	return result
 
def chooseWorkdir():
	global workdir
	workdir = QFileDialog.getExistingDirectory()
 
def showFilenamesList():
	extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
	chooseWorkdir()
	try:
		filenames = filter(os.listdir(workdir), extensions)
	except:
		pass
	lw_files.clear()
	try:
		for filename in filenames:
			lw_files.addItem(filename)
	except:
		pass


btn_dir.clicked.connect(showFilenamesList)
 
class ImageProcessor():
	def __init__(self):
		self.image = None
		self.dir = None
		self.filename = None
		self.save_dir = "Modified/"
	def loadImage(self, dir, filename):
		''' при загрузке запоминаем путь и имя файла '''
		self.dir = dir
		self.filename = filename
		image_path = os.path.join(dir, filename)
		self.image = Image.open(image_path)

	def do_bw(self):
		self.image = self.image.convert("L")
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_left(self):
		self.image = self.image.transpose(Image.ROTATE_90)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_1(self):
		self.image = self.image.rotate(1)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_45(self):
		self.image = self.image.rotate(45)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_flip(self):
		self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_cropped(self,left,up,right,down):
		box = (left,up,right,down)
		self.image = self.image.crop(box)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_sharpness(self):
		self.image = self.image.filter(ImageFilter.SHARPEN)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_blur(self):
		self.image = self.image.filter(ImageFilter.BLUR)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_smooth(self):
		self.image = self.image.filter(ImageFilter.SMOOTH)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_contour(self):
		self.image = self.image.filter(ImageFilter.CONTOUR)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_detail(self):
		self.image = self.image.filter(ImageFilter.DETAIL)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_edge_enhance(self):
		self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def do_smooth_more(self):
		self.image = self.image.filter(ImageFilter.SMOOTH_MORE)
		self.saveImage()
		image_path = os.path.join(self.dir, self.save_dir, self.filename)
		self.showImage(image_path) 
	def saveImage(self):
		''' сохраняет копию файла в подпапке '''
		path = os.path.join(self.dir, self.save_dir)
		if not(os.path.exists(path) or os.path.isdir(path)):
			os.mkdir(path)
		image_path = os.path.join(path, self.filename)
		self.image.save(image_path)

	def showImage(self, path):
		lb_image.hide()
		pixmapimage = QPixmap(path)
		w, h = lb_image.width(), lb_image.height()
		pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
		lb_image.setPixmap(pixmapimage)
		lb_image.show()
def showChosenImage():
	if lw_files.currentRow() >= 0:
		filename = lw_files.currentItem().text()
		workimage.loadImage(workdir, filename)
		image_path = os.path.join(workimage.dir, workimage.filename)
		workimage.showImage(image_path)
 
workimage = ImageProcessor() #текущая рабочая картинка для работы
lw_files.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_1)
btn_right.clicked.connect(workimage.do_45)
btn_flip.clicked.connect(workimage.do_flip)
btn_sharp.clicked.connect(workimage.do_sharpness)
btn_blur.clicked.connect(workimage.do_blur)
btn_contour.clicked.connect(workimage.do_contour)
# btn_bw.clicked.connect(workimage.do_bw)
# btn_bw.clicked.connect(workimage.do_bw)

app.exec()
