
from flask import render_template, redirect,url_for,abort,request
from flask_login import login_required, current_user
from . import main
from .forms import AdvertForm, CommentForm, SubscriberForm, UpdateProfile
from app.models import User, Comment, Advertisor, Advert, Role, Category, Subscribe, Post
from ..email import mail_message
from .. import db, photos


@main.route('/')
def index():
    '''
    function that returns the index page
    '''
    title="Hello world"
    
    # adverts = Advert.query.all()
    return render_template('index.html',title=title)


# @main.route('/allAdverts')
# def adverts_list():
    
#     adverts = Advert.query.all()

#     return render_template('brand_new.html', adverts=adverts)


@main.route('/oneadvert/<int:id>', methods=['GET', 'POST'])
def one_advert(id):

    advert = Advert.query.get(id)
    form = CommentForm()
    advert = advert.query.filter_by(id=id).first()

    if form.validate_on_submit():
        new_advert = Comment(
            ratings=0,
            like=0,
            dislike=0,
            content=form.content.data,
            comments=advert)

        # save comment
        db.session.add(new_advert)
        db.session.commit()

    comments = advert.comments_id

    return render_template('brand_new.html', advert=advert, id=id, comment_form=form, comments=comments)

# @main.route('/new_blog', methods = ['GET','POST'])
# @login_required
# def new_blog():
#    form  =BlogForm()

#    if form.validate_on_submit():
#        blog = form.blog.data

#        new_blog = Blog(blog = blog, user_id = current_user.id)

#        new_blog.save_blog()

#        return redirect(url_for('main.index'))

#    title = 'New Blog'
#    return render_template('new_blog.html',title = title, blog_form = form)

@main.route('/new-brand')
def brand_new_category():
    '''
    function to return the comment
    '''
    form = AdvertForm()
    adverts = Advert.fetch_advert()
    title = 'brand_new'
    return render_template('brand_new.html',title = title, adverts=adverts)



@main.route('/second-hand')
def second_hand_category():
    '''
    function to return the comment
    '''

    title = 'brand_new'
    return render_template('brand_new.html',title = title)

@main.route('/new-ads', methods = ['GET', 'POST'])
@login_required
def advert():
    form = AdvertForm()

    if form.validate_on_submit():
        advert_name = form.advertname.data
        advertisor_phone = form.phone.data
        location = form.location.data
        photo = form.photo.data
        advertisor_name = form.advertisorname.data
        # category = form.category.data
    
        # advert_date = form.advertname.data
        advert_category = form.category.data
        # photo = form.photo.data
        description = form.description.data
        # location = form.location.data

        advert = Advert(advert_category = category, advertisor_name = advertisorname, advert_name = advert_name, photo = photo, description =description, location = location)

        advert.save_advert()

        return redirect(url_for('main.brand_new_category'))

    title = 'New Advert'
    return render_template('ads-form.html', title = title, ad_form = form, advert_id = id)


@main.route('/user/<uname>')
# @login_required

def profile(uname):
    user = Advertisor.query.filter_by(username = uname).first()

    # post = Blog.query.filter_by(user_id = current_user.id).all()
    # print(post)
    if user is None:
        abort(404)


    title = uname

    return render_template('profile/profile.html', user = user,title=title)# blogs = post,


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = Advertisor.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)   


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = Advertisor.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))     
