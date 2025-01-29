import pytest
import requests
from jsonschema import validate
from unittest.mock import patch

# URL for the API
URL = "https://jsonplaceholder.typicode.com"


# Fixtures for reusable setup
@pytest.fixture
def base_url():
    """Base URL for the API."""
    return URL


@pytest.fixture
def headers():
    """Providing common headers."""
    return {"Content-Type": "application/json"}


@pytest.fixture
def post_data():
    """Providing mock data for creating a post."""
    return {
        "title": "Test Title",
        "userId": "1"
    }


# JSON Schema Validation
POST_SCHEMA = {
    "type": "object",
    "properties": {
        "userId": {"type": ["string", "integer"]},
        "id": {"type": ["string", "integer"]},
        "title": {"type": "string"}
    },
    "required": ["userId", "id", "title"]
}


# Test fetching: GET
def test_fetch_post(base_url, headers):
    """Test fetching a post by ID."""
    post_id = 1
    response = requests.get(f"{base_url}/posts/{post_id}", headers=headers)
    assert response.status_code == 200, "Expected status code 200"
    validate(instance=response.json(), schema=POST_SCHEMA)
    assert response.json()["id"] == post_id, "Fetched post ID does not match"


# Test creating: POST
def test_create_post(base_url, headers, post_data):
    """Test creating a new post."""
    response = requests.post(f"{base_url}/posts", json=post_data, headers=headers)
    assert response.status_code == 201, "Expected status code 201 for post creation"
    created_post = response.json()
    assert created_post["title"] == post_data["title"], "Title does not match"
    assert created_post["userId"] == post_data["userId"], "UserId does not match"


# Test updating: PUT
def test_update_post(base_url, headers, post_data):
    """Test updating an existing post."""
    post_id = 1
    updated_post = post_data.copy()
    updated_post["title"] = "Updated Title"
    response = requests.put(f"{base_url}/posts/{post_id}", json=updated_post, headers=headers)
    assert response.status_code == 200, "Expected status code 200 for post update"
    assert response.json()["title"] == "Updated Title", "Title was not updated"


# Test deleting: DELETE
def test_delete_post(base_url, headers):
    """Test deleting a post."""
    post_id = 1
    response = requests.delete(f"{base_url}/posts/{post_id}", headers=headers)
    assert response.status_code == 200, "Expected status code 200 for post deletion"


# Test fetching comments and filtering: GET
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_fetch_comments(base_url, headers, post_id):
    """Test fetching comments for a post."""
    response = requests.get(f"{base_url}/posts/{post_id}/comments", headers=headers)
    assert response.status_code == 200, "Expected status code 200"
    comments = response.json()
    assert all(comment["postId"] == post_id for comment in comments), "Comments do not match the post ID"


# Mock tests
#GET
def test_fetch_post_mock():
    """Test fetching a post with mocked response."""
    mock_response = {
        "userId": "1",
        "id": "1",
        "title": "Mocked Title"
    }
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = requests.get(f"{URL}/posts/1")
        assert response.status_code == 200
        assert response.json() == mock_response


def test_create_post_mock(post_data):
    """Creating POST with mocked response"""
    mock_response = post_data.copy()
    mock_response["id"] = 101
    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = mock_response

        response = requests.post(f"{URL}/posts", json=post_data)
        assert response.status_code == 201
        assert response.json() == mock_response


def test_timeout_handling():
    """Timeout respond"""
    with patch("requests.get", side_effect=requests.exceptions.Timeout):
        try:
            requests.get(f"{URL}/posts/1", timeout=1)
        except requests.exceptions.Timeout:
            assert True, "Timeout exception"


# Run all tests
if __name__ == "__main__":
    pytest.main()
