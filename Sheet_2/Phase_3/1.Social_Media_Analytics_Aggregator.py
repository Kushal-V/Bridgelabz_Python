# post = {"comments":{ comment1: { 'text': 'nice post', "likes": 2}, comment2: { 'text': 'very good', "likes": 3}}}

import json

def main():
    print("Enter the post:")
    post = json.loads(input())

    total_likes = sum(comment["likes"] for comment in post["comments"].values())
    print(total_likes)

main()
