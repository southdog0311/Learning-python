import pytest
from api_practice.practice import get_post, create_post, update_post, delete_post

def test_get_post():
    post = get_post(1)
    assert post is not None
    assert 'userId' in post
    assert 'id' in post
    assert 'title' in post
    assert 'body' in post
    assert post['id'] == 1

def test_create_post():
    new_post = create_post('foo', 'bar', 1)
    assert new_post is not None
    assert 'userId' in new_post
    assert 'id' in new_post
    assert 'title' in new_post
    assert 'body' in new_post
    assert new_post['title'] == 'foo'
    assert new_post['body'] == 'bar'
    assert new_post['userId'] == 1

def test_update_post():
    updated_post = update_post(1, 'foo updated', 'bar updated', 1)
    assert updated_post is not None
    assert 'userId' in updated_post
    assert 'id' in updated_post
    assert 'title' in updated_post
    assert 'body' in updated_post
    assert updated_post['id'] == 1
    assert updated_post['title'] == 'foo updated'
    assert updated_post['body'] == 'bar updated'
    assert updated_post['userId'] == 1

def test_delete_post():
    result = delete_post(1)
    assert result
