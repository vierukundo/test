"""Importing different modules"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, SelectField, DateField, DecimalField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Optional, Length
from flask_wtf.file import FileRequired
from app.models.user import User

African_countries = [
    ('Algeria', 'Algeria'),
    ('Angola', 'Angola'),
    ('Benin', 'Benin'),
    ('Botswana', 'Botswana'),
    ('Burkina Faso', 'Burkina Faso'),
    ('Burundi', 'Burundi'),
    ('Cabo Verde', 'Cabo Verde'),
    ('Cameroon', 'Cameroon'),
    ('Central African Republic', 'Central African Republic'),
    ('Chad', 'Chad'),
    ('Comoros', 'Comoros'),
    ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'),
    ('Djibouti', 'Djibouti'),
    ('Egypt', 'Egypt'),
    ('Equatorial Guinea', 'Equatorial Guinea'),
    ('Eritrea', 'Eritrea'),
    ('Eswatini', 'Eswatini'),
    ('Ethiopia', 'Ethiopia'),
    ('Gabon', 'Gabon'),
    ('Gambia', 'Gambia'),
    ('Ghana', 'Ghana'),
    ('Guinea', 'Guinea'),
    ('Guinea-Bissau', 'Guinea-Bissau'),
    ('Ivory Coast', 'Ivory Coast'),
    ('Kenya', 'Kenya'),
    ('Lesotho', 'Lesotho'),
    ('Liberia', 'Liberia'),
    ('Libya', 'Libya'),
    ('Madagascar', 'Madagascar'),
    ('Malawi', 'Malawi'),
    ('Mali', 'Mali'),
    ('Mauritania', 'Mauritania'),
    ('Mauritius', 'Mauritius'),
    ('Morocco', 'Morocco'),
    ('Mozambique', 'Mozambique'),
    ('Namibia', 'Namibia'),
    ('Niger', 'Niger'),
    ('Nigeria', 'Nigeria'),
    ('Rwanda', 'Rwanda'),
    ('Sao Tome and Principe', 'Sao Tome and Principe'),
    ('Senegal', 'Senegal'),
    ('Seychelles', 'Seychelles'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Somalia', 'Somalia'),
    ('South Africa', 'South Africa'),
    ('South Sudan', 'South Sudan'),
    ('Sudan', 'Sudan'),
    ('Tanzania', 'Tanzania'),
    ('Togo', 'Togo'),
    ('Tunisia', 'Tunisia'),
    ('Uganda', 'Uganda'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
]

WAGE_CHOICES = [
        ('10-15', '10 - 15 USD'),
        ('15-20', '15 - 20 USD'),
        ('20-30', '20 - 30 USD'),
        ('30-40', '30 - 40 USD'),
        ('40-50', '40 - 50 USD'),
        ('50-80', '50 - 80 USD'),
        ('80-100', '80 - 100 USD'),
        ('100+', 'Over 100 USD'),
]

class LoginForm(FlaskForm):
    """Represents the login form"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    """Represents user registration form"""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
            'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """Checks first if user is not registered"""
        from app.models import storage
        user = storage.check_user(User, username=username.data)
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        """Checks first if user email is not registered"""
        from app.models import storage
        user = storage.load_user_by_email(User, email=email.data)
        if user is not None:
            raise ValidationError('Please use a different email address.')

class ResetPasswordRequestForm(FlaskForm):
    """represents the password reset form"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    """represents the form where user fill new credentials"""
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class ManpowerEntryForm(FlaskForm):
    """Represents the manpower form"""
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Family name', validators=[DataRequired()])
    sex = StringField('Sex', validators=[DataRequired()])
    experience = StringField('Experience', validators=[DataRequired()])
    profession = StringField('Profession', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    contacts = StringField('Contacts', validators=[DataRequired()])
    country = SelectField('Country', choices=African_countries, validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()], format='%Y-%m-%d')
    profile = FileField('Profile Photo', validators=[FileRequired()])
    cv_file = FileField('CV', validators=[FileRequired()])
    wage_per_hour = SelectField('Wage per Hour (USD)', choices=WAGE_CHOICES, validators=[DataRequired()])

class MaterialEntryForm(FlaskForm):
    """Defines field form for materials"""
    name = StringField('Material Name', validators=[DataRequired()])
    category = StringField('Category of material', validators=[DataRequired()])
    picture = FileField('Upload Picture', validators=[DataRequired()])
    rent = BooleanField('Available for Rent')
    price = DecimalField('Price (USD)', validators=[Optional()])
    description = TextAreaField('Description', validators=[DataRequired()])
    tutorial_video = FileField('Upload Tutorial Video', validators=[Optional()])
    vendor = StringField('Vendor', validators=[Optional()])
    vendor_email = StringField('Vendor Email', validators=[Optional(), Email()])
    vendor_contacts = StringField('Vendor Contacts', validators=[Optional()])
    vendor_country = StringField('Vendor Country', validators=[Optional()])

class MachineryEntryForm(FlaskForm):
    """Defines field form for machineries"""
    name = StringField('Machinery Name', validators=[DataRequired()])
    category = StringField('Machinery category', validators=[DataRequired()])
    picture = FileField('Upload Picture', validators=[DataRequired()])
    rent = BooleanField('Available for Rent')
    price = DecimalField('Price (USD)', validators=[Optional()])
    description = TextAreaField('Description', validators=[DataRequired()])
    tutorial_video = FileField('Upload Tutorial Video', validators=[Optional()])
    vendor = StringField('Vendor', validators=[Optional()])
    vendor_email = StringField('Vendor Email', validators=[Optional(), Email()])
    vendor_contacts = StringField('Vendor Contacts', validators=[Optional()])
    vendor_country = StringField('Vendor Country', validators=[Optional()])

class MoneyEntryForm(FlaskForm):
    """Defines fields form for manpower"""
    financing_option = TextAreaField('Financing Option', validators=[DataRequired(), Length(max=1024)])
    blog = StringField('Blog', validators=[DataRequired(), Length(max=255)])
