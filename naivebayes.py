import numpy as np

class NaiveBayes:
	"""
	data is a numpy array [num voc, num doc]
	classes is an array of length num doc containing the labeled classes of the different docs
	"""
	def __init__ (data, classes):
		self.data = data
		self.pos=zeros(data.shape)