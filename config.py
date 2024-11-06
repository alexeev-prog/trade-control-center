import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
	SECRET_KEY = os.getenv('SECRET_KEY')
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///tradecontrolcenter.db'


class DevelopmentConfig(BaseConfig):
	"""Конфигурация для стадии разработки"""
	DEBUG = True
	SQLALCHEMY_ECHO = True
