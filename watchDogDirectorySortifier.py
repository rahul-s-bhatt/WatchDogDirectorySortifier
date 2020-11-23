from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time

import re

import shutil

def sem(filename, folder_destination):
	regx = re.findall("\\d", filename)
	moduleNo = int(regx[0])

	for folder in os.listdir(folder_destination):
		if folder == "MAD":
			folder_destination += "\\MAD\\" + "Module " + str(moduleNo)

	return folder_destination

class MyHandler(FileSystemEventHandler):
	def on_modified(self, event):
		for filename in os.listdir(folder_to_track):
			if(re.search("^Module", filename)):
				src = folder_to_track + "\\" + filename

				temp_destination = sem(filename, folder_destination)

				new_destination = temp_destination + "\\" + filename

				# os.rename(src, new_destination)
				shutil.move(src, new_destination)

folder_to_track = "C:\\Users\\BHATT\\Downloads"
# folder_to_track = "C:\\Users\\BHATT\\Desktop\\myFolder"
folder_destination = "E:\\Sem7"
# folder_destination = "C:\\Users\\BHATT\\Desktop\\newFolder"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
	while True:
		time.sleep(2)
except KeyboardInterrupt:
	observer.stop()

observer.join()