#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import threading
import sys
import os
import re
from time import sleep

try:
    import sqlite3 as db
except ImportError:
    print("[+] ERROR: could not import sqlite3.")
    db = None

try:
    import tweepy
    from tweepy import *
    from tweepy.streaming import *
except ImportError:
    print("[+] ERROR: Unable to import tweepy! Install with: pip3 install tweepy")
    tweepy = None


def hist_tweet(t_api):
    con = ""
    try:
        while con.lower() not in ("n", "no"):
            try:
                num_tweets = int(input("How many tweets (200 maximum): ").strip())
            except ValueError:
                print("[+] ERROR: must be a number value!")
                return
            targetUsr = input("Enter target user: ").strip()
            user = t_api.get_user(screen_name=targetUsr)
            print()
            print("Username: ", user.screen_name)
            print("Follower count: ", user.followers_count)
            print()
            target_tweets = t_api.user_timeline(screen_name=targetUsr, count=num_tweets)
            counter = 0
            for tweet in target_tweets:
                counter += 1
                print(counter, "-", tweet.text)
            con = input("Run again? (y/n): ").strip()
    except KeyboardInterrupt:
        return


def lv_stream(t_auth):
    filt = input("Enter filter option: ").strip()

    class listen(StreamListener):
        def on_status(self, status):
            try:
                print(status.author.screen_name + ": " + status.text)
                print()
                with open("STREAM_%s.csv" % filt, "a", encoding="utf-8") as saveFile:
                    saveFile.write(status.author.screen_name + ",," + status.text + "\n")
                return True
            except (BaseException, KeyboardInterrupt, SystemExit):
                sleep(3)
                return

        def on_error(self, status):
            return

    twitterStream = Stream(t_auth, listen())
    twitterStream.filter(track=[filt])


def lv_streamno(t_auth):
    filt = input("Enter filter option: ").strip()

    class listen(StreamListener):
        def on_status(self, status):
            try:
                print(status.author.screen_name + ": " + status.text)
                print()
                return True
            except (BaseException, KeyboardInterrupt, SystemExit):
                sleep(3)
                return

        def on_error(self, status):
            return

    twitterStream = Stream(t_auth, listen())
    twitterStream.filter(track=[filt])


def rcntFllw(t_api):
    targetUsr = input("Enter target user: ").strip()
    user = t_api.get_user(screen_name=targetUsr)
    for friend in user.friends():
        print(friend.screen_name)
    print()


def rcntFllwrs(t_api):
    targetUsr = input("Enter target user: ").strip()
    user = t_api.get_user(screen_name=targetUsr)
    for friends in user.followers(count=100):
        print(friends.screen_name)
    print()


def mentionCount(t_api):
    names = []
    print("""
    1. Retrieve details
    2. Count specific mentions
    """)
    opt = input("Enter an option: ").strip()
    if opt == "1":
        targetUsr = input("Please enter a username: ").strip()
        user = t_api.get_user(screen_name=targetUsr)
        target_tweets = t_api.user_timeline(screen_name=targetUsr, count=200)
        with open("tweets.txt", "a", encoding="utf-8") as saveFile:
            for tweet in target_tweets:
                saveFile.write(tweet.text + "\n")
        mentionCount(t_api)
    elif opt == "2":
        try:
            tweetedUsrs = open("tweets.txt").read().splitlines()
        except FileNotFoundError:
            print("There was an error opening the tweets file. Did you run the first option?")
            return
        for lines in tweetedUsrs:
            tos = re.findall(r"@([A-Za-z0-9_]{1,15})", lines)
            for twitUsr in tos:
                names.append(twitUsr)
        while True:
            try:
                targetUsr2 = input("Enter a twitter handle (without the @) Ctrl+C to return: ").strip()
                print("Number of times mentioned: ", names.count(targetUsr2))
            except KeyboardInterrupt:
                print()
                return


def twitSearch(t_api):
    t_query = input("Enter search: ").strip()
    t_res = tweepy.Cursor(t_api.search_tweets, q=t_query, count=10,
                          result_type="recent").items()
    while True:
        try:
            tweet = next(t_res)
            print(tweet.user.screen_name, ":", tweet.created_at, ":", tweet.text)
            print()
            sleep(5)
        except tweepy.TweepyException:
            sleep(60 * 15)
        except StopIteration:
            return
        except KeyboardInterrupt:
            return


def twitdelete(t_api, stat):
    try:
        t_api.destroy_status(stat)
        print("Deleted:", stat)
    except Exception:
        print("Failed to delete:", stat)


def batch_delete(t_api):
    print("You are about to delete all tweets from @%s." % t_api.verify_credentials().screen_name)
    print("Type 'yes' to carry out this action. There is no undo!")
    do_delete = input("> ").strip()
    if do_delete.lower() == "yes":
        for status in tweepy.Cursor(t_api.user_timeline).items():
            try:
                t = threading.Thread(target=twitdelete, args=(t_api, status.id), daemon=True)
                t.start()
            except Exception:
                print("Failed to delete:", status.id)
            sleep(0.5)


def dm_batch(t_api):
    print("You are about to delete all RECEIVED DMs from @%s." % t_api.verify_credentials().screen_name)
    print("Type 'yes' to carry out. There is no undo!")
    do_delete = input("> ").strip()
    if do_delete.lower() == "yes":
        direct_messages = tweepy.Cursor(t_api.get_direct_messages).items()
        for direct_message in itertools.islice(direct_messages, 0, None):
            try:
                t_api.delete_direct_message(direct_message.id)
                print("Deleted:", direct_message.id)
            except Exception:
                print("Failed to delete:", direct_message.id)
            sleep(5)


def dm_sent(t_api):
    print("You are about to delete all SENT DMs from @%s." % t_api.verify_credentials().screen_name)
    print("Type 'yes' to carry out. There is no undo!")
    do_delete = input("> ").strip()
    if do_delete.lower() == "yes":
        sent_direct_messages = tweepy.Cursor(t_api.sent_direct_messages).items()
        for direct_message in itertools.islice(sent_direct_messages, 0, None):
            try:
                t_api.delete_direct_message(direct_message.id)
                print("Deleted:", direct_message.id)
            except Exception:
                print("Failed to delete:", direct_message.id)
            sleep(5)


def favdelete(t_api):
    print("You are about to delete all favorites from @%s." % t_api.verify_credentials().screen_name)
    print("Type 'yes' to carry out. There is no undo!")
    do_delete = input("> ").strip()
    if do_delete.lower() == "yes":
        for status in tweepy.Cursor(t_api.get_favorites).items():
            try:
                t_api.remove_favorite(status.id)
                print("Deleted:", status.id)
            except Exception:
                print("Failed to delete:", status.id)
            sleep(1.5)


def twitlookup(t_api):
    if db is None:
        print("[+] ERROR: sqlite3 not available.")
        return
    try:
        conn = db.connect("test.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS twitter (username TEXT, followers INTEGER, lasttweet TEXT)")
    except Exception:
        print("[+] ERROR: Could not connect to db")
        return

    targetUsr = input("Please enter a username: ").strip()
    c.execute("SELECT count(*) FROM twitter WHERE username = (?)", (targetUsr,))
    data = c.fetchone()[0]

    user = None
    lastTweet = ""
    try:
        user = t_api.get_user(screen_name=targetUsr)
    except Exception:
        print("User does not exist on twitter!")
        conn.close()
        return

    print("Username: ", user.screen_name)
    followers = user.followers_count
    print("Followers: ", followers)
    tweets = t_api.user_timeline(screen_name=targetUsr, count=1)
    for tweet in tweets:
        lastTweet = tweet.text
    print("Latest tweet:\n", lastTweet)

    if data == 0:
        try:
            conn.execute(
                "INSERT INTO twitter (username, followers, lasttweet) VALUES (?, ?, ?)",
                (targetUsr, followers, lastTweet)
            )
            conn.commit()
        except Exception:
            print("[+] ERROR: Could not update database")
    else:
        print(targetUsr, " is already in the database. Updating...")
        try:
            c.execute(
                "UPDATE twitter SET followers = ?, lasttweet = ? WHERE username = ?",
                (followers, lastTweet, targetUsr)
            )
            conn.commit()
        except Exception:
            print("[+] ERROR: Could not update database")
    conn.close()


def mmenu():
    print("""
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
    """)
