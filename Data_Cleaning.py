# %% 
'''
READ ME:

The purpose of this file is to clean the raw data containing Donald Trump's tweets.
'''

#%%
## IMPORT PACAGES
import pandas as pd
import matplotlib.pyplot as plot 

data_folder = '~/Downloads/Python_Projects/Trump/Data/'

#%%
## LOAD RAW DATA
raw_data = pd.read_csv(data_folder + 'Raw_Data.csv', sep=',', encoding='latin-1')
#%%
# %%
## CLEAN RAW DATA

data = raw_data[['text', 'statusSource']] # select column with text and phone source

# define function to label source based on statusSource column
def phone_type(row):
    if 'Twitter for Android' in row['statusSource']:
        return 'Android'
    elif 'Twitter for iPhone' in row['statusSource']:
        return 'Apple'
    else: return 'other'

# apply function
data['source'] = data.apply(lambda row: phone_type(row), axis = 1)

# get rid of tweets not made on iphone or android
data = data[data.source != 'other']
#%%
plot.hist(data['source'])
plot.title('Tweet Source', y = 1)
#plot.xlabel('1 = Malignant, 0 = Benign')
plot.ylabel('Frequency')
fig = plot.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('tweet_histogram.png', dpi=100)
plot.show()
# %%
data2 = data[['text', 'source']]

# %%
# remove meaningless characters
# %%
#data
# %%
trash = ['!', '@', '#', 
    '$', '%', '^', '&', '*', '(', ')',
     '\n', 'http', 'www.', '.org', '.com', '.gov', '.',
     ',', ':', '/','"', '-', '=', '+', '_']

for item in trash:
    data2['text'] = data2['text'].str.replace(item, '')   

data2['text'] = data2["text"].str.lower()

#%%
# def writer(row):
#     if row['source'] == 'Android':
#         return 'Trump'
#     else: return 'Staff'

# %%

#data2['writer'] = data2.apply(lambda row: writer(row), axis = 1)
    
#data2 = data2[['text', 'source']]
# %%
data2.to_csv(data_folder + 'clean_data.csv', index = False)
# %%
data2
# %%
