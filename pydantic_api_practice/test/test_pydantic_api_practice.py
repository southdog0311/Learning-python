import pytest
from requests.exceptions import HTTPError
from practice.pydantic_api_practice import fetch_posts, validate_posts, Post

def test_fetch_posts():
    try:
        posts = fetch_posts()
        assert isinstance(posts, list)
    except HTTPError:
        pytest.fail("HTTP request failed")

def test_validate_posts():
    posts = [
        {"userId": 1, "id": 1, "title": "title", "body": "body"},
        {"userId": 2, "id": 2, "title": "title2", "body": "body2"}
    ]
    validated_posts = validate_posts(posts)
    assert len(validated_posts) == 2
    for post in validated_posts:
        assert isinstance(post, Post)

if __name__ == "__main__":
    pytest.main()
