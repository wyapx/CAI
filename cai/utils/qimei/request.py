import base64
import json
import time
from typing import Tuple, TypedDict

from dataclasses import dataclass
from .crypto import rsa_encrypt, calc_md5, AES
from cai.utils.httpcat import HttpCat


@dataclass()
class QueryData:
    crypt_key: str
    nonce: str
    ntime: int = int(time.time()) * 1000
    secret: str = "ZdJqM15EeO2zWc08"


class QImeiResult(TypedDict):
    q16: str
    q36: str


def _prepare_aes_crypter(crypt_key: bytes) -> Tuple[str, AES]:
    key = base64.b64encode(
        rsa_encrypt(
            crypt_key
        )
    ).decode()
    return key, AES(crypt_key)


def _gen_query(data: QueryData, device: dict) -> dict:
    key, aes = _prepare_aes_crypter(data.crypt_key.encode())
    params = base64.b64encode(
        aes.encrypt(
            json.dumps(device).encode()
        )
    ).decode()
    sign = calc_md5(key, params, str(data.ntime), data.nonce, data.secret)
    return {
        'key': key,
        'params': params,
        'time': data.ntime,
        'nonce': data.nonce,
        'sign': sign,
        'extra': ''
    }


async def get_qimei(data: QueryData, device: dict) -> QImeiResult:
    resp = await HttpCat.request(
        "POST",
        "https://snowflake.qq.com/ola/android",
        body=json.dumps(_gen_query(data, device)).encode(),
        header={"Content-Type": "application/json"}
    )
    r = resp.json()
    if r["code"]:
        raise AssertionError(f"Get qimei fail, return code: {r['code']}")

    _, aes = _prepare_aes_crypter(data.crypt_key.encode())
    return json.loads(
        aes.decrypt(
            base64.b64decode(r["data"])
        )
    )
