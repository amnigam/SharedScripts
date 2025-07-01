import requests 

URLHAUS_DUMP = 'https://urlhaus.abuse.ch/downloads/text_recent/'

def get_urlhaus_links(limit=400):
    print("📥 Fetching URLHAUS data...")
    try:
        resp = requests.get(URLHAUS_DUMP)
        resp.raise_for_status()
        urls = resp.text.strip().split("\n")        # Convert to LIST
        print(f"✅ Retrieved {len(urls)} URLs from URLHAUS API. Limiting to {limit}")
        return urls[:limit]  # limit to top N
    except Exception as e:
        print(f"❌ Failed to fetch URLHAUS dump: {e}")
        return []    
