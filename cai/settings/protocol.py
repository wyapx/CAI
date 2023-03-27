"""Application Protocol setting

This module is used to get or new the application protocol setting.
Protocol settings will be stored in APP_DIR provided by storage manager.
Once the protocol setting is loaded, it will be cached until application shut down.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""
import dataclasses
import warnings


@dataclasses.dataclass(frozen=True)
class ApkInfo:
    apk_id: str
    app_id: int
    sub_app_id: int  # com.tencent.common.config.AppSetting.f
    version: str
    apk_sign: bytes
    build_time: int  # oicq.wlogin_sdk.tools.util.BUILD_TIME
    sdk_version: str  # oicq.wlogin_sdk.tools.util.SDK_VERSION
    sso_version: int  # oicq.wlogin_sdk.tools.util.SSO_VERSION
    bitmap: int  # oicq.wlogin_sdk.request.WtloginHelper.mMiscBitmap | 0x2000000
    main_sigmap: int  # com.tencent.mobileqq.msf.core.auth.n.f
    sub_sigmap: int  # oicq.wlogin_sdk.request.WtloginHelper.mSubSigMap

    device_type: str


class Protocols:
    class Android:
        PHONE = ApkInfo(
            apk_id="com.tencent.mobileqq",
            app_id=16,
            sub_app_id=537153294,
            version="8.9.33.10440",
            build_time=1676531414,
            apk_sign=bytes(
                [
                    0xA6,
                    0xB7,
                    0x45,
                    0xBF,
                    0x24,
                    0xA2,
                    0xC2,
                    0x77,
                    0x52,
                    0x77,
                    0x16,
                    0xF6,
                    0xF3,
                    0x6E,
                    0xB6,
                    0x8D,
                ]
            ),
            sdk_version="6.0.0.2535",
            sso_version=19,
            bitmap=150470524,
            main_sigmap=16724722,
            sub_sigmap=0x10400,
            device_type="Android Phone"
        )

        PAD = ApkInfo(
            apk_id="com.tencent.mobileqq",
            app_id=16,
            sub_app_id=537152242,
            version="8.9.33.10335",
            build_time=1676531414,
            apk_sign=bytes(
                [
                    0xA6,
                    0xB7,
                    0x45,
                    0xBF,
                    0x24,
                    0xA2,
                    0xC2,
                    0x77,
                    0x52,
                    0x77,
                    0x16,
                    0xF6,
                    0xF3,
                    0x6E,
                    0xB6,
                    0x8D,
                ]
            ),
            sdk_version="6.0.0.2535",
            sso_version=19,
            bitmap=150470524,
            main_sigmap=16724722,
            sub_sigmap=0x10400,
            device_type="Android Pad"
        )

        WATCH = ApkInfo(
            apk_id="com.tencent.qqlite",
            app_id=16,
            sub_app_id=537065138,
            version="2.0.8",
            build_time=1559564731,
            apk_sign=bytes(
                [
                    0xA6,
                    0xB7,
                    0x45,
                    0xBF,
                    0x24,
                    0xA2,
                    0xC2,
                    0x77,
                    0x52,
                    0x77,
                    0x16,
                    0xF6,
                    0xF3,
                    0x6E,
                    0xB6,
                    0x8D,
                ]
            ),
            sdk_version="6.0.0.2365",
            sso_version=5,
            bitmap=16252796,
            main_sigmap=34869472,
            sub_sigmap=0x10400,
            device_type="Android Watch"
        )

    IPAD = ApkInfo(
        apk_id="com.tencent.minihd.qq",
        app_id=16,
        sub_app_id=537118796,
        version="5.9.3",
        build_time=1595836208,
        apk_sign=bytes(
            [
                170,
                57,
                120,
                244,
                31,
                217,
                111,
                249,
                145,
                74,
                102,
                158,
                24,
                100,
                116,
                199,
            ]
        ),
        sdk_version="6.0.0.2433",
        sso_version=12,
        bitmap=150470524,
        main_sigmap=1970400,
        sub_sigmap=66560,
        device_type="iPad"
    )
    MACOS = ApkInfo(
        apk_id="com.tencent.qq",
        app_id=16,
        sub_app_id=537128930,
        version="5.8.9",
        build_time=1595836208,
        apk_sign=bytes(
            [
                170,
                57,
                120,
                244,
                31,
                217,
                111,
                249,
                145,
                74,
                102,
                158,
                24,
                100,
                116,
                199,
            ]
        ),
        sdk_version="6.0.0.2433",
        sso_version=12,
        bitmap=150470524,
        main_sigmap=1970400,
        sub_sigmap=66560,
        device_type="MacOS"
    )


def get_apk_info(_type: str = "IPAD") -> ApkInfo:
    warnings.warn(
        "get_apk_info will be remove in the future, use Protocols class instead.",
        DeprecationWarning
    )
    info = {
        "IPAD": Protocols.IPAD,
        "ANDROID_PHONE": Protocols.Android.PHONE,
        "ANDROID_WATCH": Protocols.Android.WATCH,
        "MACOS": Protocols.MACOS,
    }
    if _type not in info:
        raise ValueError(f"Invalid Protocol Type: {_type}")
    return info[_type]
