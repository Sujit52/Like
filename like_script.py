import requests
import time
from datetime import datetime

def send_like(uid):
    api_url = f"https://free-like-api-aditya-ffm.vercel.app/like?uid={uid}&server_name=IND&key=@adityaapis"
    try:
        response = requests.get(api_url)
        result = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'uid': uid,
            'status_code': response.status_code,
            'response_text': response.text.strip(),
            'success': response.status_code == 200
        }
        return result
    except Exception as e:
        return {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'uid': uid,
            'status_code': None,
            'response_text': str(e),
            'success': False
        }

def main():
    # Read UIDs from file
    try:
        with open('uids.txt', 'r') as file:
            uids = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("ERROR: uids.txt file not found!")
        return
    
    print(f"Starting API calls for {len(uids)} UIDs...")
    
    results = []
    for uid in uids:
        result = send_like(uid)
        results.append(result)
        
        # Print current result
        print(f"{result['timestamp']} - UID: {result['uid']} - Status: {result['status_code']} - Success: {result['success']}")
        
        time.sleep(1)  # 1 second delay between requests
    
    # Save detailed results to log file
    with open('like_results.log', 'w') as log_file:
        for result in results:
            log_file.write(f"{result['timestamp']} - UID: {result['uid']} - Status: {result['status_code']} - Response: {result['response_text']}\n")
    
    # Show summary
    success_count = sum(1 for r in results if r['success'])
    print(f"\n=== SUMMARY ===")
    print(f"Total UIDs: {len(uids)}")
    print(f"Successful: {success_count}")
    print(f"Failed: {len(uids) - success_count}")
    print(f"Log file created: like_results.log")

if __name__ == "__main__":
    main()
