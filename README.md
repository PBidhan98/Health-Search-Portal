# Health-Search-Portal

pip install flask

python

import flask 
(no error)

exit()

mkdir Health-Search-Portal

cd Health-Search-Portal

set FLASK_APP=search.py

flask run

set FLASK_DEBUG=1

flask run
(we can see additional information in terminal in debug mode, in debug mode changes are loaded automatically)

If we don't want to work with the environment variables then there is another way using which we can run the application directly using python
put below code in search.py at the bottom

if __name__ == '__main__':
    app.run(debug=True)

python search.py

pip install flask-wtf

To use the forms we need to set the secret key for our application, a secret key will protect against modifying cookies and cross-site request forgery attacks etc.

app.config['SECRET_KEY'] = 'secret key from below'

python

import secrets

secrets.token_hex(16)
