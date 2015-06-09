__author__ = 'Olenka'
import os
import django
import csv
from myapp.models import *

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
#django.setup()

file = open('Data2.txt', 'rbU')
r = csv.reader(file, delimiter='\t')
r.next()
for row in r:
    s = Subject(id=int(row[0]), name=row[1], kredits=float(row[2].replace(',', '.')), semestr=row[3], group=int(row[4]), \
                specialization=int(row[5]) if row[5] else None, depends_on=row[6])
    s.save()


file.close()