import os
from pytube import YouTube
from converter import converter as conv

def downloader():

	yt = input('Εισαγωγή URL από YouTube: ')

	try:
		title = YouTube(yt).title
	except:
		flag = False
		print('Μη έγκυρο URL! Προσπαθήστε ξανά.')
		while (flag == False):
			try:
				yt = input('Εισαγωγή URL από YouTube: ')
				title = YouTube(yt).title
				flag = True
			except:
				print('Μη έγκυρο URL! Προσπαθήστε ξανά.')

	print(('Θελετε να κατεβάστε το {}; y/n').format(title))
	choice = input()

	if (choice == 'y'):

		try:
			try:
				dl_dir = input('Εισάγετε το path αποθήκευσης του βίντεο: ')
				YouTube(yt).streams.first().download(dl_dir)
			except:
				flag = False
				print('Μη έγκυρο path! Προσπαθήστε ξανά.')
				while (flag == False):
					try:
						dl_dir = input('Εισάγετε το path αποθήκευσης του βίντεο: ')
						YouTube(yt).streams.first().download(dl_dir)
						flag = True
					except:
						flag = False
						print('Μη έγκυρο path! Προσπαθήστε ξανά.')
		except:
			print('Κάτι πήγε στραβά στο κατέβασμα του βίντεο. Ξανατρέξτε το πρόγραμμα.')
			exit()

		print('Το βίντεο κατέβηκε. Θέλετε να το μετατρέψετε σε mp3; y/n')
		select = input()

		if (select == 'y'):

			try:
				mp3_dir = input('Εισάγετε το path αποθήκευσης του mp3 (ή αφήστε το κενό για να χρησιμοποιηθεί το ίδιο): ')
				if (mp3_dir == ''):
					mp3_dir = dl_dir
				elif not (os.path.isdir(mp3_dir)):
					raise Error
			except:
				print('Μη έγκυρο path! Προσπαθήστε ξανά.')
				flag = False
				while (flag == False):
					try:
						mp3_dir = input('Εισάγετε το path αποθήκευσης του mp3: (ή αφήστε το κενό για να χρησιμοποιηθεί το ίδιο): ')
						if (mp3_dir == ''):
							mp3_dir = dl_dir
						elif not (os.path.isdir(mp3_dir)):
							raise Error
						flag = True
					except:
						flag = False
						print('Μη έγκυρο path! Προσπαθήστε ξανά.')


			conv(title, 'mp4', 'mp3', mp3_dir)
		else:
			print('Τερματισμός προγράμματος.')

	else:
		print('Τερματισμός προγράμματος.')
		exit()


if __name__ == "__main__":
	downloader()
