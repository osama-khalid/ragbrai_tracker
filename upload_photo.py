import requests
import base64
import time
import json
import datetime
# Load the GitHub token from file
with open('github_token.txt', 'r') as file:
    github_token = file.read().strip()

while datetime.datetime.now() < datetime.datetime(2024, 7, 30):
    while(1):
        try:
            # File to upload
            file_path = 'current_photo.txt'
            repo_owner = 'osama-website'
            repo_name = 'ragbrai_tracker'
            file_name_in_repo = 'current_photo.txt'
            branch = 'main'

            text = open(file_path, 'r').read()
            # Read file content
            with open(file_path, 'rb') as file:
                content = file.read()

            # Encode content to base64
            encoded_content = base64.b64encode(content).decode('utf-8')

            # Create the URL
            url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_name_in_repo}'

            # Prepare the request headers
            headers = {
                'Authorization': f'token {github_token}',
                'Content-Type': 'application/json'
            }

            # Check if the file already exists to get the SHA
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                sha = response.json()['sha']
            else:
                sha = None

            # Prepare the payload
            payload = {
                'message': f'Add {file_name_in_repo}',
                'content': encoded_content,
                'branch': branch
            }

            if sha:
                payload['sha'] = sha

            # Send the request
            response = requests.put(url, headers=headers, data=json.dumps(payload))

            # Check the response
            if response.status_code in [200, 201]:
                print(f'Successfully uploaded {file_name_in_repo} to {repo_owner}/{repo_name}')
                print(text)
            else:
                print(f'Failed to upload {file_name_in_repo}. Status code: {response.status_code}')
                print(response.json())
            break
        except:
            time.sleep(1)
    time.sleep(100)  # 900 seconds = 15 minutes
