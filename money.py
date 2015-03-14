import requests
import webbrowser
from time import sleep

# Enter your details here.
USER = "USER_NAME"
PASSWORD = "PASSWORD"
DESTINATION = "DESTINATION_ADDRESS"  # Triple-check this!
AMOUNT = 0.02
INTERVAL = 30  # seconds
OPEN_BROWSER = True  # will open browser with blockchain.info summary of tx when successful.
QUIT_ON_SUCCESS = True  # will quit on a successful withdrawal.


def begForMoney():
    print "Requesting withdrawal for %f BTC to %s...." % (AMOUNT, DESTINATION)
    r = requests.post("https://CampBX.com/api/sendbtc.php",
                      data={"user": USER, "pass": PASSWORD, "BTCTo": DESTINATION, "BTCAmt": AMOUNT}
                      )
    print(r.text)

    # If a transaction successfully completed, open the user's webbrowser to show the tx details...
    if OPEN_BROWSER and r.json()["Success"]:
        url = "https://www.blockchain.info/tx/" + r.json()["Success"]
        webbrowser.open_new_tab(url)

    # ...and exit.
    if QUIT_ON_SUCCESS and r.json()["Success"]:
        print("Transaction completed, exiting...")
        exit(0)

# Kickoff
while True:
    begForMoney()
    print "----\nSleeping for %d seconds to prevent ratelimiting.\n----" % INTERVAL
    sleep(INTERVAL)
