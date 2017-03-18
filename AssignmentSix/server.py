from flask import Flask, render_template, request, redirect, session, flash

app = Flask( __name__ )
app.secret_key = 's3cr3tK3y'

@app.route( '/' )
def index():
	return render_template( 'index.html' )

@app.route( '/result', methods = [ 'POST' ] )
def get_info():
	rf = request.form
	if len( rf[ 'name' ] ) < 1:
		flash( 'Name can not be empty' )
		return redirect( '/' )
	elif len( rf[ 'comment' ] ) < 1:
		flash( 'Comment can not be empty' )
		return redirect( '/' )
	elif len( rf[ 'comment' ] ) > 120:
		flash( 'Comment can not be over 120 characters')
		return redirect( '/' )
	session[ 'name' ] = rf[ 'name' ]
	session[ 'lang' ] = rf[ 'language' ]
	session[ 'loca' ] = rf[ 'location' ]
	session[ 'comm' ] = rf[ 'comment' ]
	return redirect( '/result' )

@app.route( '/result' )
def result():
	return render_template( 'result.html' )

@app.route( '/goBack' )
def go_back():
	return redirect( '/' )

app.run( debug = True )