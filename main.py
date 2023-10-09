"""
This file is to test the api i am using which is from newsApi.org
    """

import requests

# Define the API endpoint URL
url = "https://newsapi.org/v2/everything?q=google&sortBy=popularity&apiKey=3fc3482200ca420dace9c853f28540a9"


# Make the GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Access the data from the response
    status = data.get("status")
    total_results = data.get("totalResults")
    articles = data.get("articles")

    # Process the articles data
    for article in articles:
        author = article.get("author")
        title = article.get("title")
        description = article.get("description")
        url = article.get("url")
        published_at = article.get("publishedAt")
        content = article.get("content")

        # You can print or further process the article data here
        print(f"Author: {author}")
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"URL: {url}")
        print(f"Published At: {published_at}")
        print(f"Content: {content}")
        print("\n")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
