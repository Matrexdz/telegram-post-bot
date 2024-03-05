
import requests
from bs4 import BeautifulSoup

# Read the HTML file
with open("files/data.html", "r", encoding="latin-1") as f:
    html_content = f.read()

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find all <a> tags with the specified class
link_tags = soup.find_all("a", class_="ui big inverted green button discBtn")

# Open walid.html file in write mode
with open("files/walid.html", "w", encoding="utf-8") as walid_file:
    # Iterate over each link
    for link_tag in link_tags:
        # Get the URL from href attribute
        link_url = link_tag["href"]
        
        # Make a GET request to the link URL
        response = requests.get(link_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the linked page
            linked_soup = BeautifulSoup(response.text, "html.parser")
            
            # Write the content of the linked page to walid.html
            walid_file.write(str(linked_soup))
            walid_file.write("\n\n")
        else:
            print(f"Failed to fetch {link_url}")
# Read the content of walid.html
# Read the HTML file
with open("files/walid.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the <a> tag with the specified class
link2_tag = soup.find("p", class_="text centered ui green label").find_next_sibling("a")

# Get the URL from href attribute
link2_url = link2_tag["href"]

# Print link2
print("Link2:", link2_url)

# Save link2 to post.txt
with open("files/post.txt", "a", encoding="utf-8") as post_file:
    post_file.write(link2_url)