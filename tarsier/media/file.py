# encoding: utf-8

import os
import hashlib


class MediaFile(object):
	def __init__(self, root, name):
		self.root = root
		self.name = name
		self.full_path = os.path.join(root, name)
		self.hash = hashlib.sha1(self.full_path.encode('utf-8')).hexdigest()[:8]
		self.size = os.path.getsize(self.full_path)

		_, ext = os.path.splitext(name)
		if ext == '.ogg':
			self.mimetype = 'video/ogg'
		elif ext == '.mp4':
			self.mimetype = 'video/mp4'