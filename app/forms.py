from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.models import User


class ResetPasswordForm(FlaskForm):
    username = StringField('Username',
                          validators=[DataRequired(), Length(min=3, max=80)])
    new_password = PasswordField('New Password',
                                validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(),
                                              EqualTo('new_password', message='Passwords must match')])
    submit = SubmitField('Reset Password')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('Username does not exist')
