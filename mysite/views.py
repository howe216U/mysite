from django.shortcuts import render
import MySQLdb

def book_list(request):
    db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render(request, 'book_list.html', {'names': names})

import datetime

def hello(request):
    now = datetime.datetime.now()
    return render(request, 'hello.html', {'current_date': now})

def my_homepage(request):
    now = datetime.datetime.now()
    return render(request, 'hello.html', {'current_date': now})

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    hours_offset = offset
    next_time = datetime.datetime.now() + datetime.timedelta(hours=offset)  
    item_list = [ {'name':"one", 'value':1}, {'name':"two", 'value':2}, {'name':"three",'value':3}, {'name':"four",'value':4}, {'name':"five",'value':5}, {'name':"six",'value':6}]
#    print next_time
# this prints on the console from python manage.py runserver ..... command
    return render(request, 'hours_ahead.html', {'one':offset,'two':next_time, 'three':'my name is django dave','item_list':item_list})
