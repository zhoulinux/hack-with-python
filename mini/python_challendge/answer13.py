'''
http://www.pythonchallenge.com/pc/return/disproportional.html

click button 5 or inspec the page source:
http://www.pythonchallenge.com/pc/phonebook.php
click the link above show error message, so use xmlrpc to talk to it.

get '555-ITALY'.
555 basically means "fake phone numbers" in US.

http://www.pythonchallenge.com/pc/return/italy.html
'''


import xmlrpc.client


conn = xmlrpc.client.ServerProxy(
    'http://www.pythonchallenge.com/pc/phonebook.php'
)
print(conn.phone('Bert'))
