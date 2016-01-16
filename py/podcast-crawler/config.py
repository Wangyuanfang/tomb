#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

DB_HOST = 'localhost'
DB_NAME = 'pdcast'
DB_USER = 'root'
DB_PASS = '123456'

MONGO_URL = 'mongodb://localhost:27017'

INDEX_CACHE_EXPIRE_DAYS = 365
LOOKUP_CACHE_EXPIRE_DAYS = 365
FEED_CACHE_EXPIRE_DAYS = 365
FORCE_PARSE_LOOKUP = False
FORCE_PARSE_FEED = False
TEST_ON_US = False

try:
    from local_config import *
except:
    pass

ITUNES_COUNTRY_CODE = {
    'Canada': 'ca', 'Uruguay (English)': 'uy_en', 'Turkmenistan': 'tm', 'Lithuania': 'lt', 'Cambodia': 'kh', 'Germany (English)': 'de_en', 'Turkey (English)': 'tr_en', 'Micronesia': 'fm', 'Argentina': 'ar', 'Bolivia': 'bo', 'Burkina Faso': 'bf', 'Ghana': 'gh', 'Saudi Arabia': 'sa', 'Panama (English)': 'pa_en', 'Dominican Republic (English)': 'do_en', 'Japan': 'jp', 'Cape Verde': 'cv', 'Slovenia': 'si', 'Guatemala': 'gt', 'Zimbabwe': 'zw', 'Belize (Spanish)': 'bz_es', 'Jordan': 'jo', 'St. Lucia': 'lc', 'Dominica': 'dm', 'Liberia': 'lr', 'Netherlands': 'nl', 'Russia (English)': 'ru_en', 'Pakistan': 'pk', 'Netherlands (English)': 'nl_en', 'Tanzania': 'tz', 'Vietnam': 'vn', 'S\xc3\xa3o Tom\xc3\xa9 and Pr\xc3\xadncipe': 'st', 'Dominica (English)': 'dm_en', 'Mauritania': 'mr', 'Seychelles': 'sc', 'New Zealand': 'nz', 'Yemen': 'ye', 'Jamaica': 'jm', 'Malaysia (English)': 'my_en', 'Albania': 'al', 'Macau': 'mo', 'Korea (English)': 'kr_en', 'India': 'in', 'Azerbaijan': 'az', 'United Arab Emirates': 'ae', 'Kenya': 'ke', 'Tajikistan': 'tj', 'Nicaragua (English)': 'ni_en', 'Turkey': 'tr', 'Japan (English)': 'jp_en', 'Czech Republic': 'cz', 'Luxembourg (English)': 'lu_en', 'Solomon Islands': 'sb', 'Switzerland (French)': 'ch_fr', 'Palau': 'pw', 'Mongolia': 'mn', 'France': 'fr', 'Bermuda': 'bm', 'Slovakia': 'sk', 'Sweden (English)': 'se_en', 'Peru': 'pe', 'Indonesia (English)': 'id_en', 'Norway': 'no', 'Malawi': 'mw', 'Benin': 'bj', 'Macau (English)': 'mo_en', 'Brazil (English)': 'br_en', 'Singapore': 'sg', 'China': 'cn', 'Armenia': 'am', 'Suriname (English)': 'sr_en', 'Dominican Republic': 'do', 'Luxembourg (French)': 'lu_fr', 'Hong Kong (English)': 'hk_en', 'Ukraine': 'ua', 'Bahrain': 'bh', 'Cayman Islands': 'ky', 'Portugal (English)': 'pt_en', 'Finland': 'fi', 'Mauritius': 'mu', 'Sweden': 'se', 'Belarus': 'by', 'British Virgin Islands': 'vg', 'Mali': 'ml', 'Russia': 'ru', 'Bulgaria': 'bg', 'United States': 'us', 'Romania': 'ro', 'Angola': 'ao', 'Chad': 'td', 'China (English)': 'cn_en', 'Cyprus': 'cy', 'Brunei Darussalam': 'bn', 'Qatar': 'qa', 'Malaysia': 'my', 'Austria': 'at', 'Latvia': 'lv', 'Mozambique': 'mz', 'Uganda': 'ug', 'Hungary': 'hu', 'Niger': 'ne', 'El Salvador (English)': 'sv_en', 'Brazil': 'br',
    'Costa Rica (English)': 'cr_en', 'Singapore (English)': 'sg_en', 'Kuwait': 'kw', 'Panama': 'pa', 'Costa Rica': 'cr', 'Luxembourg': 'lu', 'St. Kitts and Nevis': 'kn', 'Bahamas': 'bs', 'Ireland': 'ie', 'Italy (English)': 'it_en', 'Italy': 'it', 'Nigeria': 'ng', 'Taiwan (English)': 'tw_en', 'Ecuador': 'ec', 'Australia': 'au', 'Algeria': 'dz', 'El Salvador': 'sv', 'Finland (English)': 'fi_en', 'Argentina (English)': 'ar_en', 'Turks and Caicos': 'tc', 'Chile': 'cl', 'Belgium': 'be', 'Thailand': 'th', 'Belgium (English)': 'be_en', 'Hong Kong': 'hk', 'Sierra Leone': 'sl', 'Switzerland (Italian)': 'ch_it', 'Oman': 'om', 'St. Vincent and The Grenadines': 'vc', 'Gambia': 'gm', 'Philippines': 'ph', 'Uzbekistan': 'uz', 'Moldova': 'md', 'Paraguay (English)': 'py_en', 'Croatia': 'hr', 'Guatemala (English)': 'gt_en', 'Guinea-Bissau': 'gw', 'Switzerland': 'ch', 'Grenada': 'gd', 'Spain (English)': 'es_en', 'Belize': 'bz', 'Portugal': 'pt', 'Estonia': 'ee', 'Uruguay': 'uy', 'South Africa': 'za', 'Lebanon': 'lb', 'France (English)': 'fr_en', 'Tunisia': 'tn', 'United States (Spanish)': 'us_es', 'Antigua and Barbuda': 'ag', 'Spain': 'es', 'Colombia': 'co', 'Norway (English)': 'no_en', 'Vietnam (English)': 'vn_en', 'Taiwan': 'tw', 'Fiji': 'fj', 'Barbados': 'bb', 'Madagascar': 'mg', 'Belgium (French)': 'be_fr', 'Bhutan': 'bt', 'Nepal': 'np', 'Malta': 'mt', 'Honduras (English)': 'hn_en', 'Chile (English)': 'cl_en', 'Suriname': 'sr', 'Anguilla': 'ai', 'Venezuela': 've', 'Swaziland': 'sz', 'Israel': 'il', 'Lao': 'la', 'Indonesia': 'id', 'Iceland': 'is', 'Canada (French)': 'ca_fr', 'Senegal': 'sn', 'Papua New Guinea': 'pg', 'Thailand (English)': 'th_en', 'Trinidad and Tobago': 'tt', 'Germany': 'de', 'Denmark': 'dk', 'Kazakhstan': 'kz', 'Poland': 'pl', 'Ecuador (English)': 'ec_cn', 'Kyrgyzstan': 'kg', 'Montserrat': 'ms', 'Macedonia': 'mk', 'Mexico (English)': 'mx_en', 'Sri Lanka': 'lk', 'Korea': 'kr', 'Guyana': 'gy', 'Colombia (English)': 'co_en', 'Venezuela (English)': 've_en', 'Honduras': 'hn', 'Mexico': 'mx', 'Egypt': 'eg', 'Nicaragua': 'ni', 'Denmark (English)': 'dk_en', 'Switzerland (English)': 'ch_en', 'Austria (English)': 'at_en', 'United Kingdom': 'gb', 'Congo': 'cg', 'Greece': 'gr', 'Paraguay': 'py', 'Namibia': 'na', 'Bolivia (English)': 'bo_en', 'Botswana': 'bw'}

if TEST_ON_US:
    PIDS_QUERY = {'country': 'us'}
    ITUNES_COUNTRY_CODE = {'United States': 'us'}
else:
    PIDS_QUERY = {}

ITUNES_PODCAST_GENRE_CODE = {
    'Arts': 1301,
    'Business': 1321,
    'Comedy': 1303,
    'Education': 1304,
    'Games & Hobbies': 1323,
    'Government & Organizations': 1325,
    'Health': 1307,
    'Kids & Family': 1305,
    'Music': 1310,
    'News & Politics': 1311,
    'Religion & Spirituality': 1314,
    'Science & Medicine': 1315,
    'Society & Culture': 1324,
    'Sports & Recreation': 1316,
    'TV & Film': 1309,
    'Technology': 1318
}

ITUNES_PODCAST_ALL_GENRE_CODE = {
    'Arts': 1301, 'Regional': 1474, 'Natural Sciences': 1477, 'Fitness & Nutrition': 1417, 'Podcasting': 1450, 'Games & Hobbies': 1323, 'Science & Medicine': 1315, 'Performing Arts': 1405, 'Sports & Recreation': 1316, 'Christianity': 1439, 'Spirituality': 1444, 'Kids & Family': 1305, 'Other': 1464, 'Music': 1310, 'Educational Technology': 1468, 'Medicine': 1478, 'Tech News': 1448, 'Comedy': 1303, 'Local': 1475, 'Social Sciences': 1479, 'Careers': 1410, 'Personal Journals': 1302, 'Philosophy': 1443, 'Literature': 1401, 'Shopping': 1472, 'Business': 1321, 'Food': 1306, 'Automotive': 1454, 'Video Games': 1404, 'Language Courses': 1469, 'Investing': 1412, 'Software How-To': 1480, 'College & High School': 1466,
    'Aviation': 1455, 'Non-Profit': 1476, 'Training': 1470, 'Higher Education': 1416, 'Judaism': 1441, 'Government & Organizations': 1325, 'Business News': 1471, 'Religion & Spirituality': 1314, 'K-12': 1415, 'Alternative Health': 1481, 'News & Politics': 1311, 'Podcasts': 26, 'Places & Travel': 1320, 'Sexuality': 1421, 'Other Games': 1461, 'Self-Help': 1420, 'Amateur': 1467, 'Professional': 1465, 'TV & Film': 1309, 'History': 1462, 'Hinduism': 1463, 'Visual Arts': 1406, 'Fashion & Beauty': 1459, 'Outdoor': 1456, 'Management & Marketing': 1413, 'Society & Culture': 1324, 'National': 1473, 'Buddhism': 1438, 'Gadgets': 1446, 'Design': 1402, 'Hobbies': 1460, 'Health': 1307, 'Education': 1304, 'Technology': 1318, 'Islam': 1440}
