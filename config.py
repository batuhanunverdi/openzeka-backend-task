from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://openzeka_owner:DMaUYHBqx2j1@ep-lingering-hill-a224dnmm.eu-central-1.aws.neon.tech/openzeka?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
