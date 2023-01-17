# copy-tweet

A twitter bot to automatically send out the same tweets as a target user. 
This program uses the python library, Tweepy, to interact with the Twitter API and <a href="https://www.deta.sh">deta.sh</a> to run the program on a set schedule.

## Setup

To use this program, you will need to make a new twitter account that will be tweeting out the copied tweets and enable it for developer access at <a href="https://developer.twitter.com">developer.twitter.com</a>. Generate your api keys, access tokens, and bearer token and copy and paste them into the appropriate variables in config.py. Next you will need to find the numeric ID of your twitter account and the target user. This can be done by pasting the @ into <a href="https://tweeterid.com">tweeterid.com</a>. Copy and paste the id #'s into the appropriate variables in config.py.

To run the program automatically you will need to set up an account on <a href="https://www.deta.sh">deta.sh</a> and install their CLI. A tutorial for installing the CLI can be found here <a href="https://docs.deta.sh/docs/micros/getting_started/">docs.deta.sh/getting_started</a>
Once the CLI is installed, you can configure a "cron job" to schedule the execution of the code on an interval. Run the following commands in your terminal to clone
this repo and configure the cron job.

```
git clone https://github.com/aleckondichook/copy-tweet
cd copy-tweet
deta new
deta cron set "5 minutes"
```

The actual interval is up to you and can be changed. Twitter allows for 500,000 tweets to be pulled a month under their normal API access. This program pulls 20 tweets each time it is run, with the potential to to send out 10 tweets if there have been that many tweeted since the last time the program was ran. With a 5 minute interval and 10 tweets sent out each time, only (30 * 12 * 24 * 30) = 259,200 of the 500,000 limit will be used. If only 1 tweet is sent out at a time,
an interval of 2 minutes could be used. (21 * 30 * 24 * 30) = 453,600.