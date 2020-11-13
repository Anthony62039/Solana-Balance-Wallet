import requests

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--server', help='address of cluter server',default="https://devnet.solana.com/")
parser.add_argument('--soladdress', help='sol account',default="21QYCe8g5Xjcn5ZdLjSVxBcEAtPCPpW5C3CamW31Qrw6")

args = parser.parse_args()



headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Origin': 'https://explorer.solana.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://explorer.solana.com/',
    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
}

data = '{"method":"getAccountInfo","jsonrpc":"2.0","params":["'+args.soladdress+'",{"encoding":"jsonParsed","commitment":"single"}],"id":"75bd3474-7b27-49df-9dc5-f50576674992"}'

# print(data)
response = requests.post(args.server, headers=headers, data=data)

solbalance = float(response.json()["result"]["value"]["lamports"])
print("Balance SOL of account " + args.soladdress ," : ",solbalance/1000000000," SOL")
