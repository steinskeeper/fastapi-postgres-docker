from fastapi import APIRouter, Depends
from app.db.models import User
from app.db.base import db

from app.auth.auth_utils import requires_auth, email_verify_token


users = APIRouter()


@users.get('/profile')
async def get_profile(user_id=Depends(email_verify_token)):
    '''
    input args : the user_id
    returns all the data of the user
    '''

    u_dat = db.query(User).filter(User.user_id == user_id).first()

    return {
        'success': True,
        'user': u_dat.format(),

    }


@users.patch('/edit-profile')
async def edit_profile(payload: dict, user_id=Depends(email_verify_token)):
    '''
    payload = {
        name:
        bio:
        # role:
    }
    '''

    profile = db.query(User).filter(User.user_id == user_id).first()

    profile.name = payload['name']
    profile.bio = payload['bio']

    profile.update()

    return {
        'success': True,
        'profile': profile.format_short()
    }
