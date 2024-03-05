import nltk
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from nltk.corpus import stopwords
nltk.download('stopwords') 
from collections import Counter
import re


def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    lowers = text.lower()
    no_punctuation = re.sub(r'[^\w\s]',' ',lowers)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

tokens = get_tokens()
# the lambda expression below this comment
# stores stopwords in a variable for eficiency: 
# it avoids retrieving them from ntlk for each iteration
sw = stopwords.words('english')
print(sw)
filtered = [w for w in tokens if not w in sw]
count = Counter(filtered)

print(count.most_common(10))
print(sum(count.values()))