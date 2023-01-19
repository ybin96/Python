from myutil.sist import makeWordCloud

# textFile = "./movie.txt"
# imgFile = "./r.png"
# font = "../Data/DoHyeon-Regular.ttf"
# stopWord = ["철기","주양","이동석"]
#
textFile = "../Data/speech_moon.txt"
imgFile = "./moon02.png"
font = "../Data/DoHyeon-Regular.ttf"
stopWord = ["국민","여러분","우리나라","대한민국","한국"]
mask = "./heart.png"

makeWordCloud(textFile, imgFile, stopWord, font, mask)
