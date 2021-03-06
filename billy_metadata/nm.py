import datetime

metadata = {
    'name': 'New Mexico',
    'abbreviation': 'nm',
    'legislature_name': 'New Mexico Legislature',
    'legislature_url': 'http://www.nmlegis.gov/',
    'capitol_timezone': 'America/Denver',
    'chambers': {
        'upper': {'name': 'Senate', 'title': 'Senator'},
        'lower': {'name': 'House', 'title': 'Representative'},
    },
    'terms': [
        {
            'name': '2011-2012',
            'start_year': 2011,
            'end_year': 2012,
            'sessions': ['2011', '2011S', '2012'],
        },
        {
            'name': '2013-2014',
            'start_year': 2013,
            'end_year': 2014,
            'sessions': ['2013', '2014'],
        },
        {
            'name': '2015-2016',
            'start_year': 2015,
            'end_year': 2016,
            'sessions': ['2015', '2015S', '2016', '2016S'],
        },
        {
            'name': '2017-2018',
            'start_year': 2017,
            'end_year': 2018,
            'sessions': ['2017', '2017S'],
        },
    ],
    'session_details': {
        '2011': {
            'display_name': '2011 Regular Session',
            'slug': '11%20Regular',
            '_scraped_name': '2011 Regular',
        },
        '2011S': {
            'display_name': '2011 Special Session',
            'slug': '11%20Special',
            '_scraped_name': '2011 1st Special',
        },
        '2012': {
            'display_name': '2012 Regular Session',
            'slug': '12%20Regular',
            '_scraped_name': '2012 Regular',
        },
        '2013': {
            'display_name': '2013 Regular Session',
            'slug': '13%20Regular',
            '_scraped_name': '2013 Regular',
        },
        '2014': {
            'display_name': '2014 Regular Session',
            'slug': '14%20Regular',
            '_scraped_name': '2014 Regular',
        },
        '2015': {
            'display_name': '2015 Regular Session',
            'slug': '15%20Regular',
            '_scraped_name': '2015 Regular',
        },
        '2015S': {
            'display_name': '2015 Special Session',
            'slug': '15%20Special',
            '_scraped_name': '2015 1st Special',
        },
        '2016': {
            'type': 'primary',
            'start_date': datetime.date(2016, 1, 19),
            'end_date': datetime.date(2016, 2, 18),
            'display_name': '2016 Regular Session',
            'slug': '16%20Regular',
            '_scraped_name': '2016 Regular',
        },
        '2016S': {
            'type': 'special',
            'start_date': datetime.date(2016, 9, 30),
            'end_date': datetime.date(2016, 10, 1),
            'display_name': '2016 2nd Special Session',
            'slug': '16%20Special',
            '_scraped_name': '2016 2nd Special',
        },     
        '2017': {
            'type': 'primary',
            'start_date': datetime.date(2016, 1, 17),
            'end_date': datetime.date(2017, 3, 18),
            'display_name': '2017 Regular Session',
            'slug': '17%20Regular',
            '_scraped_name': '2017 Regular',
        },          
        '2017S': {
            'type': 'special',
            'display_name': '2017 Special Session',
        },          
    },
    'feature_flags': ['subjects', 'influenceexplorer'],
    '_ignored_scraped_sessions': [
        '2010 2nd Special', '2010 Regular',
        '2009 1st Special', '2009 Regular',
        '2008 2nd Special', '2008 Regular',
        '2007 1st Special', '2007 Regular',
        '2006 Regular', '2005 1st Special',
        '2005 Regular', '2004 Regular',
        '2003 1st Special', '2003 Regular',
        '2002 Extraordinary', '2002 Regular',
        '2001 2nd Special', '2001 1st Special',
        '2001 Regular', '2000 2nd Special',
        '2000 Regular', '1999 1st Special',
        '1999 Regular', '1998 1st Special',
        '1998 Regular', '1997 Regular',
        '1996 1st Special', '1996 Regular',
    ]
}
