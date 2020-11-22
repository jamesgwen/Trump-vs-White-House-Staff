#%%
## IMPORT PACAGES
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
data_folder = '~/Downloads/Python_Projects/Trump/Data/'
#%%
data = pd.read_csv(data_folder + 'clean_data.csv', sep=',', encoding='latin-1')
#%%
x_train, x_test, y_train, y_test = train_test_split(data['text'], data['writer'], test_size = 0.2, random_state = 42, stratify = data['writer'])
# %%

vector = TfidfVectorizer(stop_words = 'english', ngram_range=(1, 3), min_df = .05, max_df=.95)

vector.fit(x_train)
# %%
train = pd.DataFrame(vector.transform(x_train).todense(), columns = vector.get_feature_names())
test = pd.DataFrame(vector.transform(x_test).todense(), columns = vector.get_feature_names())
#%%
## LOGISTIC REGRESSION METHOD
reg = LogisticRegression()

reg.fit(train, y_train)

#reg.score(train, y_train)

probable_author = reg.predict(test) 
test_score = reg.score(test, y_test)

confusion_matrix(y_test, probable_author)
# %%
print ("Classifiction Matrix Logistic Regression: ")
print
print(classification_report(y_test, probable_author))
print
print("test score: " + str(test_score))

# %%
bernoulli = BernoulliNB()

bernoulli.fit(train, y_train)

bernoulli_predict = bernoulli.predict(test)
bernoulli_score = bernoulli.score(test, y_test)

confusion_matrix(y_test, bernoulli_predict)

print ("Classifiction Matrix Bernoulli: ")
print
print(classification_report(y_test, bernoulli_predict))
print
print("test score: " + str(bernoulli_score))
