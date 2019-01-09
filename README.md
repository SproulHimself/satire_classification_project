# mod3-project

Do we remove stop words, or not?
Do we stem or lemmatize our text data, or leave the words as is?
Is basic tokenization enough, or do we need to support special edge cases through the use of regex?
Do we use the entire vocabulary, or just limit the model to a subset of the most frequently used words? If so, how many?
Do we engineer other features, such as bigrams, or POS tags, or Mutual Information Scores?
What sort of vectorization should we use in our model? Boolean Vectorization? Count Vectorization? TF-IDF? More advanced vectorization strategies such as Word2Vec?


- bigrams for class -  mutual information score 
- lemmatization for improving score 
- top word frequency per class 

- check average length of each class of articles 
	- would adding length as a feature be interesting? 

- is there a way to determine strongest weighted words ? 
- grid search with random forest tweaks (graph accuracy varations)
- CLI - satire_tester 
	- run regex on the input to get ride of new lines and turn it into a string
	- use those helper functions 
	- create loop 
	- ascii art 

- slides for presentation 
	- rationale / question
	- data-preprocessing process - scraping masters 
	- EDA - Exploratory data Analysis 
	- First Models - results 
	- Changes 
	- Future plans / additions possible Chrome extension with the model 
		- get the "probability" something is satire (versus 1 or 0)
		(maybe that's already in there somewhere?)



"Leaders like Jonny Boucher, a Chicago native who, after losing too many friends and family to suicide, started a coffee shop to offer emotional support and guidance to those who might be in need of a little more than a strong cup of coffee to get through their day."



"Economic numbers looking REALLY good. Can you imagine if I had long term ZERO interest rates to play with like the past administration, rather than the rapidly raised normalized rates we have today. That would have been SO EASY! Still, markets up BIG since 2016 Election!"


"I hope you find inspiration in the stories of Dejah, Moussa, Sandor, Hong and Jonny. Their journeys began with a decision to build the better future they wanted to see. The same is true for you. What matters isn’t the size of the step you take; what matters is that you take it"

"President Trump’s greatest hurdle in persuading Americans that there is a national security crisis on the southwest border may well be his own credibility. Mr. Trump is using a rare currency — a prime-time address to the nation — to make the case for a border wall with Mexico, an issue that has forced a partial shutdown of the federal government. His penchant for superlatives — “the best,” “the worst,” “never,” “always,” and now, “crisis” — and his record of falsehoods, misstatements and exaggerations on the topic will likely be challenged as never before."

"The nation has been left disappointed by the state of cricket in the country once again today. This comes after cricketing legend Shane Warne called for a complete overhaul into the cricket system, rather than simply announcing that he would be coming out of retirement. His public calls for the inquiry followed ex-English Captain Michael Vaughan’s comments that the return of two players wouldn’t fix the nation’s problems. However, rather than simply stating that 3 returning players could fix the whole thing and sensationally announcing that he would be putting the creams back on, Warne instead asked that the way Australia’s cricketing system is geared up be completely overturned."