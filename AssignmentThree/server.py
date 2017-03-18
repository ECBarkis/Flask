from flask import Flask, render_template, request, redirect, session

app = Flask( __name__ )
app.secret_key = 'ThisIsASecret'

@app.route( '/' )
def index():
	session['counter'] += 1
	return render_template( 'index.html', visits = session['counter'] )

@app.route( '/addTwo' )
def add_two():
	session['counter'] += 1
	return redirect( '/' )

@app.route( '/reset' )
def reset():
	session['counter'] = 0
	return redirect( '/' )

app.run( debug = True )