##Reddit's Trending Subreddit Collector
##-------------------------------------
##
##Collects 325 posts from Reddit's Trending Subreddit page
##and stores the data from each post in an array
##
##Created  20 August 2018
##by Joe Bille


import requests
import requests.auth
import json

#############################################################################################################
### AUTHORIZE WITH OAUTH2 -- not yet enforced by Reddit, but encouraged

user_agent = 'test-script v1.0 by /u/jbille29'                                                                          # Reddit wants a unique identifier

client_auth = requests.auth.HTTPBasicAuth('gpNREKNvXQ9kHw', 'U_MyXU1WentHgXWMqTmtrZsy2ag')                              #'client_id','client_secret'

post_data = {'grant_type': 'password', 'username': 'jbille29', 'password': '192917aW$'}                                 # grant_type : 'password' is fine for script apps

headers = {'User-agent': user_agent}

## Request access token
response = requests.post('https://www.reddit.com/api/v1/access_token', auth=client_auth, data=post_data, headers=headers)

## Extract access token and token type to make authorized request
token_type = response.json()['token_type']
access_token = response.json()['access_token']

#############################################################################################################
### DATA AQUISITION

## Add new token data to header
headers = {"Authorization": token_type + " " + access_token, "User-Agent": user_agent}

posts_num = 324                                 # set to 324 because the request limit gives me an extra post
after_value = 'null'
request_limit = '100'                           # initially set request limit to max value: 100
trending = []                                   # an array to hold the information from Reddit
    
i = 0                                           # counter to keep track of number of posts collected
while i <= posts_num:

    ## Make an authorized request
    r = requests.get('https://oauth.reddit.com/r/trendingsubreddits/.json?limit='+request_limit+'&after='+after_value,headers = headers)

    ## Store the 'after' value for pagination
    after_value = r.json()['data']['after']
    
    ## Store posts information in an array
    for post in r.json()['data']['children']:
        trending.append(post['data'])
        i += 1
 
    if posts_num - i > 100:                     # if the number of posts stored is greater than 100
        request_limit = '100'                   # set request limit to max value: 100
    else:
        request_limit = str(posts_num - i)      # or set request limit to number of posts left to collect


#############################################################################################################
### EXAMPLE

## Uncomment to print results to the screen     
for post in trending:
    print(post['title'])                       # Change the title to 'url' to access the link associated with the post, or see my email for further information that can be collected.
                                                # To access all the data from all the posts use print(post)
print(len(trending))                           # number of posts collected

