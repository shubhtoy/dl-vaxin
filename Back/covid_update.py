from flask import Flask, render_template
from requests.api import request
from apscheduler.schedulers.background import BackgroundScheduler


import requests
import time
import datetime

aval = {}
aval_18 = {}
keys_ = []
keys = []
datas_ = []
keys_18 = []
times = None
# import jsoncodes=[]

# a.status_code = 11
def update():
    global aval, aval_18, keys_, keys, datas_, times
    if times and time.time() - times < 300:
        return
    print("DATA UPDATING.....")
    date = datetime.datetime.now()
    aval = {}
    aval_18 = {}
    keys_ = []
    keys_18 = []
    for code in range(140, 151):
        for day_plus in range(0, 61, 6):
            date_now = (date + datetime.timedelta(days=day_plus)).strftime("%d-%m-%Y")
            headers = {
                "authority": "cdn-api.co-vin.in",
                "method": "GET",
                "path": f"/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "max-age=0",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "sec-gpc": "1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            }
            headers_pre = {
                "authority": "cdn-api.co-vin.in",
                "method": "OPTIONS",
                "path": f"/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "access-control-request-headers": "authorization",
                "access-control-request-method": "GET",
                "origin": "https://selfregistration.cowin.gov.in",
                "referer": "https://selfregistration.cowin.gov.in/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "cross-site",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            }
            a = requests.get(
                f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
                headers=headers_pre,
            )
            if a.status_code == 403:
                print("Sleeping....")
                times = time.time()

            # a = requests.get(
            #     f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
            #     headers=headers,
            # )
            # print(
            #     date_now,
            #     f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
            # )
            count = 0
            while a.text == "Unauthenticated access!" and count < 6:
                day_plus += 1
                date_now = (date + datetime.timedelta(days=day_plus)).strftime(
                    "%d-%m-%Y"
                )
                count += 1
                headers = {
                    "authority": "cdn-api.co-vin.in",
                    "method": "GET",
                    "path": f"/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
                    "scheme": "https",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "cache-control": "max-age=0",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "none",
                    "sec-fetch-user": "?1",
                    "sec-gpc": "1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
                }
                headers_pre = {
                    "authority": "cdn-api.co-vin.in",
                    "method": "OPTIONS",
                    "path": f"/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
                    "scheme": "https",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "access-control-request-headers": "authorization",
                    "access-control-request-method": "GET",
                    "origin": "https://selfregistration.cowin.gov.in",
                    "referer": "https://selfregistration.cowin.gov.in/",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "cross-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
                }
                a = requests.get(
                    f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
                    headers=headers_pre,
                )
                # a = requests.get(
                #     f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
                #     headers=headers,
                # )
                # print(
                #     date_now,
                #     a.text,
                #     f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
                # )
            else:
                pass
            count = 0
            while a.status_code != 200 and count < 3:
                # print(
                #     date_now,
                #     a.text,
                #     f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
                # )
                a = requests.get(
                    f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={code}&date={date_now}",
                    headers=headers_pre,
                )
                count += 1
                # print(a)
            else:
                pass
            # print(a)
            if a.status_code == 200:
                data = a.json()
                # table = [i for i in data["centers"]["sessions"] if i["available_capacity"] > 0]
                centres = data["centers"]
                if len(centres) == 0:
                    pass
                else:
                    for i in centres:
                        sessions = i["sessions"]
                        for j in sessions:
                            if j["available_capacity"] > 0:
                                curr_data = {
                                    "name": i["name"],
                                    "address": i["address"],
                                    "fee_type": i["fee_type"],
                                    "available": j["available_capacity"],
                                    "min_age": j["min_age_limit"],
                                    "vaccine": j["vaccine"],
                                    "applicable": i["block_name"],
                                }
                                if curr_data["min_age"] != 45:
                                    print(curr_data)
                                    yes = aval_18.get(j["date"])
                                    if yes:
                                        aval_18[j["date"]].append(curr_data)
                                    else:
                                        aval_18[j["date"]] = [curr_data]
                                    # aval_18[j["date"]].append(curr_data)
                                yes = aval.get(j["date"])

                                if yes:
                                    aval[j["date"]].append(curr_data)
                                else:
                                    aval[j["date"]] = [curr_data]
                    # print("AVAL UPDATED!!!!")
                    # print(aval.keys())

    keys_ = list(aval.keys())
    keys_18 = list(aval_18.keys())
    keys_18.sort(key=lambda date: datetime.datetime.strptime(date, "%d-%m-%Y"))
    keys_.sort(key=lambda date: datetime.datetime.strptime(date, "%d-%m-%Y"))
    print("DATA UPDATED!", keys_)
    keys = [keys_, keys_18]
    datas_ = [aval, aval_18]
    return aval


sched = BackgroundScheduler(daemon=True)
sched.add_job(update, "interval", minutes=1, max_instances=1)
sched.start()

app = Flask(__name__)


@app.route("/datas", methods=["GET"])
def datas():
    return {"datas_": datas_, "keys": keys}


if __name__ == "__main__":
    app.run(port=2003)