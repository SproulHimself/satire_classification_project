### [This README is under construction.]

* In the process of converting the presentation for this project from slideshow into a proper readme format.

* Thanks for your patience!


# The Satire Detector

<p align="center">
<img width="422"  src="https://user-images.githubusercontent.com/34200538/52924063-e6627080-32f8-11e9-93fa-fd333c8e0898.jpeg">
</p>


### Abstract

"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

---

### Motivation

This project was inspired by the vast amount of people whom spread satire as real news.


<p float="center">
  <img src="https://user-images.githubusercontent.com/34200538/52924503-17dc3b80-32fb-11e9-9272-bd4c9b4235a5.png" width="420" />

  <img src="https://user-images.githubusercontent.com/34200538/52924499-14e14b00-32fb-11e9-87e8-1f925a828c99.png" width="420" />
</p>

"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."




<!-- side by side image note comment here -->
<!-- <p float="left">
  <img src="/img1.png" width="100" />
  <img src="/img2.png" width="100" />
</p> -->



---

### Dataset
We had been told several times, acquiring and cleaning the data would take up the majority of our time on this project. At first, we tried not to believe the hype but ultimately the "data wrangling" process did take up a lot of our time.

Our initial goal was to scrape multiple sources to get 2500 articles for each target label of satire and not satire. Due to time constraints and the speed of our scrapers we had to settle for 1200 satire examples and 900 non satire examples.


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




### Modeling

Following the standard train test split, we chose to run Multinomial Naive Bayes and Random Forest classifiers. While we believe there is potential overfitting occurring, we were impressed with the base metrics we received.

<p align="center">
<img width="422"  src="https://user-images.githubusercontent.com/34200538/52919973-e7ce7180-32d5-11e9-9c69-105ea90a62d2.png">
</p>

(Image taken from slideshow presentation)


----
### Summary

Working on this project was very fun and informative. We built a simple command line interface to evaluate new articles. It was very satisfying to see the overwhelming majority of articles being correctly classified.

<img width="730" alt="cli_satire_detector" src="https://user-images.githubusercontent.com/34200538/52919484-f1a1a600-32d0-11e9-8e49-d5f6a4b3029c.png">

---

### Next Steps

The model almost always makes a correct prediction when testing on articles from "out in the wild." However, at this time our model almost always identifies sports articles as satire. We plan to bolster database with more data from other sources which will include getting non-satire sports articles to train on.

Also, although the irony is quite funny, our model usually predicts FOX News articles as satire (LOL). As hilarious as this is, a correct classification is the ultimate goal. In the near future, the goals for the project will be:



* Continue to improve the database for both target labels. Accuracy quality is of upmost importance.

* Build an interactive Google Chrome application to help internet surfers decipher between what is satire and what is not.
