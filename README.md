# copy_tweet

A program to automatically send out the same tweets as another user.
This program uses tweepy, a python library that interacts with the Twitter API, and deta.sh to run the program on a set schedule.

To use this program, first clone this repository and make a new twitter account that will be tweeting out the copied tweets and enable it for developer access at https://developer.twitter.com.
Generate your api keys, access tokens, and bearer token and copy and paste them into the appropriate variables in config.py. Next you will need to find the numeric ID
of your twitter account and the account that you will be copying the tweets of. This can be done by pasting the @ into https://tweeterid.com. 
Copy and paste the id #'s into the appropriate variables in config.py. The program itself is now set up and can be run from your IDE.

To run the program automatically you will need to set up an account on deta.sh and install their CLI. A tutorial for installing the CLI can be found here https://docs.deta.sh/docs/micros/getting_started/
Once the CLI is installed, you can configure a "cron job" to schedule the execution of the code on an interval. Open a terminal and cd into the copy_tweet folder. Run the following commands.

'deta new'

'deta cron set "5 minutes"'

The actual interval is up to you and can be changed, just make sure to include the interval within quotation marks. Twitter allows for 500,000 tweets to be pulled a month under their normal API access. This program pulls 20 tweets each time it is run,
with the potential to to send out 10 tweets if there have been that many tweeted since the last time the program was ran. With a 5 minute interval and 10 tweets sent out each time, only (30 * 12 * 24 * 30) = 259,200 of the 500,000 limit will be used. If only 1 tweet is sent out at a time,
an interval of 2 minutes could be used. (21 * 30 * 24 * 30) = 453,600.

Thank you for reading and I hope you enjoy creating a twitter bot for any helpful or mischievous reasons. Please reach out to me on twitter (@0xgeeb) if you have any issues with the program.
