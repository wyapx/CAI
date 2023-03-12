import warnings

_DEVICE_INFO = {
    "androidId": "HomoOS",
    "platformId": 1,
    "appKey": "0S200MNJT807V3GE",
    "appVersion": "8.9.28.3700",
    "beaconIdSrc": "k1:2023-03-01123321.929000000;k2:2019-09-10185536.244626911;k3:0000000000000000;k4:8c829c5f2697bfed;k5:3264102;k6:843776;k7:507860;k8:131072;k9:7e0ad37b-4045-45d9-9765-428e5f90ea60;k11:0;k12:4;k13:2023-03-01123318.800000000;k14:2023-03-01000159.756000000;k15:1;k16:15;k17:2023-03-01123411.099000000;k18:2023-03-01123323.549000000;k19:16386;k20:66;k21:2023-03-01123314.030000000;k22:2019-09-10185447.459986909;k23:8207;k24:2;k25:2023-03-01123257.690000000;k26:2023-03-01123257.690000000;k27:4081;k28:10;k29:2023-03-01123257.690000000;k30:2023-03-01123257.690000000;k31:6480;k32:1;k33:2023-03-01123414.459000000;k34:2023-03-01123421.889000000;k35:3;k36:35;k37:2023-03-01002617.121000000;k38:2023-03-01000200.276000000;k39:2;k40:3;k10:1",
    "brand": "HUAWEI",
    "channelId": "2021",
    "cid": "",
    "imei": "",
    "imsi": "",
    "mac": "",
    "model": "",
    "networkType": "unknown",
    "oaid": "",
    "osVersion": "Android 11.0,level 30",
    "qimei": "",
    "qimei36": "",
    "sdkVersion": "1.2.13.6",
    "targetSdkVersion": "26",
    "audit": "",
    "userId": "{}",
    "packageId": "com.tencent.mobileqq",
    "deviceType": "Pad",
    "sdkName": "",
    "reserved": "{\"harmony\":\"0\",\"clone\":\"0\",\"containe\":\"\",\"oz\":\"UhYmelwouA+V2nPWbOvLTgN2\\\/m8jwGB+yUB5v9tysQg=\",\"oo\":\"Xecjt+9S1+f8Pz2VLSxgpw==\",\"kelong\":\"0\",\"uptimes\":\"2023-03-01 12:32:57\",\"multiUser\":\"0\",\"bod\":\"SM7250-AB-\",\"brd\":\"OPPO\",\"dv\":\"PCRT00\",\"firstLevel\":\"\",\"manufact\":\"OPPO\",\"name\":\"PCRT00\",\"host\":\"se.infra\",\"kernel\":\"Linux localhost 4.14.253-android+ #754 SMP Wed Nov 9 17:04:03 CST 2022 armv8\"}"
}


def device_info(**update) -> dict:
    di = _DEVICE_INFO
    for k, v in update.items():
        if k not in di:
            warnings.warn(f"attribute {k} not in DeviceInfo")
        di[k] = v
    return di
