
from flask import render_template, redirect,url_for,abort,request
from flask_login import login_required, current_user
from . import main
from .forms import UpdateProfile, BlogForm, CommentForm, SubscriberForm
from ..models import User, Advertisor, Role, Advert, Category, Comment, Subscribe, Post, Map
from ..email import mail_message
from .. import db,photos
# from ..request import get_quotes

# import markdown2

@main.route('/')
def index():
    '''
    function that returns the index page
    '''
    title="Hello world"
    # blogs = Blog.query.all()
    return render_template('index.html',title=title)
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

# @main.route('/comment/<id>')
# def comment(id):
#     '''
#     function to return the comment
#     '''
#     comment = Comment.get_comment(id)
#     print(comment)
#     title = 'comments'
#     return render_template('comment.html',title = title, comment = comment)

# @main.route('/new_comment/<int:id>', methods = ['GET', 'POST'])
# # @login_required
# def new_comment(id):
#     form = CommentForm()

#     if form.validate_on_submit():
#         writer = form.author.data
#         comm = form.comment.data

#         new_comment = Comment(comment = comm, blog_id = id, author= writer)
#         new_comment.save_comment()

#         return redirect(url_for('main.index'))

#     title = 'New Comment'
#     return render_template('new_comment.html', title = title, comment_form = form, pitch_id = id)

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

# @main.route('/blog/<id>')
# @login_required
# def blog(id):

#     post = Blog.query.filter_by(id=id).first()
#     db.session.delete(post)
#     db.session.commit()
#     print(post)

#     title = 'Delete blog'

#     return render_template('delete.html', title = title, blogs = post)

# @main.route('/del-comment/<id>')
# # @login_required
# def delcomment(id):
#     '''
#     function to delete comments
#     '''
#     comment = Comment.query.filter_by(id = id).first()
#     db.session.delete(comment)
#     db.session.commit()
#     print(comment)
#     title = 'delete comments'
#     return render_template('delete.html',title = title, comment = comment)

# @main.route('/subscribe',methods=["GET","POST"])
# def subscriber():
#     form=SubscriberForm()

#     if form.validate_on_submit():
#         subscriber = Subscriber(name=form.name.data,email=form.email.data)
#         db.session.add(subscriber)
#         db.session.commit()

#         mail_message("Welcome to my blog","email/welcome_user",subscriber.email,subscriber=subscriber)
#         return redirect(url_for('main.index'))
#         title = 'Subscribe'
#     return render_template('subscription.html',form=form)


# @main.route('/blog/edit/<int:id>', methods=['GET', 'POST'])
# @login_required
# def edit_blog(id):
#     """
#     Edit a blogpost in the database
#     """
#     new_blog=False

#     blog = Blog.query.get(id)
#     form = BlogForm()

#     if form.validate_on_submit():

#         blog.blog = form.blog.data

#         db.session.commit()

#         print('edited comment ')


#         return redirect(url_for('main.index'))

#     form.blog.data = blog.blog


#     return render_template('new_blog.html',action = 'Edit',new_blog = new_blog,blog_form = form,legend='Update Post')