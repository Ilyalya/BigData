from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import StringIO
import pandas as pd

languages = ["JavaScript", "Python", "Java", "PHP", "C#", "C++", "Ruby", "CSS", "TypeScript", "C", "Swift", "Objective-C", "Scala", "R",
             "Go", "Shell", "PowerShell", "Perl", "Kotlin", "Haskell", "Matlab", "SQL", "Rust", "TypeScript", "Node.js", "Pascal","Groovy", "D","Assembler", "PL/SQL", "Vue.js"]
info = pd.read_csv('dataset.csv', sep='\t', encoding='utf-8')

list_category = info['category']
print(list_category)

info['category'] = info['category'].map(lambda x: x.replace('+1ещё', ''))
info['category'] = info['category'].map(lambda x: x.replace('+2ещё', ''))
info['category'] = info['category'].map(lambda x: x.replace('+3ещё', ''))
info['category'] = info['category'].map(lambda x: x.replace('+4ещё', ''))
print(info['category'])

spisok = ', '.join(list(info['category']))
print(spisok)
for i in range(len(info)):
    for j in range(len(languages)):
        if languages[j] == info['category'][i]:
            print(languages[j], info['category'][i])
        else:
            k = info.drop([i])

print(k)

# def popular_language(spisok):
#     spam_wc = WordCloud(width = 512,height = 512).generate(spisok)
#     plt.figure(figsize = (10, 8), facecolor = 'k')
#     plt.imshow(spam_wc)
#     plt.axis('off')
#     plt.tight_layout(pad = 0)
#     plt.show()
#
# popular_language(spisok)

