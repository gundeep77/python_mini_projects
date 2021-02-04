from wordcloud import WordCloud

sal = {}
lst = ['raja', 'guria', 'yash', 'ishu', 'ladi', 'naren', 'pritam', 'jaspal', 'diljeet', 'pannu', 'rohit', 'simran', 'sehej', 'dilip', 'pinky', 'rano', 'sweety', 'kamaljit', 'komal', 'vishu', 'gourav', 'sourabh', 'charan', 'kamal', 'anuja', 'priyanshu', 'rajan', 'harbhajan', 'niranjan', 'amit', 'sumit', 'surinder', 'ritu', 'anmol', 'aman', 'surjit', 'manu', 'palak', 'pallavi', 'satinder', 'harbans', 'guddi', 'manika']

for key in lst:
    sal[key] = 1

wc = WordCloud(
    background_color='white',     # #E0FFEE
    max_words=100,
    width=350,
    height = 350,
)

wc.fit_words(sal)
wc.to_file("salujas.jpg")
