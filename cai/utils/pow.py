import hashlib
import struct
import time

from cai.utils.binary import Packet


def t546_challenge(data: bytes) -> bytes:
    """

    Args:
        data: t546 raw

    Returns:
        t547

    Notes:
        CalcPoW
        migrated from mirai, thanks a lot.
    """
    ver, algorithm_type, hash_type, src, tgt, cpy = (
        Packet(data)
        .byte()
        .int8()
        .byte()
        .offset(5)
        .bytes_with_length(2)
        .bytes_with_length(2)
        .bytes_with_length(2)
        .execute()
    )

    elp, cnt = 0, 0
    if len(tgt) != 32:
        raise ValueError("Parser err: invalid tgt")
    elif algorithm_type == 2:
        start = time.time()
        tmp = int.from_bytes(src, "big", signed=False)
        hash_it = lambda x: hashlib.sha256(x.to_bytes(128, "big")).digest()
        hash_current = hash_it(tmp)
        while hash_current != tgt:
            tmp += 1
            hash_current = hash_it(tmp)
            cnt += 1
        dst = tmp.to_bytes(128, "big")
        elp = int((time.time() - start) * 1000)
    else:
        raise TypeError(f"Unknown algorithm type: {algorithm_type}")

    ret = bytearray(data)
    ret[3] = 0x01
    return ret + struct.pack("!H128sII", 128, dst, elp, cnt)
