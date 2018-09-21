# Reddit-Scraper

Uses Reddit's API and Python's request library to access data from a specified subreddit.

The first part of the code authorizes the request with OAuth2, which is mandatory by Reddit. 
The second part then uses the request library to recieve POST data via json format.

An example is shown below where the titles from 325 posts were collected from r/trendingsubreddits and 
printed to the console. 

![image](https://user-images.githubusercontent.com/29133645/45891104-4c6abc00-bd8a-11e8-8506-19d3d3108307.png)

The script could easily be changed to print other information as well as specified
in the following link : https://github.com/reddit-archive/reddit/wiki/JSON
