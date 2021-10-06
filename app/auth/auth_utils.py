
from functools import wraps

from fastapi import FastAPI, Header

from google.oauth2 import id_token
from google.auth.transport import requests
from fastapi import Security, Depends, Request

from app.db.base import db
from app.db.models import User
import jwt


CLIENT_ID = 'ADD CLIENT ID'


def requires_auth(role):
    # decorator for checking authentication & permission
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args,request: Request, **kwargs):
            token = request.headers['Authorization']
            using = request.headers['Option']

            if using == "google":
                idinfo = google_verify_token(token)
                user = getUser(idinfo['email'])
            else:
                user = email_verify_token(token)
                user_id = user['user_id']

            return f(token, *args, **kwargs)
        return wrapper
    return requires_auth_decorator


def get_token_auth_header():
    token = token_jwt.headers['Authorization']
    if token is None:
        return abort(401)
    return token


def google_verify_token(token):
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
    
    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise ValueError('Wrong issuer.')
    
    return idinfo


# !!!!! THis is the only important auth util!!!!!
def email_verify_token(token_jwt: Request):
    token = token_jwt.headers['Authorization']
    data = jwt.decode(token, 'poppushpoppushpoppop')

    if (data == None):
        return None
    
    u_id = data['id']

    
    userinfo = db.query(User).filter(User.user_id == u_id).first()
    return userinfo.user_id



def getUser(email):
    user = db.query(User).filter(User.email == email).first()
    return user
