from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return Advertisor.query.get(int(user_id))


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String(255))
    phone = db.Column(db.Integer())
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    rel_comment= db.relationship('Comment', backref='user', lazy='dynamic')
    rel_subscribe= db.relationship('Subscribe', backref='user', lazy='dynamic')

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls, id):
        comment = Comment.query.filter_by(blog_id=id).all()
        return comment


class Advertisor(UserMixin,db.Model):

    __tablename__ = 'advertisors'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    phone_number = db.Column(db.Integer)
    pic_path = db.Column(db.String())
    bio= db.Column(db.String)
    pass_secure = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    rel_advert= db.relationship('Advert', backref='advertisors', lazy='dynamic')
    rel_post= db.relationship('Post', backref='advertisors', lazy='dynamic')
  

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f' {self.username}'

#UserMixin,
class Role(db.Model):
   __tablename__="roles"

   id = db.Column(db.Integer, primary_key=True)
   role_name = db.Column(db.String(255))
   rel_users = db.relationship('User', backref = 'role1', lazy = 'dynamic')
   rel_advertisor = db.relationship('Advertisor', backref = 'role2', lazy = 'dynamic')


#    def save_subscriber(self):
#        db.session.add(self)
#        db.session.commit()

#    @classmethod
#    def get_subscribers(cls,id):
#        return Subscriber.query.all()


#    def __repr__(self):
#        return f'User {self.email}'


class Advert(db.Model):

    __tablename__ = 'adverts'

    id = db.Column(db.Integer,primary_key = True)
    advert_name = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    advertisor_id = db.Column(db.Integer, db.ForeignKey("advertisors.id"))
    rel_comment= db.relationship('Comment', backref='adverts', lazy='dynamic')
    rel_subscribe= db.relationship('Subscribe', backref='adverts', lazy='dynamic')
    rel_post= db.relationship('Post', backref='adverts', lazy='dynamic')

    # advertisor_id = db.relationship('Advertisor', backref='advert', lazy='dynamic')

    # def save_advert(self):
    #     db.session.add(self)
    #     db.session.commit()

    # @classmethod
    # def get_adverts(cls, user_id):
    #     advert = Adverts.query.filter_by(id=user_id).all()
    #     return advert


class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer,primary_key = True)
    category_name = db.Column(db.String)
    # advertisor_id = db.Column(db.Integer, db.ForeignKey("advertisors.id"))
    rel_advert= db.relationship('Advert', backref='categories', lazy='dynamic')
    rel_subscribe= db.relationship('Subscribe', backref='categories', lazy='dynamic')
    rel_post= db.relationship('Post', backref='categories', lazy='dynamic')

    # def save_advert(self):
    #     db.session.add(self)
    #     db.session.commit()

    # @classmethod
    # def get_adverts(cls, user_id):
    #     advert = Adverts.query.filter_by(id=user_id).all()
    #     return advert


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    advert_id = db.Column(db.Integer, db.ForeignKey("adverts.id"))

    # advert_id = db.relationship('Advert', backref='comment', lazy='dynamic')

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls, id):
        comment = Comment.query.filter_by(advert_id=id).all()
        return comment




class Subscribe(db.Model):
   __tablename__="subscribes"

   id = db.Column(db.Integer, primary_key=True)
   description = db.Column(db.String(255))
   email = db.Column(db.String(255))
   user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
   category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
   advert_id = db.Column(db.Integer, db.ForeignKey("adverts.id"))
#    advert_id = db.relationship('Advert', backref='comment', lazy='dynamic')
   

   def save_subscribe(self):
       db.session.add(self)
       db.session.commit()

   @classmethod
   def get_subscribes(cls,id):
       return Subscriber.query.all()


   def __repr__(self):
       return f'User {self.email}'




class Post(db.Model):
   __tablename__="posts"

   id = db.Column(db.Integer, primary_key=True)
   advert_id = db.Column(db.Integer, db.ForeignKey("adverts.id"))
   category_id =  db.Column(db.Integer, db.ForeignKey("categories.id"))
   advertisor_id =  db.Column(db.Integer, db.ForeignKey("advertisors.id"))

   

   def save_post(self):
       db.session.add(self)
       db.session.commit()

   @classmethod
   def get_posts(cls,id):
       return Post.query.all()


class Map:
    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self. quote = quote