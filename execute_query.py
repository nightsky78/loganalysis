#!/usr/bin/env python3
"""Print query results for news log DB."""

import db

# set numbers of lines to show
top_authors_line = 3
top_articles_lines = 3

# set error margin to show. Course asks for more than 1%
error_margin = 0.01

# instanciate the DB handler
myDB = db.DbHandler()

# retrieve and print the top articles
top_articles = myDB.retrieve_popular_articles(top_articles_lines)
print('1. What are the most popular three articles of all time?')

i = 0
for value in top_articles:
    print(top_articles[i][0] + '  ---  ' + str(top_articles[i][1]) + ' views')
    i = i + 1
print(" ")

#  retrieve and print the top authors
top_authors = myDB.retrieve_popular_authors(top_authors_line)
print('2. Who are the most popular article authors of all time?')
i = 0
for value in top_authors:
    print(top_authors[i][0] + '  ---  ' + str(top_authors[i][1]) + ' views')
    i = i + 1
print('')

# retrieve and print days where errors are higher as error margin set above.
error_days = myDB.retrieve_failure_days(error_margin)
print('3. On which days did more than 1% of requests lead to errors?')
i = 0
for value in error_days:
    print('{0} --- {1:.2f}% errors'.format(error_days[i][0].
                                           strftime('%B %d, %Y'),
                                           error_days[i][1]*100))
    i = i + 1
print('')
