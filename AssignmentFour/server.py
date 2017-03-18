from flask import Flask, render_template, request, redirect, session
import random

app = Flask( __name__ )
app.secret_key = 'MySecr3t'

@app.route( '/' )
def index():
	if not session[ 'status' ]:
		session[ 'status' ] = 'start game'
	if not session[ 'number' ]:
		session[ 'number' ] = random.randrange( 0, 101 )
	return render_template( 'index.html' )

@app.route( '/guess', methods = [ 'POST' ] )
def guess():
	guess = int( request.form[ 'guess' ] )
	if guess > session[ 'number' ]:
		session['status'] = 'greater than'
	if guess < session[ 'number' ]:
		session['status'] = 'less than'
	if guess == session[ 'number' ]:
		session['status'] = 'perfect'
	return redirect( '/' )

@app.route( '/newGame', methods = [ 'POST' ] )
def startOver():
	session[ 'number' ] = random.randrange( 0, 101 )
	session[ 'status' ] = 'start game'
	return redirect( '/' )

app.run( debug = True )