def test_unregister_participant_removes_email_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    assert signup_response.status_code == 200

    # Act
    unregister_response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    activities_response = client.get("/activities")

    # Assert
    assert unregister_response.status_code == 200
    assert activities_response.status_code == 200
    activity = activities_response.json()[activity_name]
    assert email not in activity["participants"]
