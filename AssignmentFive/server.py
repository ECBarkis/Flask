from flask import Flask, render_template, request, redirect, session
import random

app = Flask( __name__ )
app.secret_key = 'S3cr3tK3y'

@app.route( '/' )
def index():
	if not session[ 'gold' ]:
		session[ 'gold' ] = 0
	if not session[ 'activities' ]:
		session[ 'activities' ] = ''
	return render_template( 'index.html' )

@app.route( '/process_money', methods = [ 'POST' ] )
def process_money():
	rf = request.form
	if rf[ 'action' ] == 'farm':
		gold = random.randrange( 10, 21 )
		activities = 'Earned {} gold from the farm!\n'.format( gold )
		session[ 'gold' ] += gold
	if rf[ 'action' ] == 'cave':
		gold = random.randrange( 5, 11 )
		activities = 'Earned {} gold from the cave!\n'.format( gold )
		session[ 'gold' ] += gold
	if rf[ 'action' ] == 'house':
		gold = random.randrange( 2, 6 )
		activities = 'Earned {} gold from the house!\n'.format( gold )
		session[ 'gold' ] += gold
	if rf[ 'action' ] == 'casino':
		gold = random.randrange( -50, 50 )
		if gold < 0:
			activities = 'Entered a casino and lost {} gold... Ouch..\n'.format( gold )
			session[ 'gold' ] += gold
		if gold > 0:
			activities = 'Entered a casino and won {} gold... Sweet..\n'.format( gold )
			session[ 'gold' ] += gold
		if gold == 0:
			activities = 'Entered a casino and broke even\n'
	activities += session[ 'activities' ]
	session[ 'activities' ] = activities
	return redirect( '/' )

@app.route( '/startOver', methods = [ 'POST' ] )
def startOver():
	session[ 'gold' ] = 0
	session[ 'activities' ] = ''
	return redirect( '/' )

app.run( debug = True )