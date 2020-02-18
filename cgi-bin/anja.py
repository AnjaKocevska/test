#!/usr/local/bin/python3

# A simple script to accept input from an html form,
# parse the information, and do something - which in this case
# is to give user feedback with a simple html page.

# use python's the CGI package
import cgi
import cgitb
cgitb.enable()

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
v_name = form.getvalue('name')
v_email= form.getvalue('email')
v_color= form.getvalue('color')

# send an html response.
print("""
<html>
<body style="background-color: %s"
<p>
Thanks, %s %s
</p>
</body>
</html>
""" % (v_color, v_name, v_email))

file=open("stylee.css","w")
file.write("body{background-color: %s}" %(v_color))
file.close()