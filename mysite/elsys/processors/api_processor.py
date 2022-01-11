import requests

COMMENTS_URL = "https://jsonplaceholder.typicode.com/posts/1/comments"
POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def sort_func(json):
    try:
        if 'title' in json:
            return len(json['title'])
        else:
            return len(json['body'])
    except KeyError:
        return 0


class ApiProcessor:
    @staticmethod
    def longest_comment():
        data = requests.get(COMMENTS_URL)
        comments = sorted(data.json(), key=sort_func, reverse=True)
        return comments[0]
    
    @staticmethod
    def post_with_longest_title():
        data = requests.get(POSTS_URL)
        posts = sorted(data.json(), key=sort_func, reverse=True)
        return posts[0]
