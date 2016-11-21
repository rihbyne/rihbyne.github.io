#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

AUTHOR = u'Rihan Pereira'

SITEURL = 'http://localhost:8113'
SITENAME = u"Rihan's log"
SITESUBTITLE = u"Software Enthusiast | Guitarist | Rookee Bassist"
SITELOGO = 'images/android-chrome-512x512.png'

THUMBNAIL = 'images/img_2.jpg'

TIMEZONE = 'Asia/Kolkata'

SITEFOOTER = u'Rihan &copy; 2016. Contents is <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/us/">cc by-nc-sa</a>. All opinions are of my own.'

#SITETITLE = AUTHOR
#SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR

USE_FOLDER_AS_CATEGORY = True
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

# source static dirs to be included in output dir
STATIC_PATHS = ['extra', 'images', 'pdfs', 'downloadables', 'blog']
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['doityourself']

INDEX_URL = 'blog'
INDEX_SAVE_AS = INDEX_URL+'/index.html'

ARTICLE_URL = INDEX_URL+'/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL+'/index.html'

page_dir = 'doityourself'
PAGE_URL = page_dir+'/{slug}'
PAGE_SAVE_AS = PAGE_URL+'/index.html'

DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'

DEFAULT_PAGINATION = 6

COPYRIGHT_YEAR = 2016

#DISQUS_SITENAME = 'rihbynelog'
#GOOGLE_ANALYTICS = 'something'

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (('blog', INDEX_URL),
                    ('resume', 'downloadables/resume.pdf'),
                    ('reading', 'https://goodreads.com/rihbyne'),
                    ('DIYs', 'DIYs'),
                   )

#social links
SOCIAL = (('Github', 'https://github.com/rihbyne'),
          ('Linkedin', 'https://linkedin.com/in/rihbyne'),
          ('Soundcloud', 'https://soundcloud.com/rihbyne'),
          ('Quora', 'https://quora.com/Rihan-Pereira'),
          ('Twitter', 'https://twitter.com/rihbyne'),
          ('YouTube', 'https://www.youtube.com/c/Rihan-Pereira'),)

#CONTACT_EMAIL = "rihen234@gmail.com"

#DEFAULT_LANG = 'en'
#OG_LOCALE = 'en_US'
#LOCALE = 'en_US'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

LINKS = (('Portfolio', 'http://localhost:8113'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

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

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/human.txt': {'path': 'humans.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/htaccess': {'path': '.htaccess'},
}
