
#A simple rectangular word cloud using a cancer dataset from kaggle

from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'PAM50_proteins.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)



plt.imshow(wordcloud)
plt.axis("off")


wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
