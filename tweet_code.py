import nltk

#This tweet was posted by @analyticbridge
tweet="10 types of regressions for #DataScientists, #Statisticians and other #Analytic practitioners, which one to use? http://ow.ly/zsvs4"
 
tokens = nltk.word_tokenize(tweet)
 
tokens

#['10', 'types', 'of', 'regressions', 'for', '#', 'DataScientists', ',', '#', 'Statisticians', 'and', 'other', '#', 'Analytic', 'practitioners', ',', 'which', 'one', 'to', 'use', '?', 'http', ':', '//ow.ly/zsvs4']
 
#nltk.pos_tag processes the tweet text and attaches a tag to each word, e.g. CD: cardinal numbers, NNS: plural nouns, NNP: singular nouns, etc.
 
tagged = nltk.pos_tag(tokens)
 
tagged
#[('10', 'CD'), ('types', 'NNS'), ('of', 'IN'), ('regressions', 'NNS'), ('for', 'IN'), ('#', '#'), ('DataScientists', 'NNS'), (',', ','), ('#', '#'), ('Statisticians', 'NNS'), ('and', 'CC'), ('other', 'JJ'), ('#', '#'), ('Analytic', 'NNP'), ('practitioners', 'NNS'), (',', ','), ('which', 'WDT'), ('one', 'CD'), ('to', 'TO'), ('use', 'VB'), ('?', '.'), ('http', 'NN'), (':', ':'), ('//ow.ly/zsvs4', '-NONE-')]
 
#Nouns can be printed using the tag information and functions from the regular expression package (https://docs.python.org/2/library/re.html).
 
import re
for i in range(0,len(tagged)):
     if re.match('N',tagged[i][1]):
             print (tagged[i][0])
 
#Output
##types
##regressions
##DataScientists
##Statisticians
##Analytic
##practitioners
##http
