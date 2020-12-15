# ###### IMPORT #####
from news_test_project.parsers import *
import os, sys


proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append((proj))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news.settings")


# ###### IMPORT #####
import django
django.setup()
from  django.db import DatabaseError
from news_test_project.parsers import *
from news_test_project.models import Vacancy, City, Language



parser = (
    (site_126, 'https://126.ru/stavropol/rabota/it-telekom-kompyutery/'),
    (site_joblab, 'https://joblab.ru/search.php?r=vac&srprofecy=%CF%F0%EE%E3%F0%E0%EC%EC%E8%F1%F2&kw_w2=1&srzpmin=&srregion=26&srcity=305&srcategory=&submit=1'),
    (site_1777, 'https://rabota.1777.ru/search_vakansia.php?cat_id=4')
     )


city = City.objects.filter(slug='Stavropol').first()
language = Language.objects.filter(slug='Python').first()

jobs, errors = [], []

for func, url in parser:
    print(func)
    print(url)
    j, e = func(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass