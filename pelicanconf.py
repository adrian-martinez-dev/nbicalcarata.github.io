# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adri\xe1n Mart\xednez'
SITENAME = u'Ziggurat Vertigo'
SITESUBTITLE = u'Apuntes diversos y hojas trampa'

PATH = 'content'
# THEME = "/home/adrian/pelican-themes/nikhil-theme"
# THEME = "/home/adrian/pelican-themes/storm"
THEME = "pujangga"

TIMEZONE = 'America/Monterrey'

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'es': '%A, %d de %B del %Y',
    'jp': '%Y-%m-%d(%a)',
}
SHOW_CONTENT_SUMMARY_ON_INDEX = True
DEFAULT_LANG = u'es'
LOCALE='es_MX.utf8'

DEFAULT_DATE_FORMAT = {'%A %d %B %Y'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = 4

# DEFAULT_PAGINATION = False
# SUMMARY_MAX_LENGTH = 30
# DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# MENUITEMS = (
    # ('Inicio', ''),
    # ('Acerca de',  '/pages/acerca-de.html'),
    # ('CV', '')
    # )

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

STATIC_PATHS = ['images' ]

# PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

PLUGINS = [
    # ...
    'pelican_gist',
    # ...
]
