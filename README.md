# The Satire Detector


### Abstract


### Motivation

This project was inspired by the vast amount of people whom spread satire as real news.








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

(Image  taken from slideshow presentation)



----
### [This README is under construction.]

* I am in the process of converting my presentation for this project from slideshow into a proper readme format.

* Thanks for your patience!

<img width="730" alt="cli_satire_detector" src="https://user-images.githubusercontent.com/34200538/52919484-f1a1a600-32d0-11e9-8e49-d5f6a4b3029c.png">
