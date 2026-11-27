def test_create_task_returns_201(client):
    response = client.post("/tasks", json={"title": "Write report"})

    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["title"] == "Write report"
    assert body["status"] == "todo"

def test_invalid_status_is_rejected(client):
    response = client.post(
        "/tasks", json={"title": "Write report", "status": "invalid"}
    )

    assert response.status_code == 422





def test_blank_title_is_rejected(client):
    response = client.post("/tasks", json={"title": ""})
    assert response.status_code == 422

def test_unknown_task_id_returns_404_on_get_patch_delete(client):
    assert client.get("/tasks/999").status_code == 404
    assert client.patch("/tasks/999", json={"status": "done"}).status_code == 404
    assert client.delete("/tasks/999").status_code == 404

def test_non_positive_task_id_is_rejected(client):
    assert client.get("/tasks/0").status_code == 422

def test_unknown_field_id_on_create_is_rejected(client):
    response = client.post(
        "/tasks", json={"title": "Write report", "id": 999}
    )
    assert response.status_code == 422

def test_patch_status_only_updates_status(client):
    created = client.post(
        "/tasks", json={"title": "Write report", "description": "Draft v1"}
    ).json()
    response = client.patch(f"/tasks/{created['id']}", json={"status": "done"})
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "done"
    assert body["title"] == "Write report"
    assert body["description"] == "Draft v1"

def test_patch_title_null_is_rejected(client):
    created = client.post("/tasks", json={"title": "Write report"}).json()
    response = client.patch(f"/tasks/{created['id']}", json={"title": None})
    assert response.status_code == 422

def test_delete_returns_204_then_get_returns_404(client):
    created = client.post("/tasks", json={"title": "Write report"}).json()
    task_id = created["id"]
    delete_resp = client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 204
    assert client.get(f"/tasks/{task_id}").status_code == 404