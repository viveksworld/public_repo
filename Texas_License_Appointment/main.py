import requests
from playsound import playsound
import json
from datetime import datetime

zip_code = input("Enter the ZIP code for DPS location search : ")
appoinment_date = input("Enter the appointment date to search (mm/dd/yyyy): ")


dps_url = "https://publicapi.txdpsscheduler.com/api/AvailableLocation"

data = {"TypeId": 71, "ZipCode": zip_code, "CityName": "", "PreferredDay": 0}
json_data = json.dumps(data)


while 1:
    try:
        print("{}-Checking DPS for {} @ {}".format(datetime.now(), appoinment_date, zip_code))
        resp = requests.post(dps_url, json_data, headers={"Content-Type": "application/json",
                                                          "Origin": "https://public.txdpsscheduler.com"}).content.decode(
            "utf-8")
        resp_data_list = json.loads(resp)

        for item in resp_data_list:
            if item["NextAvailableDate"] == appoinment_date:
                # playsound("/Users/vivek/Downloads/Store_Door_Chime-Mike_Koenig-570742973.mp3")
                print("{} location at {} has the next appointment for {}".format(item["Name"], item["Address"],
                                                                                 appoinment_date))
                playsound("./787sos-morse-code_daniel-simion.mp3")
    except:
        pass


