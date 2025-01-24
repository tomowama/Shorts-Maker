import requests
from bs4 import BeautifulSoup
SUBREDDITS = ["AITAH"]
def scrap(subreddit): # MAKE THIS RETURN A STRING
    url = f"https://www.reddit.com/r/{subreddit}/top/?t=day"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")


    titles = soup.select('[id^="post-title-"]')

    post_data = {}

    for title in titles:
        paragraphs = []
        next_element = title.find_next()  # Get the next element after the title

        while next_element and next_element.name != 'h1':
            if next_element.name == 'p':  # Collect <p> tags
                paragraphs.append(next_element.text)
            next_element = next_element.find_next()  # Move to the next element

        post_data[title.text] = paragraphs

    for post, paragraphs in post_data.items():
        print(f"Title: {post}")
        for i, paragraph in enumerate(paragraphs, start=1):
            print(f"  Paragraph {i}: {paragraph}")


# get the posts.

for subreddit in SUBREDDITS:
    content = scrap(subreddit)
