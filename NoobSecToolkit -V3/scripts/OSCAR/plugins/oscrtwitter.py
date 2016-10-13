#!/usr/bin/python
# -*- coding: utf-8 -*-

# import sqlite3 for DB operations

import itertools
try:
    import sqlite3 as db
except:
    print "[+]ERROR: could not import sqlite3. You won't be able to add users to a sqliteDB!"
    pass

try:
    import tweepy
    from tweepy import *
    from tweepy.streaming import *
except:
    print '[+]ERROR: Unable to import the tweepy library installed!!'
    print 'You will not be able to use the twitter collection side of oscar!'

import sys
import thread
import os

def hist_tweet(t_api):
    con = ''
    try:
        while con != 'n' or con != 'N' or con != 'No' or con != 'no':
            try:
                num_tweets = input('How many tweets (200 maximum): ')
            except NameError:
                print "[+]ERROR: must be a number value!"
                return
            targetUsr = raw_input('Enter target user: ')
            user = t_api.get_user(targetUsr)
            print '\n'
            print 'Username: ', user.screen_name
            print 'Follower count: ', user.followers_count
            print '\n'
            target_tweets = t_api.user_timeline(targetUsr,count=num_tweets)
            counter = 0
            for tweet in target_tweets:
                counter += 1
                print counter, '-', tweet.text
            con = raw_input('Run again?(y/n): ')
            if con == 'no' or con == 'n' or con == 'N' or con == 'No':
                return
    except KeyboardInterrupt:
        return


# streaming class for the tweepy lib

def lv_stream(t_auth):

  # ask for the specified filter. Supports standard string. Hashtags too :P

    filt = raw_input('Enter filter option: ')

    class listen(StreamListener):

        def on_status(self, status):
            try:

        # print the status....use utf, or else.

                print status.author.screen_name.encode('utf-8') + ': ' \
                    + status.text.encode('utf-8')
                print '\n'
                saveFile = open('STREAM_%s.csv' % filt, 'a')
                saveFile.write(str(time.ctime()) + ',,'+ status.author.screen_name.encode('utf-8') +',,' + status.text.encode('utf-8'))
                saveFile.write('\n')
                saveFile.close()
                return True
            except (BaseException, KeyboardInterrupt, SystemExit):
                #print 'failed on data, ', str(e)
                sleep(3)
                return

        def on_error(self, status):
            return

    twitterStream = Stream(t_auth, listen())
    twitterStream.filter(track=[filt])


def lv_streamno(t_auth):

  # ask for the specified filter. Supports standard string. Hashtags too :P

    filt = raw_input('Enter filter option: ')

    class listen(StreamListener):

        def on_status(self, status):
            try:

        # print the status....use utf, or else.

                print status.author.screen_name.encode('utf-8') + ': ' \
                    + status.text.encode('utf-8')
                print '\n'
                return True
            except (BaseException, KeyboardInterrupt, SystemExit):
                #print 'failed on data, ', str(e)
                sleep(3)
                return

        def on_error(self, status):
            return

    twitterStream = Stream(t_auth, listen())
    twitterStream.filter(track=[filt])


# This can get confusing. Friends are people that are mutual followers.
# That is, those users who target follows and is followed by

def rcntFllw(t_api):
    targetUsr = raw_input('Enter target user: ')
    user = t_api.get_user(targetUsr)
    for friend in user.friends():
        print friend.screen_name
    print '\n'
    return


def rcntFllwrs(t_api):
    targetUsr = raw_input('Enter target user: ')
    user = t_api.get_user(targetUsr)
    for friends in user.followers(count=100):
        print friends.screen_name
    print '\n'
    return


def mentionCount(t_api):
    names = []
    print """
    1. Retrieve details
    2. Count specific mentions
  """
    opt = raw_input('Enter an option: ')
    if opt == '1':
        targetUsr = raw_input('Please enter a username: ')
        user = t_api.get_user(targetUsr)
        # 200 is the api limit per query currently?
        target_tweets = t_api.user_timeline(targetUsr, count=200)
        saveFile = open('tweets.txt', 'a')
        for tweet in target_tweets:

      # print tweet.text

            saveFile.write(tweet.text.encode('utf-8'))
            saveFile.write('\n')
        saveFile.close()
        mentionCount(api)
    if opt == '2':
        try:
            tweetedUsrs = open('tweets.txt').read().splitlines()
        except:
            print 'There was an error opening the tweets file.',
            print 'Did you run the first option?'
            return

        for lines in tweetedUsrs:
            tos = re.findall('@([A-Za-z0-9_]{1,15})', lines)
            for twitUsr in tos:
                names.append(twitUsr)
        while True:
            try:
                targetUsr2 = \
                    raw_input('Enter a twitter handle (without the @)'
                              'Ctrl+C to return: ')
                print 'Number of times mentioned: ', \
                    names.count(targetUsr2)
            except KeyboardInterrupt:
                print '\n'
                return


  # twitMenu()

def twitSearch(t_api):
    t_query = raw_input('Enter search: ')
    t_res = tweepy.Cursor(t_api.search, q=t_query, count=10,
                          result='recent',
                          include_entities=True).items()
    while True:
        try:
            tweet = t_res.next()
            print tweet.user.screen_name.encode('utf-8'), ':', \
                tweet.created_at, ':', tweet.text.encode('utf-8')
            print   # print an extra line...just for readability
            sleep(5)  # sleep so it is human readable
        except tweepy.TweepError:

      # if tweepy encounters an error, sleep for fifteen minutes..this will
      # help against API bans.

            sleep(60 * 15)
        except KeyboardInterrupt:
            return

def twitdelete(t_api, stat):
    try:
        t_api.destroy_status(stat)
        print "Deleted:", stat
    except:
        print "Failed to delete:", stat

"""Copied from https://gist.github.com/davej/113241 <- credit where credit is due"""
def batch_delete(t_api):
    print "You are about to Delete all tweets from the account @%s." % t_api.verify_credentials().screen_name
    print "Does this sound ok? There is no undo! Type yes to carry out this action."
    do_delete = raw_input("> ")
    if do_delete.lower() == 'yes':
        for status in tweepy.Cursor(t_api.user_timeline).items():
            try:
                #t_api.destroy_status(status.id)
                thread.start_new_thread(twitdelete, (t_api, status.id,))
                #print "Deleted:", status.id
            except:
                print "Failed to delete:", status.id
            sleep(.5)
    return

def dm_batch(t_api):
    print "You are about to Delete all RECEIEVED DMs from the account @%s." % t_api.verify_credentials().screen_name
    print "Does this sound ok? There is no undo! Type yes to carry out this action."
    do_delete = raw_input("> ")
    if do_delete.lower() == 'yes':
        direct_messages = tweepy.Cursor(t_api.direct_messages).items()
        for direct_message in itertools.islice(direct_messages,0,None):
        #for message in tweepy.Cursor(t_api.direct_messages).items():
            try:
                #t_api.destroy_direct_message(message.id)
                t_api.destroy_direct_message(direct_message.id)
                print "Deleted:", direct_message.id
            except:
                print "Failed to delete:", direct_message.id
            sleep(5)
    return

def dm_sent(t_api):
    print "You are about to Delete all SENT DMs from the account @%s." % t_api.verify_credentials().screen_name
    print "Does this sound ok? There is no undo! Type yes to carry out this action."
    do_delete = raw_input("> ")
    if do_delete.lower() == 'yes':
        sent_direct_messages = tweepy.Cursor(t_api.sent_direct_messages).items()
        for direct_message in itertools.islice(sent_direct_messages,0,None):
        #for message in tweepy.Cursor(t_api.direct_messages).items():
            try:
                #t_api.destroy_direct_message(message.id)
                t_api.destroy_direct_message(direct_message.id)
                print "Deleted:", direct_message.id
            except:
                print "Failed to delete:", direct_message.id
            sleep(5)
    return

"""
def fdelete(t_api, stat):
    try:
        t_api.destroy_favorite(stat)
        print "Deleted:", stat
    except:
        print "Failed to delete:", stat
"""

def favdelete(t_api):
    print "You are about to Delete all favorites from the account @%s." % t_api.verify_credentials().screen_name
    print "Does this sound ok? There is no undo! Type yes to carry out this action."
    do_delete = raw_input("> ")
    if do_delete.lower() == 'yes':
        for status in tweepy.Cursor(t_api.favorites).items():
            try:
                t_api.destroy_favorite(status.id)
                #thread.start_new_thread(fdelete, (t_api, status.id,))
                print "Deleted:", status.id
            except:
                print "Failed to delete:", status.id
            sleep(1.5)
    return

def twitlookup(t_api):
    try:
        conn = db.connect('test.db')
        c = conn.cursor()
    except:
        print '[+]ERROR: Could not connect to db'
        return
    targetUsr = raw_input('Please enter a username: ')

  # check if user is in the SQLite db or not

    c.execute('SELECT count(*) FROM twitter WHERE username = (?)',(targetUsr, ))
    data = c.fetchone()[0]
    if data == 0:
        try:
            user = t_api.get_user(targetUsr)
        except:
            print 'User does not exist on twitter!'
            return
        print 'Username: ', user.screen_name
        followers = user.followers_count
        print 'Followers: ', followers
        tweets = t_api.user_timeline(targetUsr, count=1)
        for tweet in tweets:
            lastTweet = tweet.text
        print 'Latest tweet: \n', lastTweet
        try:
            conn.execute("INSERT INTO twitter (username, followers, lasttweet)"
                         "VALUES (?, ?, ?)",
                         (targetUsr, followers, lastTweet))
            conn.commit()
        except:
            print '[+]ERROR: Could not update databse'
        conn.close()
        return
    else:
        print targetUsr, ' is already in the database.'
        print 'Updating user information....'
        user = t_api.get_user(targetUsr)
        print 'Username: ', user.screen_name
        followers = user.followers_count
        print 'Followers: ', followers
        tweets = t_api.user_timeline(targetUsr, count=1)
        for tweet in tweets:
            lastTweet = tweet.text
        print 'Latest tweet: \n', lastTweet
        try:
            c.execute('UPDATE twitter set followers = ?, lasttweet ='
                      '? where username = ?',
                      (followers, lastTweet, targetUsr))
            conn.commit()
            conn.close()
        except:
            print '[+]ERROR: Could not update databse'
            return
        return

def mmenu():
    print """
    1. Live stream twitter (saved as csv)
    2. Live stream NO LOGGING!
    3. Gather last X tweets from user
    4. View recent follows
    5. View recent followers
    6. Get count of mentions of another user (last 200 tweets)
    7. Search for tweet
    8. Add user to sqlite db
    9. Delete all your tweets.
    10. Delete all favorites
    11. Delete Received DMs
    12. Delete Sent DMs
    0. Return
        """
