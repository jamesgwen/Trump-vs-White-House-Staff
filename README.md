# Trump-vs-White-House-Staff (Ongong Project)

**Background**
At the beginning of the Trump presidency, much attention was paid to the president’s tweets. Known for aggressive and inflammatory tweets, President Trump became known quickly for his late-night twitter rants and reactionary responses to political enemies. Similar to many politicians, Donald Trump’s staff uploads official content to social media on his behalf. As Trumps tweets became more well known, many wondered if his staff was also engaging in posting aggressive tweets on the president’s behalf.<br />

This project aims to see if term frequency–inverse document frequency can accurately differentiate between tweets written by President Trump and his staff. At the beginning of the presidency, Donald Trump was known to use an Android phone while the majority of his staff were photographed with iPhones. Data from Twitter indicates on what type of phone a tweet was written. For the purpose of training the model, we will assume that tweets written on Android are written by Trump while those on iPhone are written by his staff. If the model can accurately predict what phone was used to write tweets in the test dataset, we can therefore logically conclude that Donald Trump is the sole writer of the more inflammatory content.<br />

**Quick Data Exploration**
Let's explore the tweets! From the wordcloud, we can see many of Trump's popular phrases such as Make America Great Again. We can also see many of Trump's talking points suchs as (crooked) Hillary Clinton, Bernie Sanders, and Ted Cruz. The prevelance of these words indicates that both Trump and his staff likely are consistent with the rhetoric stereotypical to Trump.<br />

![alt text](https://github.com/jamesgwen/Trump-vs-White-House-Staff/blob/main/wordcloud.png?raw=true)<br/>

Now let us look at the split between tweets written on Android and those on Apple.
![alt text](https://github.com/jamesgwen/Trump-vs-White-House-Staff/blob/main/tweet_histogram.png?raw=true)<br/>

From this graph, we can see that the majority of @realDonaldTrump tweets are written on Android. However, it is only a slight majority. A large number of tweets are written on Apple. This would indicate that either Donald Trump swtiches from Android to Apple to write his tweets or that his staff play an active role in keeping his account active.<br/> 

**Analysis**<br/>
*To see code, please look at the python script*<br/>
Now onto the analysis. For this project, I used term frequency–inverse document frequency (TF-IDF) to convert the tweets into data that would be agreeable for different methods. After getting the TF-IDF scores, I decided to compare logistic regression and Bernoulli naive Bayes classifer to see which would be better at classifying the tweets. These two methods are great for classifying binary variables. The idea here is that if either method can accurately determine on which phone a tweet was written, then the iPhone writters are different from the Android writers; put more simply, if either method can tell the difference between an Android tweet and an iPhone tweet, then we likely confirm that Donald Trump writes the tweets made on Android and his staff write the tweets made on iPhone.<br/> 

*Note: the label for Android was changed to Trump and the label for iPhone was changed to staff in the data*<br/>
*Logistic Regression*<br/>
![alt text](https://github.com/jamesgwen/Trump-vs-White-House-Staff/blob/main/logistic_regression.png?raw=true)<br/>

*Bernoulli naive Bayes*<br/>
![alt text](https://github.com/jamesgwen/Trump-vs-White-House-Staff/blob/main/Bernoulli%20naive%20Bayes.png?raw=true)<br/>
