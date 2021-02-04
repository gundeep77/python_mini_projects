from wordcloud import WordCloud

roomies = {}

word_set = {'prashant', 'prashu', 'chhotu', 'nachi', 'nachirandi', 'shahin', 'bhaijaan', 'chcha', 'prateek', 'gotu', 'gundeep', 'bhaalu', 'gunnu', 'yala', 'slow', 'mechanical', 'CSE', 'electronics', 'dota', 'sandwich', 'artbiz', 'dramatics', 'toastmasters', 'badminton', 'football', 'basketball', 'VIT', 'limra', 'tara-ma', 'hart-lounge', 'counter-strike', 'AOE', 'chal-ab-nikal', 'ASME', 'ronaldo', 'suits', 'prison-break', 'GOT', 'arrow', 'flash', 'guitar', 'ASP', 'swagat', 'pondi', 'akhhhmad', 'pool', 'yalapanti', 'transformers', 'cube-ka-wajood'}


for key in word_set:
    roomies[key] = 1

wc = WordCloud(
    background_color='#E0FFEE',
    max_words=100,
    width=1000,
    height = 1000,
)

wc.fit_words(roomies)
wc.to_file("L123.jpg")