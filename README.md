# The Satire Detector

This project was inspired by the vast amount of people whom spread satire as real news.








### Dataset
We had been told several times, acquiring and cleaning the data would take up the majority of our time on this project. At first, we tried not to believe the hype but ultimately the "data wrangling" process did take up a lot of our time.

Our initial goal was to scrape multiple sources to get 2500 articles for each target label of satire and not satire. Due to time constraints and the speed of our scrapers we had to settle for 1200 satire examples and 900 non satire examples.

--------

### Preprocessing
First, we started off by writing functions for each source to remove the body of the articles from all the other unwanted content like the author's name. There were several of these functions, so here is a general example:

<p align="center">
  <!-- <img width="422" alt="images/clean_art_example" src="https://user-images.githubusercontent.com/25883937/27927285-e2c9f80a-6250-11e7-9553-e8fdd427730e.png">  -->
</p>

<p align="center">
<img width="422"  src="https://github.com/SproulHimself/satire_classification_project/blob/master/images/clean_art_example_func.png">
</p>

Next, each article was tokenized with stop words and punctuation removed.

* IMAGE HERE


The final preprocessing step was to lemmatize the data using the WordNetLemmatizer() from the NLTK framework.

------
### Modeling

Following the standard train test split, we chose to run Multinomial Naive Bayes and Random Forest classifiers.



----
### [This README is under construction.]

* I am in the process of converting my presentation for this project from slideshow into a proper readme format.

* Thanks for your patience!
