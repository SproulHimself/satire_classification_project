# The Satire Detector

<p align="center">
<img width="422"  src="https://user-images.githubusercontent.com/34200538/52924063-e6627080-32f8-11e9-93fa-fd333c8e0898.jpeg">
</p>


> We live in the golden age of satire. It’s almost to the point where we seem to conduct as much of our political conversation through humor as through the normal media. 
- Malcom Gladwell, in [The Satire Paradox](http://revisionisthistory.com/episodes/10-the-satire-paradox)

### Abstract

With the rise of "fake news" and the increasing discourse about the means to manage the spread of misinformation, we wanted to take a slice of that category and see if we could train a model to reasonably predict whether a news item was satirical or not. Even humans can have a hard time determining whether or not an article is satirical. 

In this project, we scraped and cleaned a data set of news articles labelled as satirical or not satirical. We used Natural Language Processing and Machine Learning techniques to create a model that was reasonably accurate in predicting whether or not an article was satirical. 

Our next steps include improvements to our data set, and potential a Chrome extension that can classify an article on a page with our satire ranking. 

---

### Motivation

This project was inspired by some high profile instances of legitimate organizations spreading satire as real news. 

In 2012, The Onion ran [a piece](https://www.cnn.com/2012/11/27/world/asia/north-korea-china-onion/index.html) that declared North Korean leader Kim Jong Un the "sexiest man alive." The China's People's Daily Online took it seriously and ran it as a serious story. More recently, in March of 2017, a [satirical item](https://www.newyorker.com/humor/borowitz-report/trump-orders-all-white-house-phones-covered-in-tin-foil) by New Yorker write Andy Borowitz said that Trump had ordered the phones at the White House to be covered with tin foil. The satirical piece was picked up by was picked up online and in print by China’s Reference News, which is published by the state-run Xinhua news agency.  

In an age where real news can test the credulity of reasonable readers, it can be increasingly hard to see the difference between satire and fact. So we were concerned that our model might not be effective. 


<p align="center">
  <img src="https://user-images.githubusercontent.com/34200538/52924503-17dc3b80-32fb-11e9-9272-bd4c9b4235a5.png" width="425" />

  <img src="https://user-images.githubusercontent.com/34200538/52924499-14e14b00-32fb-11e9-87e8-1f925a828c99.png" width="425" />
</p>


<!-- side by side image note comment here -->
<!-- <p float="left">
  <img src="/img1.png" width="100" />
  <img src="/img2.png" width="100" />
</p> -->



---

### Data Set
We had been told several times that acquiring and cleaning the data would take up the majority of our time on this project. At first, we tried not to believe the hype but ultimately the "data wrangling" process turned out to be rather time consuming. 

Our initial goal was to scrape multiple sources to get 2500 articles for each target label of satire and not satire. Due to time constraints and the speed of our scrapers we had to settle for 1200 satire examples and 900 non-satire examples.

--------

### Preprocessing
First, we started off by writing functions for each source to remove the body of the articles from all the other unwanted content like the author's name. There were several of these functions, so here is a general example:


<p align="center">
<img width="422"  src="https://user-images.githubusercontent.com/34200538/52919478-e189c680-32d0-11e9-897d-40a0969de351.png">
</p>

Next, each article was tokenized with stop words and punctuation removed.

<p align="center">
<img width="822"  src="https://user-images.githubusercontent.com/34200538/52919468-cdde6000-32d0-11e9-87ec-b65978c5321d.png">
</p>

The final preprocessing step was to lemmatize the data using the WordNetLemmatizer() from the NLTK framework.

------

### Visualizing The Dataset

**Dimensionality reduction using truncated SVD,
aka: latent semantic analysis (LSA).**

This transformer performs linear dimensionality reduction by means of truncated singular value decomposition (SVD). Contrary to principal component analysis (PCA), this estimator does not center the data before computing the singular value decomposition. This means it can work with scipy.sparse matrices efficiently.


Here is a **stationary** 3D graph of the vectorized dataset using TruncatedSVD:

<p align="center">
<img width="822"  src="https://user-images.githubusercontent.com/34200538/52926449-cab09780-3303-11e9-9af8-539f32e87c13.png">
</p>


Here is an **animated** 3D graph of the vectorized dataset using TruncatedSVD:

<p align="center">
<img width="822"  src="https://thumbs.gfycat.com/AgileHomelyHake.webp">
</p>



------




### Modeling

Following the standard train test split, we chose to run Multinomial Naive Bayes and Random Forest classifiers. While we believe there is potential overfitting occurring, we were impressed with the base metrics we received.

<p align="center">
<img width="422"  src="https://user-images.githubusercontent.com/34200538/52919973-e7ce7180-32d5-11e9-9c69-105ea90a62d2.png">
</p>

<!-- (Image taken from slideshow presentation) -->

<!-- #### [ GRIDSEARCH & TPOT METRICS COMING SOON ] -->

----
### Summary

Working on this project was a great real-world application of complex natural language processing techniques.  

We built a simple command line interface to evaluate new articles and were satisfied to see that the majority of our articles were correctly classified. Interestingly, articles from a Reddit thread [nottheonion](https://www.reddit.com/r/nottheonion/) were mostly classified as real news, but it misclassified many as satirical. But with headlines like, "National Weather Service Issues ‘Small Dog Warning’ Due to High Winds", you can't blame our model for lower performance on these types of articles.  

<p align="center">
<img width="730" alt="cli_satire_detector" src="https://user-images.githubusercontent.com/34200538/52970612-6da7f680-3382-11e9-8791-b241954b7e51.png">
</p>

---

### Next Steps

The model almost always makes a correct prediction when testing on articles from "the wild." However, at this time our model almost always identifies sports articles as satire. We plan to bolster database with more data from other sources which will include getting non-satire sports articles to train on.

Also, although the irony is quite funny, our model usually predicts FOX News articles as satire (lolz). As hilarious as this is, a correct classification is the ultimate goal. In the near future, the goals for the project will be:

* Continue to improve the data set for both target labels. Accuracy quality is of upmost importance.

* Build an interactive Google Chrome application to help internet surfers decipher between what is satire and what is not.
