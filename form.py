from flask import Flask,request,render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,BooleanField,DateTimeField,
					RadioField,SelectField,TextField,
					TextAreaField)
from wtforms.validators import DataRequired
app = Flask(__name__)

app.config['SECRET_KEY']='mysecretkey'

class InfoForm(FlaskForm):

	breed = StringField(' what breed are you ',validators=[DataRequired()])
	neutered = BooleanField('have you been neutered')
	mood = RadioField('please choose your mood',choices=[('mood_one','happy'),('mood_two','Excited')])
	food_choice = SelectField('picck your food',choices=[('chi','chicken'),('bf','beef'),('fish','fish')])
	feedback = TextAreaField()
	submit = SubmitField('submit')



@app.route('/', methods=['GET','POST'])
def index():

	# breed=False

	# form = InfoForm()

	# if form.validate   _on_submit():

	# 	breed=form.breed.data
	# 	form.breed.data = ''

	form = InfoForm()
	if form.validate_on_submit():
		flash('you just enterd here!')
		session['breed']=form.breed.data 
		session['neutered']=form.neutered.data
		session['mood'] = form.mood.data
 		session['feedback'] = form.feedback.data

		return redirect(url_for('thankyou'))
 
	return render_template('index.html',form=form)



@app.route('/thankyou')
def thankyou():
	return render_template('thankyou.html')











