#!/usr/bin/python3
"""
Task 2: Using Python to interact with APIs.
This script sends HTTP requests, processes the received JSON data,
prints it to the console, and saves structured data into a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Sends a GET request to JSONPlaceholder and prints:
    - the HTTP status code
    - the title of each post returned by the API
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    # If the request succeeds, convert response to JSON and print all titles
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Sends a GET request to JSONPlaceholder and saves structured post data
    to a CSV file called posts.csv.

    Each row of the CSV contains:
    - id of the post
    - title of the post
    - body text of the post
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Convert full post objects into simplified dictionaries
        processed_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Create posts.csv with specific columns
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(processed_posts)
