def test_signup_valid_activity(client):
    # Act
    response = client.post("/activities/Chess Club/signup?email=test@example.com")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Signed up test@example.com for Chess Club"}

    # Verify participant was added
    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert "test@example.com" in activities["Chess Club"]["participants"]


def test_signup_duplicate_email(client):
    # Arrange
    client.post("/activities/Chess Club/signup?email=test@example.com")

    # Act
    response = client.post("/activities/Chess Club/signup?email=test@example.com")

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_invalid_activity(client):
    # Act
    response = client.post("/activities/NonExistent Activity/signup?email=test@example.com")

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]