from wordcloud import WordCloud

dota_dict = {}

word_set = {'silencer', 'farm', 'arpit', 'hookNow', 'bootySeeker', 'ghusAndar', 'botChal', 'gank', 'NOOB', 'gankKarlo', 'gundeep', 'void', 'pushKar', 'meMid', 'sahiBataRahaHu', 'chutiyaBounty', 'akshat', 'bobo', 'enigma', 'hawk', 'slark', 'ulti', 'yala', 'teriMaa', 'hawkChut', 'sniper', 'support', 'noobArcana', 'butcher', 'pudge', 'rikiChut', 'bihari', 'hellblazer', 'PRO', 'jungle', 'topAaja', 'megaCreeps', 'daman', 'riki', 'nightcrawler', 'ohBhai'}

for key in word_set:
    dota_dict[key] = 1

wc = WordCloud(
    background_color='#E0FFEE',
    max_words=100,
    width=1000,
    height = 1000,
)

wc.fit_words(dota_dict)
wc.to_file("dota.jpg")
