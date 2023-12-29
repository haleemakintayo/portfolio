import urllib.request
import json

def calculate_comment_counts(url):
    # Fetch JSON data from the provided URL
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')

    # Parse JSON data
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

    # Extract comment counts
    comment_counts = [comment['count'] for comment in json_data.get('comments', [])]

    # Compute the sum of comment counts
    total_comments = sum(comment_counts)

    return total_comments

# Prompt the user for a URL
url = input("Enter the URL: ")

# Call the function and display the result
result = calculate_comment_counts(url)
if result is not None:
    print(f"Sum of comment counts: {result}")


