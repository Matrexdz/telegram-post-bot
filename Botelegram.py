import subprocess
import time





main_header = """
  __  __       _                    _     
 |  \/  |     | |                  | |    
 | \  / | __ _| |_ _ __ _____  ____| |____
 | |\/| |/ _` | __| '__/ _ \ \/ / _` |_  /
 | |  | | (_| | |_| | |  __/>  < (_| |/ / 
 |_|  |_|\__,_|\__|_|  \___/_/\_\__,_/___|
                                          
"""

subprocess.run(['python', 'files/bot.py'], check=True)

def run_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running {script_name}: {e}")
while True:
    # Read the urls.txt file to check for links
    with open('files/urls.txt', 'r', encoding='utf-8') as file:
        links = file.readlines()

    # If there are no links left, break out of the loop
    if not links:
        break

    # Run the bot2.py script
    run_script('files/bot2.py')

    # Read the content of urls.txt, excluding the first line
    with open('files/urls.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) > 0:
            lines = lines[1:]

    # Write the modified content back to urls.txt
    with open('files/urls.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)

    # Wait for the bot2.py process to finish before proceeding
    time.sleep(1)  # Adjust this time as needed

    # Run the lik.py script
    run_script('files/lik.py')

    # Wait for the lik.py process to finish before proceeding
    time.sleep(1)  # Adjust this time as needed

    # Run the post.py script
    run_script('files/post.py')
    
    time.sleep(1)  # Adjust this time as needed
