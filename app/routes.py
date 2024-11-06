#!/usr/bin/python3
from random import randint
from datetime import datetime
from flask import Blueprint, render_template, url_for, redirect, request, flash, get_flashed_messages  # noqa: F401
from app.models import User, Article, Comment, Like, db

main_bp = Blueprint('main', __name__)


@main_bp.app_errorhandler(404)
def handle_404(error):
	return render_template('error.html', code=404, 
							description='Страница не найдена. Попробуйте проверить URL.',
							title='404'), 404


@main_bp.app_errorhandler(401)
def handle_401(error):
	return render_template('error.html', code=401, description='Доступ запрещен. Возможно, эта страница доступна для зарегистрированных пользователей.',
							title='401'), 401


@main_bp.route('/')
def index():
	return render_template('index.html', title='Главная')
