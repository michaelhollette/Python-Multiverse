"""
Web Scraping in Python Tutorial
-------------------------------

This script demonstrates how to perform web scraping in Python using the 
'requests' and 'BeautifulSoup' libraries. The goal is to fetch data from a webpage,
parse the HTML, extract the desired data, and store it in a structured format.
"""

# Import required libraries
import requests
from bs4 import BeautifulSoup
import csv
import time

# Step 1: Sending a Request to a Website
def fetch_page(url):
    """
    Fetches the HTML content of a webpage.
    
    Parameters:
    - url (str): The URL of the webpage to scrape.
    
    Returns:
    - BeautifulSoup object containing the HTML content if successful, None otherwise.
    """
    try:
        response = requests.get(url)
        for item, value in response.headers.items():
            print(f"item: {item}, value: {value}")
        response.raise_for_status()  # Raises an HTTPError if the status is 4xx, 5xx
        
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None


# Step 2: Parsing and Extracting Data
def extract_headings(soup):
    """
    Extracts headings (e.g., h2 elements) from a parsed HTML page.
    
    Parameters:
    - soup (BeautifulSoup): Parsed HTML content.
    
    Returns:
    - List of headings as strings.
    """
    headings = []
    h2_tags = soup.find_all('h2')
    for tag in h2_tags:
        headings.append(tag.text.strip())
    return headings


def extract_links(soup):
    """
    Extracts all hyperlinks from the page.
    
    Parameters:
    - soup (BeautifulSoup): Parsed HTML content.
    
    Returns:
    - List of hyperlinks as strings.
    """
    links = []
    anchor_tags = soup.find_all('a', href=True)  # Only tags with href attribute
    for tag in anchor_tags:
        link = tag['href']
        links.append(link)
    return links


# Step 3: Storing Data in a CSV File
def save_to_csv(data, filename="scraped_data.csv"):
    """
    Saves data to a CSV file.
    
    Parameters:
    - data (list of lists): Data to save.
    - filename (str): Name of the CSV file.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Heading or Link"])  # Header row
            for row in data:
                writer.writerow([row])
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")


# Step 4: Main Function to Run the Script
def main():
    """
    Main function to perform web scraping.
    
    Instructions:
    - Replace `url` with the webpage URL you want to scrape.
    - Update the `sleep_time` if needed to avoid overloading the server.
    """
    url = "https://home.barclays/"  # Replace with the target website
    sleep_time = 1  # Time delay between requests in seconds
    
    # Fetch the HTML content
    soup = fetch_page(url)
    if soup:
        # Extract data (e.g., headings and links)
        headings = extract_headings(soup)
        links = extract_links(soup)

        # Print the extracted data
        print("\nHeadings Found:")
        for heading in headings:
            print(heading)

        print("\nLinks Found:")
        for link in links:
            print(link)

        # Save to CSV
        all_data = headings + links
        save_to_csv(all_data)

        # Respect the server by adding a delay between requests
        time.sleep(sleep_time)


# Step 5: Run the Script
if __name__ == "__main__":
    main()
