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
# current_csrf_token = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=15))
# print(html_pages.login_page.format(current_csrf_token=current_csrf_token))
cookie_dict={}
if "HTTP_COOKIE" in os.environ :
    cookie_info = os.environ["HTTP_COOKIE"]
    cookies = cookie_info.split(';')
    for cookie in cookies :
        cookie_split = cookie.split('=')
        cookie_dict[cookie_split[0].strip()] = cookie_split[1].strip()
    username = cookie_dict["username"]

    query = "SELECT checkings, savings from bank where username='{username}'"
    c.execute(query.format(username=username))
    conn.commit()
    users = c.fetchall()

    table = ""
    for user in users :
        table += "<tr>\n"
        for col in user :
            table += "<td>" + str(col) + "</td>\n"
        table += "</tr>\n"

    print(html_pages.loggedin.format(username=username,table=table))

else:
    cookie_info= "Cookie not defined"
    current_csrf_token = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=15))
    print(html_pages.login_page.format(current_csrf_token=current_csrf_token))

