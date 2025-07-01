import requests 

OPENPHISH_FEED = 'https://openphish.com/feed.txt' 

def fetch_phish_urls(limit=300):
    print("📥 Fetching OpenPhish feed...")
    try:
        resp = requests.get(OPENPHISH_FEED)
        resp.raise_for_status()
        urls = resp.text.strip().split("\n")
        print(f"✅ Retrieved {len(urls)} URLs.")
        return urls[:limit]  # limit to top N
    except Exception as e:
        print(f"❌ Failed to fetch OpenPhish feed: {e}")
        return []    
