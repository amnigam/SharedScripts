from checkPhish import check_url_safety
from openPhishFeed import fetch_phish_urls 

testUrls = [
    "http://testsafeBrowse.appspot.com/apiv4/ANY_PLATFORM/MALWARE/URL/",
    "http://testsafeBrowse.appspot.com/apiv4/ANY_PLATFORM/SOCIAL_ENGINEERING/URL/", # Phishing test URL
    "https://www.google.com/", # A known safe URL
    "https://example.com/",    # Another known safe URL
    "http://secure365.email/office-login/",  # Phishing link from PhishingTank
    "http://login-verification.co.uk/google", # From PhishTank
    "http://testsafebrowsing.appspot.com/s/phishing.html"
]

openPhishUrls = fetch_phish_urls()

# resp = check_url_safety(testUrls) 
resp = check_url_safety(openPhishUrls) 

if resp and "matches" in resp:
    print(f"The following {len(resp['matches'])} URLs were flagged as malicious:")
    for match in resp["matches"]:
        url = match.get("threat", {}).get("url")
        threat_type = match.get("threatType")
        platform_type = match.get("platformType")
        print(f"- URL: {url}, Threat Type: {threat_type}, Platform: {platform_type}")
        # if threat_type == "SOCIAL_ENGINEERING":
        #     print(f"  -> This is specifically identified as a phishing link!")
else:
    print("All tested URLs are likely safe (no matches found).")
