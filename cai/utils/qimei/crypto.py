import os
import hashlib
from typing import Optional

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def rsa_encrypt(content: bytes, key_path: Optional[str] = None) -> bytes:
    if not key_path:
        key_path = os.path.join(__file__.rsplit(os.sep, 1)[0], "public_key.pem")
    with open(key_path, "rb") as f:
        key = serialization.load_pem_public_key(f.read())
    return key.encrypt(
        content,
        padding.PKCS1v15()
    )


def calc_md5(*multi_string) -> str:
    md5 = hashlib.md5()
    for s in multi_string:
        md5.update(s if isinstance(s, bytes) else s.encode())
    return md5.hexdigest()


class AES:
    block_size = 16

    def __init__(self, key: bytes):
        self._cipher = Cipher(algorithms.AES(key), modes.CBC(key))

    @staticmethod
    def _pad(v: bytes) -> bytes:
        padding_size = AES.block_size - len(v) % AES.block_size
        return v + (padding_size * chr(padding_size)).encode()

    @staticmethod
    def _unpad(v: bytes) -> bytes:
        return v[:-v[-1]]

    def encrypt(self, content: bytes) -> bytes:
        enc = self._cipher.encryptor()
        return enc.update(self._pad(content)) + enc.finalize()

    def decrypt(self, content: bytes) -> bytes:
        dec = self._cipher.decryptor()
        return self._unpad(dec.update(content) + dec.finalize())
