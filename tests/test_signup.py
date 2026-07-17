def test_signup_updates_activity_participants(client):
    # Arrange
    activity_name = "Chess Club"
    email = "signup-check@mergington.edu"

    # Act
    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    activities_response = client.get("/activities")

    # Assert
    assert signup_response.status_code == 200
    assert activities_response.status_code == 200
    activity = activities_response.json()[activity_name]
    assert email in activity["participants"]
