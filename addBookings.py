from login import loginUser, getCookies
login_data = loginUser()
cookies = getCookies(login_data)

import requests
import json

url = "https://opentext.safetrax.in/forwardmongo/saverosters?version=new"

payload = json.dumps({
  "officeId": "663dc275c1187f14448f9cb2",
  "employeeId": "62cfd2ec46777d6499c3fbd7",
  "dates": [
    1729449000000,1729535400000,1729621800000,1729708200000,1729794600000,1729881000000,1729967400000
  ],
  "loginHours": 29700000,
  "logoutHours": 62100000,
  "revised": False,
  "shiftSequence": 0
})
headers = {
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8,vi;q=0.7,id;q=0.6',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Cookie': cookies,
  'DNT': '1',
  'Origin': 'https://opentext.safetrax.in',
  'Referer': 'https://opentext.safetrax.in/roster',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
