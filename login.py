import requests

url = "https://opentext.safetrax.in/auth"

payload='hashrequest=&cnonce=&username=&password='
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'max-age=0',
  'content-type': 'application/x-www-form-urlencoded',
  'origin': 'https://opentext.safetrax.in',
  'priority': 'u=0, i',
  'referer': 'https://opentext.safetrax.in/auth?redirectTo=/roster',
  'sec-ch-ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36'
}


def loginUser():
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def getCookies(response):
    cookies = []
    raw_cookies = response.cookies._cookies['opentext.safetrax.in']['/']
    for cookie in raw_cookies.keys():
        cookies.append(f"{cookie}={raw_cookies[cookie].value}")
    return "; ".join(cookies)
