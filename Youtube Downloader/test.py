import pafy

def download_with_pafy(url):
	# create instant
	video = pafy.new(url)

	# get tile
	title = video.title
	print(title)

	# get rating
	# rating = video.rating
	# print(rating)

	# get viewount
	# views = video.viewcount
	# print(views)

	# get author
	author = video.author
	print(author)

	# get length
	# length = video.length
	# print(length)

	# get duration, likes, dislikes & description
	duration = video.duration
	print(duration)

	# get file size
	vid = video.getbest()

	size = vid.get_filesize()
	print(size)


	# get likes
	# likes = video.likes
	# print(likes)

	# get dislikes
	# dislikes = video.dislikes
	# print(dislikes)

	# get description
	# desription = video.description
	# print(description)


if __name__ == '__main__':
	download_with_pafy("https://www.youtube.com/watch?v=7sQ59A9EdZ4")