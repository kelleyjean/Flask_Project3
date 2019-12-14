from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .BlogpostModel import BlogpostModel, BlogpostSchema
from .UserModel import UserModel, UserSchema

db = SQLAlchemy()

bcrypt = Bcrypt()

