import requests
import time

def send_like(uid):
    api_url = f"https://free-like-api-aditya-ffm.vercel.app/like?uid={uid}&server_name=IND&key=@adityaapis"
    try:
        response = requests.get(api_url)
        print(f"UID: {uid} - Status: {response.status_code} - Response: {response.text}")
    except Exception as e:
        print(f"Error for UID {uid}: {e}")

def main():
    with open('src/uids.txt', 'r') as file:
        uids = [line.strip() for line in file if line.strip()]
    
    for uid in uids:
        send_like(uid)
        time.sleep(1)  # 1 second delay between requests

if __name__ == "__main__":
    main()