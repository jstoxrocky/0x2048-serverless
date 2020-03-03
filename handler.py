import json
import redis
from webserver import (
    nonce,
)

def new_session(event, context):
    '''
    Reset session data with new session ID and challenge
    Send challenge and session_id "cookie" back to client
    '''
    sessions = redis.Redis()
    session_id = nonce().hex()
    challenge = nonce().hex()
    session_data = {
        'paid': False,
        'challenge': challenge
    }
    sessions.set(session_id, json.dumps(session_data))
    payload = {
        'session_id': session_id,
        'challenge': challenge,
    }
    return json.dumps(payload)


def new_game(event, context):
    nonce = session['nonce']
    confirmation = confirm_payment(nonce, signature)
    # new_game = 
    return json.dumps({
        'session_id': session_id,
    })