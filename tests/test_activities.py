def test_get_activities_returns_all_activities(client):
    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)

    # Check that all expected activities are present
    expected_activities = [
        "Chess Club", "Programming Class", "Gym Class", "Basketball Team",
        "Tennis Club", "Art Studio", "Music Band", "Debate Team", "Science Club"
    ]
    for activity in expected_activities:
        assert activity in data
        assert "description" in data[activity]
        assert "schedule" in data[activity]
        assert "max_participants" in data[activity]
        assert "participants" in data[activity]
        assert isinstance(data[activity]["participants"], list)


def test_get_activities_structure(client):
    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()

    # Check structure of one activity
    chess_club = data["Chess Club"]
    assert chess_club["description"] == "Learn strategies and compete in chess tournaments"
    assert chess_club["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert chess_club["max_participants"] == 12
    assert isinstance(chess_club["participants"], list)