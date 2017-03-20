from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask( __name__ )
app.secret_key = 'S3cretK3y'
EMAIL_REGEX = re.compile( r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$' )

@app.route( '/' )
def index():
	return render_template( 'index.html' )

@app.route( '/register', methods = [ 'POST' ] )
def register():
	rf = request.form
	if len( rf[ 'firstName' ] ) < 1:
		flash( u'First name can not be empty', 'error' )
	elif not rf[ 'firstName' ].isalpha():
		flash( u'First name can not have numbers', 'error' )
	elif len( rf[ 'lastName' ] ) < 1:
		flash( u'Last name can not be empty', 'error' )
	elif not rf[ 'lastName' ].isalpha():
		flash( u'Last name can not have numbers', 'error' )
	elif len( rf[ 'email' ] ) < 1:
		flash( u'Email can not be empty', 'error' )
	elif not EMAIL_REGEX.match( rf[ 'email' ] ):
		flash( u'Invalid email address', 'error' )
	elif len( rf[ 'password' ] ) < 8:
		flash( u'Password must have more than 8 characters', 'error' )
	elif rf[ 'password' ] != rf[ 'confirmation' ]:
		flash( u'Password does not match confirmation', 'error' )
	elif len( rf[ 'confirmation' ] ) < 1:
		flash( u'Password Confirmation can not be empty', 'error')
	else:
		flash( u'Thanks for submitting your information.', 'success' )
	return redirect( '/' )

app.run( debug = True )