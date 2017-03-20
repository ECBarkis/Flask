from flask import Flask, render_template, request, redirect

app = Flask( __name__ )

@app.route( '/' )
def index():
	return render_template( 'index.html' )

@app.route( '/ninja' )
@app.route( '/ninja/' )
def ninja():
	return render_template( 'ninja.html', ninja = 'tnmt' )

@app.route( '/ninja/<blue>' )
@app.route( '/ninja/<blue>/' )
def blue(blue):
	return render_template( 'ninja.html', ninja = blue )

@app.route( '/ninja/<orange>' )
@app.route( '/ninja/<orange>/' )
def orange(orange):
	return render_template( 'ninja.html', ninja = orange )

@app.route( '/ninja/<red>' )
@app.route( '/ninja/<red>/' )
def red(red):
	return render_template( 'ninja.html', ninja = red )

@app.route( '/ninja/<purple>' )
@app.route( '/ninja/<purple>/' )
def purple(purple):
	return render_template( 'ninja.html', ninja = purple )

app.run( debug = True )