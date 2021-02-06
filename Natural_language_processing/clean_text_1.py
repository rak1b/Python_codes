import string
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import style
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
read_text= open('read.txt',encoding='utf-8').read()
# emotion_text = open('emotion.txt').read()


"""
learning translate,and maketrans
translate take table,which made by maketrans
and translate,changes into our english format
_________________________________________
Maketrans makes table
first check maketrans with one argument
dict = {'A':'1','B':'2'}
print(str.maketrans(dict))
result:{65: '1', 66: '2'}

next check maketrans with two argument
a = 'abcde'
b = '12345'
print(str.maketrans(a,b))
result:{97: 49, 98: 50, 99: 51, 100: 52, 101: 53}

next check maketrans with three argument
a = 'abcde%$'
b = '1234534'
c = '%$!'
print(str.maketrans(a,b,c))
result:{97: 49, 98: 50, 99: 51, 100: 52, 101: 53, 37: None, 36: None}
d = read_text.translate(str.maketrans(a,b,c))
print(d)
result:H5r5's 1r5 som5 TEXT

removed special char if there,and chng the values
"""



lower_text = read_text.lower()
print(lower_text)
print(string.punctuation)
cleaned_data_step_1 = lower_text.translate(str.maketrans('','',string.punctuation))


# Stop Words means these are not necessary for sentiment analysis
# stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
#               "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
#               "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
#               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
#               "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
#               "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
#               "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
#               "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
#               "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
#               "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
#
#
# cleaned_data_step_2 = cleaned_data_step_1.split()
# split is slow,we will use word_tokenize()
cleaned_data_step_2 = word_tokenize(cleaned_data_step_1,'english')
stop_words = stopwords.words('english')
cleaned_data_step_final = []
for mydata in cleaned_data_step_2:
    if mydata not in stop_words:
        cleaned_data_step_final.append(mydata)


emotion_list_after_filter = []
with open("emotion.txt") as emotion_text :
    for line in emotion_text:
        clean_emotion_line = line.translate(str.maketrans('','',"', \n"))
        word,emotion = clean_emotion_line.split(':')
        for clean_word in cleaned_data_step_final:
            if word == clean_word:
                emotion_list_after_filter.append(word)


emo_count = Counter(emotion_list_after_filter)
print(emo_count)
style.use('ggplot')
fig,axis = plt.subplots()
axis.bar(emo_count.keys(),emo_count.values())
plt.savefig('graph.png')
fig.autofmt_xdate()
plt.ylabel('Amounts')
plt.xlabel('Words')
plt.title('Sentimental Analysis')
# plt.xticks(rotation = 45)
plt.show()
