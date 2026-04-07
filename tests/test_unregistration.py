def test_unregistration_valid_participant(client):
    # Arrange
    client.post("/activities/Chess Club/signup?email=test@example.com")

    # Act
    response = client.delete("/activities/Chess Club/participants?email=test@example.com")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Removed test@example.com from Chess Club"}

    # Verify participant was removed
    activities_response = client.get("/activities")
    activities = activities_response.json()
    assert "test@example.com" not in activities["Chess Club"]["participants"]


def test_unregistration_non_existent_participant(client):
    # Act
    response = client.delete("/activities/Chess Club/participants?email=nonexistent@example.com")

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_unregistration_invalid_activity(client):
    # Act
    response = client.delete("/activities/NonExistent Activity/participants?email=test@example.com")

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]