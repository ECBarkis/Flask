from flask import Flask, render_template, request, redirect

app = Flask( __name__ )

@app.route( '/' )
def index():
	return render_template( 'index.html' )

@app.route( '/result', methods = [ 'POST' ] )
def get_info():
	rf = request.form
	name = rf[ 'name' ]
	lang = rf[ 'language' ]
	loca = rf[ 'location' ]
	comment = rf[ 'comment' ]
	return redirect( '/result' )

@app.route( '/result' )
def result():
	return render_template( 'result.html' )

@app.route( '/goBack' )
def go_back():
	return redirect( '/' )

app.run( debug = True )