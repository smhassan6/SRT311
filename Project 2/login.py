#!/usr/bin/python3
import pymysql
import cgi
import cgitb
import html_pages
cgitb.enable()
form = cgi.FieldStorage()
try:
    username = pymysql.escape_string(form["username"].value)
except:
    username = "void"
try:
    hashed_password = pymysql.escape_string(form["hashed_password"].value)
except:
    hashed_password = "void"
try:
    current_csrf_token = form["current_csrf_token"].value
except:
    current_csrf_token = "void"

conn = pymysql.connect(
db='project2',
user='kobe',
passwd='bryant',
host='localhost')
c = conn.cursor()

query="SELECT * FROM bank where username='{username}'"
c.execute(query.format(username=username))
conn.commit()
user = c.fetchone()
if user:
    if user[1] == hashed_password:
        query="Update bank SET current_csrf_token='{current_csrf_token}' WHERE username='{username}'"
        c.execute(query.format(username=username, current_csrf_token=current_csrf_token))
        conn.commit()
        print(html_pages.save_cookie.format(username=username, hashed_password=hashed_password, current_csrf_token=current_csrf_token))
        
    else:
        print(html_pages.fail_page)



