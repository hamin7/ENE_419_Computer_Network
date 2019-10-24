from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import requests
import csv
import json

# making a function for it
def api_to_csv(url):
    print(datetime.datetime.now())
    r = requests.get(url)
    data = r.json()
    public_data = data['data']

    lol = url.split("/")
    filename = lol[-1] + ".csv"

    with open(filename, 'w') as main_data:
        # create the csv writer object

        csvwriter = csv.writer(main_data)

        count = 0

        for temp in public_data:
            if count == 0:
                header = temp.keys()
                csvwriter.writerow(header)
                count += 1
            csvwriter.writerow(temp.values())

        url = data["paging"]["next"]
        if url == "":
            pass

        return(api_to_csv(url))

scheduler = BlockingScheduler()
scheduler.add_job(api_to_csv("http://venmo.com/api/v5/public"), 'interval', seconds = 2)
scheduler.start()