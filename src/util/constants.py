"""
Script with constaants used throughout the project
"""

API = (
    "https://restor2-prod-1-api.restor.eco/search/1/organizations/search?page=x&size=y"
)

HEADERS = {
    "authority": "restor2-prod-1-api.restor.eco",
    "method": "POST",
    "path": "search/1/organizations/search?page=x&size=y",
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "2",
    "content-type": "application/json",
    "origin": "https://restor.eco/",
    "priority": "u=1, i",
    "referer": "https://restor.eco/",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}
