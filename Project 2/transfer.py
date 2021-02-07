import pymysql
import cgi
import cgitb
import html_pages
import os
cgitb.enable()
conn = pymysql.connect(
db='project2',
user='kobe',
passwd='bryant',
host='localhost')
c = conn.cursor()
form = cgi.FieldStorage()
print("Content-Type: text/html")
print()
try:
    account = pymysql.escape_string(form["account"].value)
except:
    account = "Void"
try:
    sender = pymysql.escape_string(form["sender"].value)
except:
    sender = "Void"
try:
    receiver = pymysql.escape_string(form["receiver"].value)
except:
    receiver = "Void"
try:
    amount = pymysql.escape_string(form["amount"].value)
except:
    amount ="Void"
try:
    current_csrf_token = pymysql.escape_string(form["current_csrf_token"].value)
except:
    current_csrf_token = "Login again"

cookie_info = os.environ["HTTP_COOKIE"]
cookies = cookie_info.split(';')
cookie_dict={}
for cookie in cookies :
    cookie_split = cookie.split('=')
    cookie_dict[cookie_split[0].strip()] = cookie_split[1].strip()
try:
    username = cookie_dict["username"]
except:
    username = "Void"
try:
    hashed_password = cookie_dict["hashed_password"]
except:
    hashed_password = "Void"
try:
    current_csrf_token = cookie_dict["current_csrf_token"]
except:
    current_csrf_token = "Void"
if c.rowcount > 0:
    query = "SELECT username from bank where username = '{account}'"
    c.execute(query.format(account=account))
    if c.rowcount > 0:
        if sender_amount < amount:
            print("Not enough funds")
        else:
                try:
                    sender_amount = sender_amount-amount
                    receiver_amount = receiver_amount+amount
                    query = "update bank set {sender} = {sender_amount} where username = '{username}'"
                    c.execute(query.format(username=username, sender=sender, sender_amount=sender_amount))
                    query1 = "update bank set {receiver} = {receiver_amount} where username = '{account}'"
                    c.execute(query1.format(receiver=receiver, receiver_amount=receiver_amount, account=account))
                    conn.commit()
                    print(html_pages.success)