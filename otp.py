import secrets
import string
def generate_otp(length=5):
    digits=string.digits
    otp=''.join(secrets.choice(digits) for _ in range(length))
    return int(otp)
    
