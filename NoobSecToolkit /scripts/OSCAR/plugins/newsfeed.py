#!/usr/bin/env python

try:
    import feedparser
except:
    print "[+]ERROR: Unable to import feedparser"
    pass

import thread


#thread function to do the sorting and file IO :)
def newsthread():
    for lines in sorted_dictionary:
        saveFile = open('rss/newsraw_news.csv', 'a')
        print lines, "\n"
        saveFile.write(str(lines))
        saveFile.write('\n')
        saveFile.close()
    f1 = csv.reader(open('rss/news/raw_news.csv', 'rb'))
    writer = csv.writer(open("rss/news/NEWS-OUT.csv", "wb"))
    feedOut = set()
    for row in f1:
        if row[0] not in feedOut:
            writer.writerow(row)
            feedOut.add(row[0])
    return


def newsStart():
    print """
    A threshold value will tell OSCAR to search for occurrences
    of your keywords. This helps to ensure validity of news as
    well as relevance

    Note: Not all sources will report the time they were updated.

    News is printed on screen and output to NEWS-OUT.csv
    Duplicate entries in the csv will be deleted automatically

    Edit feeds in: feeds.dat
    Edit filters in: filter.dat
    """
    my_feeds = open('config/'+"rssfeeds.dat").readlines()
    keywords = open('config/'+"rssfilter.dat").read().splitlines()
    print "keywords: ", keywords
    score_threshold = input("Please enter keyword threshold (ex: 2): ")
    score_dictionary = {}
    for my_feed in my_feeds:
        f = feedparser.parse(my_feed)
        for entry in f['entries']:
            entry_score = 0
            for keyword in keywords:
                entry_score += entry['summary'].count(keyword)
                try:
                    tmp_key = '%s ,, %s ,, %s' % (entry['title'],
                                                  entry['link'],
                                                  entry['updated'])
                    score_dictionary[tmp_key] = entry_score
                except:
                    tmp_key = '%s ,, %s' % (entry['title'], entry['link'])
                    score_dictionary[tmp_key] = entry_score
    filtered_dictionary = {key.encode('utf-8'): value for key,
                           value in score_dictionary.items()
                           if value >= score_threshold}
    sorted_dictionary = sorted(filtered_dictionary.iteritems(),
                               key=lambda x: x[1],
                               reverse=True)
    #start thread for file IO performance
    thread.start_new_thread(newsthread, (sorted_dictionary,))
    #for lines in sorted_dictionary:
    #  saveFile = open('rss/newsraw_news.csv','a')
    #  print lines,"\n"
    #  saveFile.write(str(lines))
    #  saveFile.write('\n')
    #  saveFile.close()
    #f1 = csv.reader(open('rss/news/raw_news.csv', 'rb'))
    #writer = csv.writer(open("rss/news/NEWS-OUT.csv", "wb"))
    #feedOut = set()
    #for row in f1:
    #  if row[0] not in feedOut:
    #    writer.writerow(row)
    #    feedOut.add( row[0] )
    #return
