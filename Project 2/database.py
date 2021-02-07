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
    current_csrf_token = pymysql.escape_string(form["current_csrf_token"].value)
except:
    current_csrf_token = "void"

def connection():
    conn = pymysql.connect(
    db='project2',
    user='kobe',
    passwd='bryant',
    host='localhost')
    c = conn.cursor()

def all():
    c.execute("SELECT * from bank where username = '{username}' and hashed_password = '{hashed_password}'" )
    conn.commit()

def update():
    
    query = "update bank set {sender} = {sender_amount} where username = '{username}'"
    c.execute(query.format(username=username, sender=sender, sender_amount=sender_amount))
    query1 = "update bank set {receiver} = {receiver_amount} where username = '{account}'"
    c.execute(query1.format(receiver=receiver, receiver_amount=receiver_amount, account=account))
    conn.commit()

def retrieve():
    c.execute("SELECT current_csfr_token='{current_csrf_token} where username='{username}'")
    conn.commit()

def save_token():
    query="Update bank SET current_csrf_token='{current_csrf_token}' WHERE username='{username}'"
    c.execute(query.format(username=username, current_csrf_token=current_csrf_token))
    conn.commit()

