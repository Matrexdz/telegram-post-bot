import requests
from bs4 import BeautifulSoup

# Define URLs and file names
url = "https://www.discudemy.com/all"
filename = "files/nadjib.html"
output_file = "files/urls.txt"
output_file1 = "files/archiv.txt"

# Fetch HTML content
response = requests.get(url)

if response.status_code == 200:
    # Save HTML content to a file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"HTML content saved to {filename}")

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all links with class "card-header"
    links = soup.find_all("a", class_="card-header")
    
    # Extract URLs
    extracted_urls = [link.get("href") for link in links]
    
    # Read existing archive URLs
    with open(output_file1, "r", encoding="utf-8") as f:
        existing_urls = set(f.read().splitlines())
    
    # Append new unique URLs to the archive file
    with open(output_file1, "a", encoding="utf-8") as f:
        for url in extracted_urls:
            if url not in existing_urls:
                f.write(url + "\n")
    print(f"All unique URLs appended to {output_file1}")
    
    # Read the contents of urls.txt
    with open(output_file, 'r+', encoding="utf-8") as f:
        urls = f.readlines()
        # Remove duplicate URLs from urls.txt
        unique_urls = [url for url in urls if url.strip() not in existing_urls]
        f.seek(0)
        f.writelines(unique_urls)
        f.truncate()
    print("Duplicate URLs removed from urls.txt")
    
    # Write all extracted URLs to a file
    with open(output_file, "a", encoding="utf-8") as f:
        for url in extracted_urls:
            f.write(url + "\n")
    print(f"All URLs saved to {output_file}")

else:
    print(f"Failed to fetch HTML content from {url}. Status code: {response.status_code}")
