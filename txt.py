import requests
from datetime import datetime

# ===== CONFIGURATION =====
# Add your list of TXT file URLs here
TXT_FILES = [
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/143.244.35.74_80.txt",
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/172.110.221.91_8080.txt",
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/185.182.193.203_25461.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/206.212.242.25_80.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/chino19121959.hofcepesp1.top_8080.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/94.130.11.12_8080.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/45.139.122.199_80_.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/31.43.191.125_8080.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/forza-acmilan.streamtv.to_8080_.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/etvserv.xyz_55337.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/eres.muy.muy.tonto.hnsefpop.top_8080.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/cord-cutter.net_8080.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/junglemuff.best_80.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/jettv.pro_25461.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/iptv3.kbc.al_25461.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/imediatv666.store_7777.txt", 
    "https://github.com/insa-ship-it/combo/raw/refs/heads/main/text/garaveli.123tv.to_8080.txt", 
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
