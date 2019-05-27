from flask import Flask,render_template,redirect,flash,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app=FlaskForm(__name__)

app.config['SECRET_KEY']='mysecretkey'

class InfoForm(FlaskForm):
	breed=StringField('lets enter something here')
	submit=SubmitField('submit')

@app.route('/',methods=['GET','POST'])
def index():


	form=InfoForm()

	if form.validate_on_submit():
		session['breed']=form.breed.data
		flash(f'your breed is there {session['breed']}')

		return redirect(url_for('index'))
	return render_template('index.html',form=form)	

