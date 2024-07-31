import requests

def get_post(post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 取得貼文 ID 為 1 的貼文
post = get_post(1)
print(post)



def create_post(title, body, user_id):
    post_data = {
        'title': title,
        'body': body,
        'userId': user_id
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=post_data)
    if response.status_code == 201:
        return response.json()
    else:
        return None

# 新增一篇貼文
new_post = create_post('foo', 'bar', 1)
print(new_post)




def update_post(post_id, title, body, user_id):
    post_data = {
        'id': post_id,
        'title': title,
        'body': body,
        'userId': user_id
    }
    response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=post_data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 更新貼文 ID 為 1 的貼文
updated_post = update_post(1, 'foo updated', 'bar updated', 1)
print(updated_post)



def delete_post(post_id):
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    if response.status_code == 200:
        return True
    else:
        return False

# 刪除貼文 ID 為 1 的貼文
delete_result = delete_post(1)
print(delete_result)



