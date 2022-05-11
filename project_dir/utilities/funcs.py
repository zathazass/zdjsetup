from random import choices
from string import ascii_uppercase, digits
from cryptography.fernet import Fernet
from django.conf import settings


def generate_otp():
    '''
    Returns 6-digit random alpha-number as OTP
    '''
    alpha_numeric_str = ascii_uppercase + digits
    return ''.join(choices(alpha_numeric_str, k=6))


def encrypt_data(value):
    '''
    Encrypt data based on settings.CRYPTO_KEY which base64 random key
    '''
    F = Fernet(settings.CRYPTO_KEY.encode())
    return F.encrypt(value.encode()) if isinstance(value, str) else F.encrypt(value)


def decrypt_data(value):
    '''
    Decrypt data based on settings.CRYPTO_KEY which base64 random key
    '''
    F = Fernet(settings.CRYPTO_KEY.encode())
    return str(F.decrypt(bytes(value)), 'utf-8')


def make_a_new_crypto_key():
    '''
    Generates and returns a new crypto key
    '''
    return str(Fernet.generate_key(), 'utf-8')
