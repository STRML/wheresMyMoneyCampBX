import requests
from time import sleep

# Enter your details here.
USER = 'USER_NAME'
PASSWORD = 'PASSWORD'
DESTINATION = 'DESTINATION_ADDRESS'  # Triple-check this!
AMOUNT = 0.02
INTERVAL = 30  # seconds


def begForMoney():
    print "Requesting withdrawal for %f BTC to %s...." % (AMOUNT, DESTINATION)
    r = requests.post("https://CampBX.com/api/sendbtc.php",
                      data={'user': USER, 'pass': PASSWORD, 'BTCTo': DESTINATION, 'BTCAmt': AMOUNT}
                      )
    print(r.text)

# Kickoff
while True:
    begForMoney()
    print "----\nSleeping for %d seconds to prevent ratelimiting.\n----" % INTERVAL
    sleep(INTERVAL)
