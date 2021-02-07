from PIL import Image
from wordcloud import WordCloud, STOPWORDS

with open("input_text.txt", "r") as f:      # taking input words through a text file
    inp = f.read()

stopwords = STOPWORDS
more_stopwords = ['lets', 'said', 'although', 'course', 'purpose', 'companies', 'publish', 'much']
for word in more_stopwords:
    stopwords.add(word)

wc = WordCloud(
    background_color='#E0FFEE',     # #E0FFEE(light blue)
    max_words=200,
    stopwords=stopwords,
    width=2000,
    height=1000
)

wc.generate(inp)
wc.to_file("my_cloud.jpg")
