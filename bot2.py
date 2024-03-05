import requests
from bs4 import BeautifulSoup

def main():
    # Read URL from url.txt
    with open('files/urls.txt', 'r') as file:
        url = file.readline().strip()

    # Fetch HTML content from the URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
        html_content = response.text
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    # Save the HTML content to data.html
    with open('files/data.html', 'w') as file:
        file.write(html_content)



    # Search for image link and title in the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extracting image link
    image_link = soup.find('meta', attrs={'name': 'twitter:image'})
    if image_link:
        image_url = image_link.get('content')
        try:
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            with open('files/image.jpg', 'wb') as image_file:
                image_file.write(image_response.content)

        except requests.RequestException as e:
            print(f"Error fetching image: {e}")
    else:
        print("No image link found in the HTML content.")

    # Extracting title
    title_meta = soup.find('meta', attrs={'name': 'twitter:title'})
    if title_meta:
        title = title_meta.get('content')
        # Save the title to post.txt with UTF-8 encoding
        with open('post.txt', 'w', encoding='utf-8') as post_file:
            post_file.write("✏️: *{}*\n\n".format(title))

    else:
        print("No title found in the HTML content.")

    # Extracting description
    description_meta = soup.find('meta', attrs={'name': 'twitter:description'})
    if description_meta:
        description = description_meta.get('content')
        # Save the description to post.txt with UTF-8 encoding
        with open('post.txt', 'a', encoding='utf-8') as post_file:
            post_file.write("📝: " + description + "\n\n")

    else:
        print("No description found in the HTML content.")

    # Extracting languages
    language_spans = soup.find_all('span', class_='languages')
    with open('post.txt', 'a', encoding='utf-8') as post_file:
        for language_span in language_spans:
            language = language_span.get_text(strip=True)
            post_file.write("🔠: " + language + "\n\n")

    # Extracting prices
    price_spans = soup.find_all('span', class_='price')
    with open('post.txt', 'a', encoding='utf-8') as post_file:
        for price_span in price_spans:
            price = price_span.get_text(strip=True)
            post_file.write("💲:  " + price + " Free\n\n")

    # Extracting publishers
    publisher_spans = soup.find_all('span', class_='publisher')
    with open('post.txt', 'a', encoding='utf-8') as post_file:
        for publisher_span in publisher_spans:
            publisher = publisher_span.get_text(strip=True)
            post_file.write("👩‍🏫:  " + publisher + " \n\n")
            post_file.write("🌟: Rated 4.1 out of 5 \n\n")
            post_file.write("🆓: FREE For Limited Time\n\n")

if __name__ == "__main__":
    main()
