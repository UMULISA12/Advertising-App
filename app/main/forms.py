from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField
from wtforms.validators import Required
from werkzeug import secure_filename
from flask_wtf.file import FileField

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')   


class AdvertForm(FlaskForm):

    advertisorname = StringField('Write your name', validators=[Required()])
    advertname = StringField('Name of your product',validators=[Required()])
    category=SelectField('Category:',choices=[('first-hand','First-hand'),('second-hand','Second-hand')])
    Photo = FileField('Your photo', validators=[Required()])
    description = TextAreaField('add details', validators=[Required()])
    location = StringField('Add location', validators=[Required()])
    phone = StringField("Number", validators=[Required()] )
    Submit = SubmitField('Submit')

class SubscriberForm(FlaskForm):
    name = StringField("Enter your name")
    email = StringField("Email", validators=[Required()])
    submit= SubmitField('Subscribe')

class CommentForm(FlaskForm):
    comment= TextAreaField('comment', validators=[Required()])
    author = StringField('enter your name', validators=[Required()])
    Submit = SubmitField('Submit')