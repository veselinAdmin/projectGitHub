
import os.path
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
listDrive= []
pulledFile=None
upload_file='py_logo.png'

gfile = drive.CreateFile({'parents': [{'id': '10HBiD0fMkEfhZZbLUteUyfdiWLmtm1m-'}]})
gfile.SetContentFile(upload_file)
gfile.Upload()

file_list = drive.ListFile(	{'q': "'{}' in parents and trashed=false".format('10HBiD0fMkEfhZZbLUteUyfdiWLmtm1m-')}).GetList()
for file in file_list:
	print('title: %s, id: %s' % (file['title'], file['id']))
	listDrive.append([file['title'], file['id']])

for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
	print('Checking {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
	if file['title'] == upload_file:
		print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
		pulledFile=file.GetContentFile(file['title'])
		listDrive.append(file['title'])

		print(file['title'])
		print(f"Pulling file {file['title']}")
		print(f'Checking pulled file ', listDrive[0], ' ,is the same as pushed ', upload_file)
	else:
		pass

isFile=os.path.isfile('C:\\Users\\Veselin\\PycharmProjects\\driveUpload\\py_logo.png')
print(isFile)
if isFile:
	print('File exists in the folder py_logo.png')
	if listDrive[0] == upload_file:

		print('pulled ', listDrive[0])
		print('pushed ', upload_file)
