## CampBX Auto-Withdrawal Script

![meme](https://i.imgflip.com/i9tn4.jpg)

CampBX appears to be allowing withdrawals at random. Users are concerned the funds may be lost.

Rather than clicking 'withdrawal' all day, this script uses the API your money from CampBX at intervals.

CampBX appears to be allowing small withdrawals to get through, but we have not yet figured out a pattern.

Usage
-----

1. Edit `money.py`. Add your CampBX credentials, the desired amount to withdraw, and the destination address.
  - Minimum withdrawal amount is 0.01 BTC.

2. Install the `requests` dependency. `pip install requests` or `easy_install requests` will do it. See the
[requests documentation](http://docs.python-requests.org/en/latest/user/install/) if that isn't working for you.

3. Run the script (`python money.py`). Wait. Probably wait all day.

Troubleshooting Notes
---------------------

* You have to disable 2FA to use the CampBX API. 

* Using the API also logs you out of the web interface for some unknown reason.

* CampBX has a daily withdrawal limit, and it appears that the "Cold Wallet Maintenance" errors still deduct
  from that limit. If you start getting limit errors, you aren't likely to get through for another 24 hours.
