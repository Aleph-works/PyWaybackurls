from core import requester
from urllib.parse import unquote
import os
import sys


def main(domain):
    if os.name == 'nt':
        os.system('cls')

    target = domain
    results = []
    url = f"http://web.archive.org/cdx/search/cdx?url=*.{target}/*&output=txt&fl=original&collapse=urlkey&page=/"

    response = requester.connector(url)
    if response == False:
        return
    response = unquote(response)

    final_uris = response
    print(final_uris)

    file = open("temp.txt","w")
    file.write(final_uris)
    file.close
    file = open("temp.txt","r")
    uris = file.read().splitlines()

    for uri in uris:
        results.append(uri)

    if len(results) > 0:
        print("Found: %s matches." % (len(results)))
        print()
        return {
            "matches": len(results),
            "result": results,
        }
    else:
        return {"matches": 0, "result": []}

    os.system('rm temp.txt')

if __name__ == "__main__":
        try:
                domain = sys.argv[1]
        except:
                print("Eg. ./PyWaybackurls <domain>")
                sys.exit()
        main(f"{domain}")
