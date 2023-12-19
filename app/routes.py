from flask import render_template, flash, redirect, url_for
from app.email import send_password_reset_email
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm, ManpowerEntryForm, MachineryEntryForm, MaterialEntryForm, MoneyEntryForm
from flask import request
from werkzeug.urls import url_parse
from app import app
from app.models.user import User
from werkzeug.utils import secure_filename
import os
from app.models.machinery import Machinery
from app.models.material import Material
from app.models.manpower import Manpower

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi'}

def allowed_file(filename):
        return '.' in filename and \
                           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():
    images_folder = '/home/rukundo/test/app/static/images'
    images = os.listdir(images_folder)
    images_path = [f'images/{image}' for image in images if image.startswith('profile')]
    return render_template('homepage.html', title='Home Page', images=images_path)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        from app.models import storage
        user = storage.check_user(User, form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dash')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.save()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        from app.models import storage
        user = storage.load_user_by_email(User, email=form.email.data)
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        user.save()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/materials')
def materials():
    from app.models import storage
    from app.models.material import Material
    materials = storage.all(Material)
    sorted_materials = sorted(materials.values(), key=lambda x: x.category)
    categories = []
    for material in sorted_materials:
        if material.category not in categories:
            categories.append(material.category)
    return render_template('material.html', materials=sorted_materials, categories=categories)

@app.route('/machineries')
def machineries():
    from app.models import storage
    from app.models.machinery import Machinery
    machineries = storage.all(Machinery)
    sorted_machineries = sorted(machineries.values(), key=lambda x: x.category)
    print(sorted_machineries)
    categories = []
    for machinery in sorted_machineries:
        if machinery.category not in categories:
            categories.append(machinery.category)
    print(categories)
    return render_template('machinery.html', machineries=sorted_machineries, categories=categories)

@app.route('/management')
def management():
    return render_template('management.html')

@app.route('/money')
def money():
    return render_template('money.html')

@app.route('/manpowers')
def manpowers():
    from app.models import storage
    from app.models.manpower import Manpower
    manpowers = storage.all(Manpower)
    sorted_manpowers = sorted(manpowers.values(), key=lambda x: x.profession)
    categories = []
    for manpower in sorted_manpowers:
        if manpower.profession not in categories:
            categories.append(manpower.profession)
    return render_template('manpower.html', manpowers=sorted_manpowers, categories=categories)

@app.route('/search_results')
def search_results():
    query = request.args.get('query')
    page_name = request.args.get('page')
    classes = {
            'manpower': [Manpower, 'manpower.html', 'profession'],
            'machinery': [Machinery, 'machinery.html', 'category'],
            'material': [Material, 'material.html', 'category']
            }
    class_data = classes.get(page_name, None)
    class_name = class_data[0]
    if class_name and query:
        from app.models import storage
        objs = storage.all(class_name)
        print(query)
        category = class_data[2]

        def attribute_match(obj):
            # Iterate over all attributes of the object
            for attribute_name in dir(obj):
                attribute_value = getattr(obj, attribute_name)
                # Check if the query matches the attribute value
                if isinstance(attribute_value, str) and query.lower() in attribute_value.lower():
                    return attribute_value
                return None
        sorted_objs = sorted(objs.values(), key=attribute_match)
        print(sorted_objs)
        categories = []
        for obj in sorted_objs:
            category_name = getattr(obj, category, None)
            if category_name not in categories:
                categories.append(category_name)
        return render_template(class_data[1], manpowers=sorted_objs, categories=categories)
    return {page_name: query}

@app.route('/dashboard')
@login_required
def dash():
    return render_template('dashboard.html')

@app.route('/add_manpower', methods=['GET', 'POST'])
def add_manpower():
    form = ManpowerEntryForm()
    if form.validate_on_submit():
        args = {}
        profile = form.profile.data
        if profile and allowed_file(profile.filename):
            filename = secure_filename(profile.filename)
            profile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            args['profile'] = os.path.join('images/', filename)
        cv = form.cv_file.data
        if cv and allowed_file(cv.filename):
            filename = secure_filename(cv.filename)
            cv.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            args['cv'] = os.path.join('images/', filename)
        args['first_name'] = form.first_name.data
        args['last_name'] = form.last_name.data
        args['sex'] = form.sex.data
        args['experience'] = form.experience.data
        args['profession'] = form.profession.data
        args['email'] = form.email.data
        args['contacts'] = form.contacts.data
        args['country'] = form.country.data
        args['city'] = form.city.data
        args['date_of_birth'] = form.date_of_birth.data
        args['wage_per_hour'] = form.wage_per_hour.data

        from app.models.manpower import Manpower
        manpower = Manpower(**args)
        manpower.save()
        flash('You have successfully added new manpower!')
        return redirect(url_for('dash'))
    return render_template('add_manpower.html', form=form)

@app.route('/add_material', methods=['GET', 'POST'])
def add_material():
    form = MaterialEntryForm()

    if form.validate_on_submit():
        args = {}
        # Handle picture upload
        picture = form.picture.data
        if picture and allowed_file(picture.filename):
            filename = secure_filename(picture.filename)
            picture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            args['picture'] = os.path.join('images/', filename)

        # Handle tutorial video upload
        tutorial_video = form.tutorial_video.data
        if tutorial_video and allowed_file(tutorial_video.filename):
            video_filename = secure_filename(tutorial_video.filename)
            tutorial_video.save(os.path.join(app.config['UPLOAD_FOLDER'], video_filename))
            args['tutorial_video'] = os.path.join('images/', video_filename)
        # ... other form fields ...
        args['name'] = form.name.data
        args['category'] = form.category.data
        args['rent'] = form.rent.data
        args['price'] = form.price.data
        args['description'] = form.description.data
        args['vendor'] = form.vendor.data
        args['vendor_email'] = form.vendor_email.data
        args['vendor_contacts'] = form.vendor_contacts.data
        args['vendor_country'] = form.vendor_country.data

        from app.models.material import Material
        material = Material(**args)
        material.save()

        flash('You have successfully added new material!')
        return redirect(url_for('dash'))

    return render_template('add_material.html', form=form)

@app.route('/add_machinery', methods=['GET', 'POST'])
def add_machinery():
    form = MachineryEntryForm()

    if form.validate_on_submit():
        args = {}
        # Handle picture upload
        picture = form.picture.data
        if picture and allowed_file(picture.filename):
            filename = secure_filename(picture.filename)
            picture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            args['picture'] = os.path.join('images/', filename)

        # Handle tutorial video upload
        tutorial_video = form.tutorial_video.data
        if tutorial_video and allowed_file(tutorial_video.filename):
            video_filename = secure_filename(tutorial_video.filename)
            tutorial_video.save(os.path.join(app.config['UPLOAD_FOLDER'], video_filename))
            args['tutorial_video'] = os.path.join('images/', video_filename)
        # ... other form fields ...
        args['name'] = form.name.data
        args['category'] = form.category.data
        args['rent'] = form.rent.data
        args['price'] = form.price.data
        args['description'] = form.description.data
        args['vendor'] = form.vendor.data
        args['vendor_email'] = form.vendor_email.data
        args['vendor_contacts'] = form.vendor_contacts.data
        args['vendor_country'] = form.vendor_country.data

        from app.models.machinery import Machinery
        machinery = Machinery(**args)
        machinery.save()

        flash('You have successfully added new machinery!')
        return redirect(url_for('dash'))

    return render_template('add_machinery.html', form=form)

@app.route('/add_money', methods=['GET', 'POST'])
def add_money():
    form = MoneyEntryForm()
    if form.validate_on_submit():
        # Create a Money instance with the form data
        from app.models.money import Money
        money = Money(
            financing_option=form.financing_option.data,
            blog=form.blog.data
        )
        # Save the money instance to the database
        money.save()
        flash('You have successfully added new money entry!')
        return redirect(url_for('dash'))

    return render_template('add_money.html', form=form)
