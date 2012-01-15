import urllib

"""

 @author  Martin Okorodudu <webmaster@fotocrib.com>
 @license http://opensource.org/licenses/lgpl-license.php
          GNU Lesser General Public License, Version 2.1



 This class is a wrapper for the fototools service.


"""


class Fotocrib:

	def __init__(self,imgSrc, filename):
		self.imgSrc = imgSrc
		self.filename = filename
		
	
	def thumbnail(self):
		self.__handleRequest({"q" : "thumbnail"})
	
	
	def label(self, text, location):
		self.__handleRequest({"q" : "label", "t" : text, "l" : location})
	
	
	def roundCorners(self, radius):
		self.__handleRequest({"q" : "round", "r" : radius})
		
		
	def cube(self, r, g, b):
		self.__handleRequest({"q" : "cube", "r" : r, "g" : g, "b" : b})
	
	
	def lift(self, height):
		self.__handleRequest({"q" : "raise", "h" : height})
	
	
	def scale(self, pct):
		self.__handleRequest({"q" : "scale", "p" : pct})
	
	
	def resize(self, width, height):
		self.__handleRequest({"q" : "resize", "w" : width, "h" : height})
	
	
	def focus(self):
		self.__handleRequest({"q" : "focus"})
		
		
	def emboss(self):
		self.__handleRequest({"q" : "emboss"})
		
	
	def paint(self):
		self.__handleRequest({"q" : "paint"})
	
	
	def repaint(self, r, g, b):
		self.__handleRequest({"q" : "repaint", "r" : r, "g" : g, "b" : b})
	
	
	def frame(self, border, r, g, b):
		self.__handleRequest({"q" : "frame", "t" : border, "r" : r, "g" : g, "b" : b})
	
	
	def roundFrame(self, border,radius, r, g, b):
		self.__handleRequest({"q" : "rframe", "t" : border, "v" : radius, "r" : r, "g" : g, "b" : b})
	
	
	def mirror(self):
		self.__handleRequest({"q" : "mirror"})
	
	
	def grayscale(self):
		self.__handleRequest({"q" : "grayscale"})
	
	
	def brighten(self):
		self.__handleRequest({"q" : "brighten"})
	
	
	def sobel(self):
		self.__handleRequest({"q" : "sobel"})
	
	
	def blur(self):
		self.__handleRequest({"q" : "blur"})
	
	
	
	def __handleRequest(self, params):
		argList = map(lambda(k, v) : str(k) + "=" + str(v), params.items())
		url = "http://fotocrib.com/fototools.php?s=" + self.imgSrc + "&" + "&".join(argList)
		
		stream = urllib.urlopen(url)
		img = stream.read()
		stream.close()
		
		self.__writeToFile(self.filename, "w", img)
		
	
	def __writeToFile(self, filename, mode, content):
		fd = None
		try:
			fd = open(filename, mode)
			fd.write(content)
		finally:
			if fd is not None:
				fd.close()
			
		
	def getImgSrc(self):
		return self.imgSrc
	
	
	def setImgSrc(self, value):
		self.imgSrc = value
	imgSrc = property(fset=setImgSrc, fget=getImgSrc)
	
	
	def getFileName(self):
		return self.filename
	
	
	def setFileName(self, value):
		self.filename = value
	filename = property(fset=setFileName, fget=getFileName)
	
	 