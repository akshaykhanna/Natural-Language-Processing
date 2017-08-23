'''
Created on 15-Aug-2017

@author: Akshay Khanna
'''
#import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.corpus.reader import tagged
from __builtin__ import str
from operator import pos

def tokenizerNltk():
    from nltk.tokenize import sent_tokenize, word_tokenize

    text= "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
    
    print(sent_tokenize(text));
    print(word_tokenize(text));


def stopWordsNltk():
    from nltk.corpus import stopwords
    stopwordsSet= set(stopwords.words('english'))
    print 'Stopwords in NLTK lib:',stopwordsSet
    from nltk.tokenize import word_tokenize
    text = "This is a sample sentence, showing off the stop words filtration."
    print 'Example text:',text
    wordsInSent=word_tokenize(text);
    print 'Words in example text:',wordsInSent
    filtered_W=[w for w in wordsInSent if not w in stopwordsSet]
    print 'Words in example text after filtering stopwords',filtered_W
    print 'Sentence before removing stopwords: ', text
    sentAfterRemovingStopWords=''
    for w in filtered_W:
        sentAfterRemovingStopWords +=w+' ' 
    print 'Sentence after removing stopwords: ',sentAfterRemovingStopWords

   
def stemmingInNltk():
    from nltk.tokenize import word_tokenize
    text = "I am working for work day and night. I worked hard."
    #print 'Example text:',text
    wordsInSent=word_tokenize(text);
    from  nltk.stem import PorterStemmer
    ps=PorterStemmer()
    sentAfterStemming=''
    for w in wordsInSent:
        sentAfterStemming+= ps.stem(w)+" "
    print 'Sentence before stemming:', text
    print 'Sentence after stemming:', sentAfterStemming


def partsOfSpeech(): 
    from nltk.tokenize import PunktSentenceTokenizer, word_tokenize
    from nltk.corpus import state_union
    from nltk import pos_tag
    train_text = state_union.raw()
    sample_text = state_union.raw("2006-GWBush.txt")
    custom_sentence_tokenizer=PunktSentenceTokenizer(train_text)
    afterTokenizing= custom_sentence_tokenizer.tokenize(sample_text)
    try:
        for l in afterTokenizing:
            words=word_tokenize(l)
            tagged = pos_tag(words)
            print tagged
    except Exception as e:
        print str(e)
    pass

def partsOfSpeechSimple():
    import nltk 
    from nltk.tokenize import word_tokenize
    from nltk import pos_tag
    #print 'Part Of Speech (POS) tags:'
    text = "This is a sample sentence, an example to display words & there respective parts of speech in english."
    print 'text:',text
    try:
        words=word_tokenize(text)
        print 'words:',words
        tagged = pos_tag(words)
        print tagged
    except Exception as e:
        print str(e)
    pass
#tokenizerNltk()
#stopWordsNltk()
#stemmingInNltk()  
#partsOfSpeech()
partsOfSpeechSimple()
