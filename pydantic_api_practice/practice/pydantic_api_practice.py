import requests
from pydantic import BaseModel, ValidationError
from typing import List, Optional

# 定義 Pydantic 模型來描述 API 返回的數據結構
class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

# 獲取數據的函數
def fetch_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()
    return response.json()

# 驗證數據的函數
def validate_posts(posts: List[dict]):
    validated_posts = []
    for post in posts:
        try:
            validated_post = Post(**post)
            validated_posts.append(validated_post)
        except ValidationError as e:
            print(f"Validation error for post: {post['id']}")
            print(e)
    return validated_posts

if __name__ == "__main__":
    posts = fetch_posts()
    validated_posts = validate_posts(posts)
    print(f"Validated {len(validated_posts)} posts")
