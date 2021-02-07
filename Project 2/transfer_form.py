#!/usr/bin/python3
import string
import random
import pymysql
import html_pages
import os
import cgitb
cgitb.enable()
conn = pymysql.connect(
db='project2',
user='kobe',
passwd='bryant',
host='localhost')
c = conn.cursor()
print("Content-Type: text/html")
print()

if "HTTP_COOKIE" in os.environ :
   cookie_info = os.environ["HTTP_COOKIE"]
   print(html_pages.transfer_form)

else :
   cookie_info = "cookie not defined"
   print(html_pages.fail_page)
