import mmh3
import base64
import requests
import argparse

print(r"""
       *  *     .   *     ✨
        \ | /       *
      `. ★ .'     🪄 Favicon Spellcaster
        / | \        ~ by @soyelmago ~

""")

parser = argparse.ArgumentParser(description="Calculate Shodan favicon hash from URL")
parser.add_argument("-u", "--url", required=True, help="URL of the favicon.ico file")
args = parser.parse_args()

try:
    response = requests.get(args.url)
    response.raise_for_status()
except Exception as e:
    print(f"❌ Error fetching favicon: {e}")
    exit()

favicon_b64 = base64.encodebytes(response.content)
favicon_hash = mmh3.hash(favicon_b64)

print(f"\n🔮 Shodan Favicon Hash: {favicon_hash}")
print(f"📜 Shodan DORK:\n")
print(f"    http.favicon.hash:{favicon_hash}\n")
print("✨ Paste it in https://www.shodan.io/search to discover hosts using the same favicon.")

