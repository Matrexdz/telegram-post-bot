import sys
import requests
from pprint import pprint

def send_message(token, chat_id, message, photo=None):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}

    if photo:
        url = f"https://api.telegram.org/bot{token}/sendPhoto"
        files = {'photo': open(photo, 'rb')}
        data = {"chat_id": chat_id, "caption": message}
        response = requests.post(url, data=data, files=files)
    else:
        response = requests.post(url, data=data)
    
    return response.json()

def main():
    # Replace 'YOUR_BOT_TOKEN' with your Telegram Bot token
    bot_token = '7061542804:AAE2yJ-JPiNKTlzqUrDgGy8nM6z5IQNurnY'
    
    # Replace 'YOUR_CHAT_ID' with the chat ID of your channel
    chat_id = '-1002046721440'

    # Read the content of the post.txt file with UTF-8 encoding
    try:
        with open("files/post.txt", "r", encoding="utf-8") as file:
            post_content = file.read()
    except UnicodeDecodeError:
        # Print error message to stderr to avoid UnicodeEncodeError in stdout
        print("UnicodeDecodeError: Unable to decode characters in input file.", file=sys.stderr)
        sys.exit(1)

    # Path to the image file
    image_path = "files/image.jpg"

    # Send the content and image to your Telegram channel
    response = send_message(bot_token, chat_id, post_content, photo=image_path)
    
    # Print the response from the Telegram API using pprint
    pprint(response, stream=sys.stdout, indent=4, width=100, depth=None, compact=False, sort_dicts=True)

if __name__ == "__main__":
    main()
