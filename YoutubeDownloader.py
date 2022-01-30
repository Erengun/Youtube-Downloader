#Youtube video downloader

#for starting again the program
def main():
	from pytube import YouTube

	#get the link from the user
	link = input("Enter the video link : ")

	#download the video
	yt = YouTube(link)
	print("Downloading : ",yt.title)
	mpx = input("Press 3 for mp3 \n Press 4 for mp4")
	if mpx == 3:
		#show mp3 itags
		print("Available mp3 itags : ")
		for i in yt.streams.filter(progressive=True, file_extension='mp3').all():
			print(i)
		#get the itag from the user
		itag = int(input("Enter the itag : "))
		#download the video
		if not itag in yt.streams.filter(progressive=True, file_extension='mp3').all():
			print("Invalid itag press 1 to try again \n press 2 to exit") 
			if itag == 1:
				main()
			exit()
		yt.streams.get_by_itag(itag).download()
	elif mpx == 4:
		#show mp4 itags
		print("Available mp4 itags : ")
		for i in yt.streams.filter(progressive=True, file_extension='mp4').all():
			print(i)
		#get the itag from the user
		itag = int(input("Enter the itag : "))
		#download the video
		yt.streams.get_by_itag(itag).download()
	else:
		print("Invalid Input")
		go = input("Press 1 to try again \n Press 2 to exit")
		if go == 1:
			main()
		else:
			exit()

if (__name__ == "__main__"):
    main()
