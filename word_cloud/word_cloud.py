from PIL import Image
from wordcloud import WordCloud, STOPWORDS

with open("input_text.txt", "r") as f:
    inp = f.read()

# background = np.array(Image.open("galaxy.jpg"))
stopwords = STOPWORDS
more_stopwords = ['lets', 'said', 'although', 'course', 'purpose', 'companies', 'publish', 'much']
for word in more_stopwords:
    stopwords.add(word)

wc = WordCloud(
    background_color='#E0FFEE',     # #E0FFEE(light blue)
    max_words=200,
    stopwords=stopwords,
    # mask=background
    width=2000,
    height=1000
)

wc.generate(inp)
wc.to_file("my_cloud.jpg")
