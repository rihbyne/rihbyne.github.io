#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rihan Pereira'
SITEURL = 'http://localhost:8113'
SITENAME = 'ByneBits'
SITETITLE = AUTHOR
SITESUBTITLE = 'Software Engineer | Guitarist | Rookee Bassist'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = ''
FAVICON = '/extra/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

#blog theming control
THEME = 'themes/Flex'
PATH = 'content'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y'
}

DEFAULT_DATE = 'fs'

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

DEFAULT_PAGINATION = 5

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
