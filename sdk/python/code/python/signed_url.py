import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner

import json
import memory
import time

main()

def main():
    key_id = 'KF4ZWB2OGIN4A'
    url = 'https://d1za37rregmkz7.cloudfront.net/app1/var3.json'
    current_time = datetime.datetime.utcnow()
    expire_date = current_time + datetime.timedelta(minutes = 2)
    cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)
    signed_url = cloudfront_signer.generate_presigned_url(url, date_less_than=expire_date)
    print(signed_url)

def rsa_signer(message):
    with open('private-key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )    
        signer = private_key.signer(padding.PKCS1v15(), hashes.SHA1())
        signer.update(message)
        return signer.finalize()    