# tests/api/test_reqres_users.py
import requests

BASE = "https://reqres.in/api"

def test_get_users_list():
    r = requests.get(f"{BASE}/users?page=2")
    assert r.status_code == 200
    data = r.json()
    assert "data" in data
    assert isinstance(data["data"], list)

def test_create_and_get_and_delete_user():
    # Create
    payload = {"name":"maria","job":"tester"}
    r = requests.post(f"{BASE}/users", json=payload)
    assert r.status_code == 201
    created = r.json()
    user_id = created.get("id")
    assert user_id is not None

    # GET (nota: ReqRes no realmente persiste, pero vamos a demostrar el encadenamiento)
    r_get = requests.get(f"{BASE}/users/{user_id}")
    # en ReqRes /users/{id} para ids no persistentes puede devolver 404 — validá según la API elegida.
    if r_get.status_code == 200:
        info = r_get.json()
        assert "data" in info

    # DELETE (ReqRes devuelve 204)
    r_del = requests.delete(f"{BASE}/users/{user_id}")
    assert r_del.status_code in (204, 404)  # ok: 204 o 404 dependiendo de la API
