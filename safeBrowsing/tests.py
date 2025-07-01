from checkPhish import check_url_safety
from openPhishFeed import fetch_phish_urls 
from urlhaus import get_urlhaus_links 

manualTestUrls = [
    "http://testsafeBrowse.appspot.com/apiv4/ANY_PLATFORM/MALWARE/URL/",
    "http://testsafeBrowse.appspot.com/apiv4/ANY_PLATFORM/SOCIAL_ENGINEERING/URL/", # Phishing test URL
    "https://www.google.com/", # A known safe URL
    "https://example.com/",    # Another known safe URL
    "http://secure365.email/office-login/",  # Phishing link from PhishingTank
    "http://login-verification.co.uk/google", # From PhishTank
    "http://testsafebrowsing.appspot.com/s/phishing.html"   # Known phishing link. 
]

openPhishTestUrls = fetch_phish_urls()
urlHausTestUrls = get_urlhaus_links()

# resp = check_url_safety(openPhishTestUrls) 
resp = check_url_safety(urlHausTestUrls)
# resp = check_url_safety(manualTestUrls) 

if resp and "matches" in resp:
    print(f"The following {len(resp['matches'])} URLs were flagged as malicious:")
    for match in resp["matches"]:
        url = match.get("threat", {}).get("url", {}).strip()        # strip it of trailing spaces. 
        threat_type = match.get("threatType")
        platform_type = match.get("platformType")
        print(f"- URL: {url}, Threat Type: {threat_type}, Platform: {platform_type}")
else:
    print("All tested URLs are likely safe (no matches found).")
