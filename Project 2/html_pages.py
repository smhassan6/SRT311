#!/usr/bin/python3

import cgi
import cgitb
cgitb.enable()
login_page = """Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
    <title>Bank</title>
</head>
<body>
<h2> Login</h2>
    <form action="login.py" method="POST">
        Bank ID: <input type="text" name="username""><br><br>
        Password: <input type="password" name="hashed_password"><br><br>
        <input type="hidden" name="current_csrf_token" value="{current_csrf_token}">
        <input type="submit" value="submit">
    </form>
</body>
</html>
"""

fail_page = """
<!DOCTYPE html>
<html>
<head>
    <title> Failed to Login</title>
    <meta http-equiv="refresh"
        content="0; url = http://localhost/srt311/project2/main.py" />  
</head>
<body>
    <script>alert("Failed to login");</script>
</body>
</html>
"""

save_cookie = """Content-Type: text/html
Set-Cookie: username={username}
Set-Cookie: hashed_password={hashed_password}
Set-Cookie: current_csrf_token={current_csrf_token}

<!DOCTYPE html>
 <html>
 <head>
      <title>Login Successful</title>
      <meta http-equiv="refresh"
         content="1; url = http://localhost/srt311/project2/main.py" />  
 </head>
 <body>
     <h2> Login Successful </h2>
  </body>
 </html>
"""
loggedin = """Content-Type: text/html
<!DOCTYPE html>
    <html>
    <head>
        <title> Welcome {username} </title>
    </head>
    <body>
        <center>
        <h1>Welcome {username}</h1>
        <table style="width:50%" border="1">
            <tr>
                <td><strong>Checkings</strong></td>
                <td><strong>Savings</strong></td>
            </tr>
            {table}
        </table>
        <a href="transfer_form.py">Transfer money</a>
        </center>
    </body>
</html>
"""

transfer_form = """<!DOCTYPE html>
<html>
<head>
<title>Transfer Money</title>
<head>
<body>
<h2> Transfer Money</h2>
    <form action="transfer.py" method="POST">
        Account of Recepient:  <input type="text" name="account""><br><br>
        From (checking or savings):  <input type="text" name="sender""><br><br>
        To (checkings or savings): <input type="text" name="receiver""><br><br>
        Amount <input type ="text" name="amount""><br><br>
        <input type="hidden" name="current_csrf_token" value="{current_csrf_token}">
        <input type="submit" value="submit">
        <a href="main.py">Cancel</a>
    </form>
</body>
</html>
"""

success = """Content-Type: text/html
Transfer Success!
"""