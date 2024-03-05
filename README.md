# LAB 2

## Task 2.1: Getting Started with NLTK
### 2.1.1 Counts
The 10 most common words in FirstContactWithTensorFlow.txt are:
<br>[('the', 1343), (',', 1251), ('.', 810), (')', 638), ('(', 637), ('of', 586), ('to', 491), ('a', 470), (':', 454), ('in', 417)]
<br>The total number of words in the book are: **25187**

### 2.1.2 No punctuation counts
The 10 most common words in FirstContactWithTensorFlow.txt without punctuation are:
<br>[('the', 1445), ('of', 587), ('to', 532), ('in', 509), ('a', 496), ('and', 347), ('tf', 304), ('is', 289), ('we', 283), ('that', 276)]
<br>The total number of words in the book without punctuation are: **21661**

### 2.1.3 No punctuation and stop words counts
**Why "Tensorflow" is not the most frequent word?**
<br>Because words like determintants, preprositions and other are more recurrent. They are known as stop words, a set of commonly used words in a language.
<br>**Which are the Stop Words?**
<br>In this scenario, some of the stop words are 'the', 'of', 'to', 0in', 'a', 'and', 'is', 'we', 'that' and many more
<br>The 10 most common words in FirstContactWithTensorFlow.txt without punctuation and stop words are:
<br>[('tf', 304), ('tensorflow', 241), ('0', 241), ('1', 154), ('data', 121), ('tensor', 101), ('code', 90), ('learning', 86), ('dimension', 84), ('2', 80)]
<br>The total number of words in the book punctuation and stop words are: **13146**

## Task 2.3: Tweet pre-processing

In this section we aim to preprocess tweets based on a provided code by [Marco Bonzanini](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/). Nowadays, tweets are no longer plain text it also allows adding emojis, mentions, links... When preprocessing text to then do more complex task language detection or sentiment analysis, this must be taken into account. One of the most important steps in this preprocessing is word tokenisation as seen in the first section, which allows the proper separation of words, punctuation and links to present a better structured input to a model. Hence Marco Bonzanini's work allows the separation of those *special characters* properly like emojis, html tags an urls for example using regex, which are predefinition of character patterns.

## Task 2.4: Counter social
### 2.4.1 API selection
The API chosen is the first one. We have retreived some Tweets and saved them in a json file to preprocess them using the **nltk** library and the improvements of **Marco Bonzanini**


## Time and difficulties
Overall we have been working on the session for about 2 hours and a half. The main difficulties have been working with some packages of nltk. In the macOs environment I was getting an issue with the ssl certificate to download the different modules of nltk, so first I have tried to create local credentials, but it did not work. So finally I overpassed this situation creating an unverified context in the specific scripts where the specific modules of nltk like *punkt* or *stopwords* had to be downloaded.<br>
<br>On the other hand I could not work with **X** API, since I do not have an account, but it was easy to use one of the free versions provided. I have worked with API before, so retreiving the information with the code provided and store it in a JSON file was not a main difficulties.<br>
<br>Futhermore, I would like to add, that I founded very interesting the preprocessing part, since preprocessing tweets or other short social media message is a real challenge due to slang, usage of different languages and emojis, so the regex approach was very insighfull to ameliorate the tokenisation.