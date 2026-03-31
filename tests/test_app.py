def test_root_redirects_to_static(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_get_activities_returns_all_activities(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert "Chess Club" in body
    assert "Programming Class" in body
    assert "Gym Class" in body


def test_signup_for_existing_activity_adds_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Ensure participant not already in list
    initial_response = client.get("/activities")
    assert email not in initial_response.json()[activity]["participants"]

    # Act
    signup_response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert signup_response.status_code == 200
    assert signup_response.json() == {"message": f"Signed up {email} for {activity}"}

    # Verify new participant is present after signup
    final_response = client.get("/activities")
    assert email in final_response.json()[activity]["participants"]


def test_signup_for_unknown_activity_returns_404(client):
    # Arrange
    activity = "Unknown Club"
    email = "anyone@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
