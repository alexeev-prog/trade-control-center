from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from app.auth import login

db = SQLAlchemy()


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)


class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tags = db.Column(db.Text, nullable=False)
	title = db.Column(db.String(128), nullable=False)
	intro = db.Column(db.String(1024), nullable=False)
	price = db.Column(db.Float, nullable=False, default=0.0)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
	user = db.relationship('User', backref=db.backref('articles', lazy=True))


class Article(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tags = db.Column(db.Text, nullable=False)
	article_category = db.Column(db.String(64), nullable=False)
	title = db.Column(db.String(80), nullable=False)
	intro = db.Column(db.String(1024), nullable=False)
	text = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
	user = db.relationship('User', backref=db.backref('articles', lazy=True))


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
	user = db.relationship('User', backref=db.backref('comments', lazy=True))
	creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
	article = db.relationship('Article', backref=db.backref('comments', lazy=True))


class Like(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
	user = db.relationship('User', backref=db.backref('likes', lazy=True))
	article = db.relationship('Article', backref=db.backref('likes', lazy=True))


@login.user_loader
def load_user(id):
	return db.session.get(User, int(id))
