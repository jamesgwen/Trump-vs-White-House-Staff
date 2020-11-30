# Trump-vs-White-House-Staff (Ongong Project)

At the beginning of the Trump presidency, much attention was paid to the president’s tweets. Known for aggressive and inflammatory tweets, President Trump became known quickly for his late-night twitter rants and reactionary responses to political enemies. Similar to many politicians, Donald Trump’s staff uploads official content to social media on his behalf. As Trumps tweets became more well known, many wondered if his staff was also engaging in posting aggressive tweets on the president’s behalf.<br />

This project aims to see if term frequency–inverse document frequency can accurately differentiate between tweets written by President Trump and his staff. At the beginning of the presidency, Donald Trump was known to use an Android phone while the majority of his staff were photographed with iPhones. Data from Twitter indicates on what type of phone a tweet was written. For the purpose of training the model, we will assume that tweets written on Android are written by Trump while those on iPhone are written by his staff. If the model can accurately predict what phone was used to write tweets in the test dataset, we can therefore logically conclude that Donald Trump is the sole writer of the more inflammatory content.<br />

Let's explore the tweets! From the wordcloud, we can see many of Trump's popular phrases such as Make America Great Again. We can also see many of Trump's talking points suchs as (crooked) Hillary Clinton, Bernie Sanders, and Ted Cruz. The prevelance of these words indicates that both Trump and his staff likely are consistent with the rhetoric stereotypical to Trump.<br />

![alt text](https://github.com/jamesgwen/Trump-vs-White-House-Staff/blob/main/wordcloud.png?raw=true)<br/>
