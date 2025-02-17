import argparse
import http.client
import json
parser = argparse.ArgumentParser(description="GitHub User Activity CLI")
parser.add_argument("username",type=str,help="Username to review activity")

args = parser.parse_args()

if args.username:
    try:
        conn = http.client.HTTPSConnection("api.github.com")
        
        headers = {
            'User-Agent':"Mozilla/5.0",
        }
        conn.request("GET",f'/users/{args.username}/events',headers=headers)
        res = conn.getresponse()
        print(res.status,res.reason)
        data = res.read().decode("utf-8")
        conn.close()
        eventos = json.loads(data)

        for evento in eventos:
            print(f"Se ha realizado:{evento['type']}  En:{evento['repo']['name']}")

    except Exception as e:
        print(e)
else:
    print("Invalid Username!!")

    