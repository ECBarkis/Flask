from flask import Flask, render_template

app = Flask( __name__ )

@app.route( '/' )
def hello_world():
	return render_template( 'index.html', name = 'Elliot' )

@app.route( '/success' )
def success():
	return render_template( 'success.html', name = 'Elliot' )

app.run( debug = True )