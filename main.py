import requests, time, uuid, random

def register_device():
    _rticket=str((time.time()*1000)).split('.')[0]
    gen_time = str(int(time.time()*1000))
    openudid = "".join([random.choice("abcdefghijklmn1234567890") for i in range(16)])
    google_aid = str(uuid.uuid4())
    url = "https://applog.musical.ly/service/2/device_register/?app_language=es&language=es&region=ES&sys_region=ES&carrier_region=FR&carrier_region_v2=&build_number=7.7.0&timezone_offset=28800&timezone_name=Asia%2FShanghai&mcc_mnc=20815&is_my_cn=0&fp=&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=770&version_name=7.7.0&device_platform=android&ssmix=a&device_type=G011A&device_brand=google&os_api=19&os_version=4.4.4&openudid="+openudid+"&manifest_version_code=2018071950&resolution=720*1280&dpi=240&update_version_code=2018071950&_rticket="+_rticket+"&config_retry=b"
    payload = '{"magic_tag":"ss_app_log","header":{"display_name":"musical.ly","update_version_code":2018071950,"manifest_version_code":2018071950,"aid":1233,"channel":"googleplay","appkey":"5559e28267e58eb4c1000012","package":"com.zhiliaoapp.musically","app_version":"7.7.0","version_code":770,"sdk_version":"2.5.3.9.1","os":"Android","os_version":"11","os_api":30,"device_model":"sdk_gphone_x86","device_brand":"google","device_manufacturer":"Google","cpu_abi":"armeabi-v7a","build_serial":"unknown","release_build":"dfab4da_20180719","density_dpi":420,"display_density":"mdpi","resolution":"1794x1080","language":"en","mc":"02:15:B2:00:00:00","timezone":0,"access":"4g","not_request_sender":0,"carrier":"Android","mcc_mnc":"310260","rom":"6903271","rom_version":"RSR1.201013.001","google_aid":"'+google_aid+'","openudid":"'+openudid+'","serial_number":"unknown","sim_serial_number":[],"region":"US","tz_name":"GMT","tz_offset":0,"sim_region":"us"},"_gen_time":'+gen_time+'}'
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Host': 'applog.musical.ly',
        'User-Agent': 'okhttp/3.7.0.6'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()['device_id_str'], response.json()['install_id_str'], openudid

device_id, install_id, openudid = register_device()
