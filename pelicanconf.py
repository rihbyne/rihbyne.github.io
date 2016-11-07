#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rihan Pereira'

SITEURL = 'https://rihbyne.github.io'
SITENAME = u"Rihan's log"
SITESUBTITLE = u"Software Enthusiast | Guitarist | Rookee Bassist"
SITELOGO = ''

TIMEZONE = 'Asia/Kolkata'

SITEFOOTER = u'Rihan &copy; 2016. Contents is <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/us/">cc by-nc-sa</a>. All opinions are of my own.'

#SITETITLE = AUTHOR
#SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR

DEFAULT_CATEGORY = 'software'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

SUMMARY_MAX_LENGTH = 15

#blog theming control
THEME = '../pelican-extras/pelican-themes/cid'
TYPOGRAPHY=True
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

OUTPUT_PATH = 'output'
PATH = 'content'

INDEX_URL = 'blog'
INDEX_SAVE_AS = INDEX_URL+'/index.html'

ARTICLE_URL = INDEX_URL+'/{slugs}'
ARTICLE_SAVE_AS = ARTICLE_URL+'/index.html'

page_dir = 'DIYs'
PAGE_URL = page_dir+'/{slug}'
PAGE_SAVE_AS = PAGE_URL+/index.html

DEFAULT_PAGINATION = 10

#DISQUS_SITENAME = 'rihbynelog'
#GOOGLE_ANALYTICS = 'something'






DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

LINKS = (('Portfolio', 'http://localhost:8113'),)

# Blogroll
SOCIAL = (('linkedin', 'http://getpelican.com/'),
          ('github', 'http://python.org/'),
          ('google', 'http://jinja.pocoo.org/'),
          ('twitter', '#'),
          ('rss', '#'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 2

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#plugins control
PLUGIN_PATHS = ['../pelican-extras/pelican-plugins']
PLUGINS = ['sitemap', 'post_stats', 'extract_toc', 'render_math']
MD_EXTENSIONS = ['codehilite', 'extra', 'smarty', 'toc']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# source static dirs to be included in output dir
STATIC_PATHS = ['extra', 'images', 'pdfs']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/htaccess': {'path': '.htaccess'}
}



COLOPHON = True
COLOPHON_TITLE = 'About'
COLOPHON_CONTENT = "Mainly..."
