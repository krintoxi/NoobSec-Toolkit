#!/usr/bin/env python3
import threading
import csv
import os

try:
    import feedparser
except ImportError:
    print("[+] ERROR: Unable to import feedparser. Install with: pip3 install feedparser")
    feedparser = None


def newsthread(sorted_dictionary):
    os.makedirs("rss/news", exist_ok=True)
    raw_news_path = "rss/news/raw_news.csv"
    out_path = "rss/news/NEWS-OUT.csv"

    with open(raw_news_path, "a", newline="", encoding="utf-8") as saveFile:
        for lines, score in sorted_dictionary:
            print(lines, "\n")
            saveFile.write(str(lines) + "\n")

    seen = set()
    out_rows = []
    if os.path.exists(raw_news_path):
        with open(raw_news_path, "r", encoding="utf-8") as f1:
            reader = csv.reader(f1)
            for row in reader:
                if row and row[0] not in seen:
                    out_rows.append(row)
                    seen.add(row[0])

    with open(out_path, "w", newline="", encoding="utf-8") as out_f:
        writer = csv.writer(out_f)
        writer.writerows(out_rows)


def newsStart():
    if feedparser is None:
        return

    print("""
    A threshold value will tell OSCAR to search for occurrences
    of your keywords. This helps to ensure validity of news as
    well as relevance.

    Note: Not all sources will report the time they were updated.

    News is printed on screen and output to NEWS-OUT.csv
    Duplicate entries in the csv will be deleted automatically

    Edit feeds in: config/rssfeeds.dat
    Edit filters in: config/rssfilter.dat
    """)

    try:
        my_feeds = open("config/rssfeeds.dat").readlines()
        keywords = open("config/rssfilter.dat").read().splitlines()
    except FileNotFoundError as e:
        print("[+] ERROR: Config file not found: " + str(e))
        return

    print("Keywords: ", keywords)
    try:
        score_threshold = int(input("Please enter keyword threshold (ex: 2): ").strip())
    except ValueError:
        score_threshold = 2

    score_dictionary = {}
    for my_feed in my_feeds:
        f = feedparser.parse(my_feed.strip())
        for entry in f["entries"]:
            entry_score = 0
            for keyword in keywords:
                entry_score += entry.get("summary", "").count(keyword)
            try:
                tmp_key = "%s ,, %s ,, %s" % (
                    entry.get("title", ""),
                    entry.get("link", ""),
                    entry.get("updated", "")
                )
            except Exception:
                tmp_key = "%s ,, %s" % (entry.get("title", ""), entry.get("link", ""))
            score_dictionary[tmp_key] = entry_score

    filtered_dictionary = {
        key: value for key, value in score_dictionary.items()
        if value >= score_threshold
    }
    sorted_dictionary = sorted(
        filtered_dictionary.items(), key=lambda x: x[1], reverse=True
    )

    t = threading.Thread(target=newsthread, args=(sorted_dictionary,), daemon=True)
    t.start()
    t.join()
