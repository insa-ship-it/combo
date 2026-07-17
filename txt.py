import requests
from datetime import datetime

# ===== CONFIGURATION =====
# Add your list of TXT file URLs here
TXT_FILES = [
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/www.eporner.com.streamtv.to_8080_.txt",
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/wickediptv.xyz_80.txt",
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/vt57.ofztvxv.top_8080.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/vooezao.top_8080_panel.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/vipapyenhmw.top_8080.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/user.scalecdn.co_8080.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/tv.startseven.tn_2052.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/tivim24.de_8000.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/tectonbrand.com_.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/storetvip.shop_8080.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/starlatino.tv_8880.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/smartvnow.xyz_25461.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/skynetdigital.us_80.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/sitemap.dinofox.sbs_80_.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/s.rocketdns.info_8080.txt", 
    "", 
    "", 
    "", 
    "", 
]

# Output file
OUTPUT_FILE = "combined_list.txt"

# ===== FUNCTIONS =====
def fetch_txt_content(url):
    """Fetch content from a raw text URL"""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        # Returns a list of lines, stripping whitespace
        return [line.strip() for line in response.text.splitlines() if line.strip()]
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
        return []

def main():
    """Main function to combine text files"""
    print(f"🚀 Starting to combine {len(TXT_FILES)} text files...")
    
    all_lines = []
    
    # Process each URL
    for url in TXT_FILES:
        print(f"🔄 Processing: {url}")
        content = fetch_txt_content(url)
        if content:
            all_lines.extend(content)
            print(f"✅ Added {len(content)} lines from {url.split('/')[-1]}")
    
    # Remove duplicates while maintaining order
    unique_lines = list(dict.fromkeys(all_lines))
    
    # Write to output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        outfile.write(f"# Generated on {datetime.utcnow().isoformat()} UTC\n")
        outfile.write(f"# Total unique lines: {len(unique_lines)}\n\n")
        outfile.write("\n".join(unique_lines))
    
    print(f"\n🎉 Success! Combined content saved as '{OUTPUT_FILE}'")
    print(f"📄 Total lines: {len(unique_lines)}")

if __name__ == "__main__":
    main()
