#you must install jwt library via pip install pyjwt
import jwt
import datetime

# Define your secret key (this should be kept safe and not shared publicly)
SECRET_KEY = 'your_secret_key'

# Define the token claims
payload = {
    'sub': 'narender.singh@maersk.com',
    'iat': datetime.datetime.now(),
    'exp': datetime.datetime.now() + datetime.timedelta(hours=1)  # Token valid for 1 hour
}

# Create the JWT
token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

print(f'JWT: {token}')
