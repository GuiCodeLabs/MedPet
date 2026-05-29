def test_criar_pet_valido(client):
    # Cria cliente primeiro
    cliente_payload = {
        "nome": "João",
        "cpf": "12345678901",
        "email": "joao@email.com"
    }
    cliente_response = client.post("/clientes/", json=cliente_payload)
    cliente_id = cliente_response.json()["id"]

    # Cria o pet
    pet_payload = {
        "nome": "Rex",
        "especie": "Cachorro",
        "raca": "Labrador",
        "idade": 3,
        "peso": 20.5,
        "cliente_id": cliente_id
    }
    response = client.post("/pets/", json=pet_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Rex"
    assert data["cliente_id"] == cliente_id
    assert "id" in data

def test_criar_pet_tutor_inexistente(client):
    pet_payload = {
        "nome": "Rex",
        "especie": "Cachorro",
        "cliente_id": 9999
    }
    response = client.post("/pets/", json=pet_payload)
    assert response.status_code == 400
    assert "tutor" in response.json()["detail"].lower()

def test_listar_pets(client):
    cliente_payload = {
        "nome": "João",
        "cpf": "12345678901",
        "email": "joao@email.com"
    }
    cliente_response = client.post("/clientes/", json=cliente_payload)
    cliente_id = cliente_response.json()["id"]

    pet_payload = {
        "nome": "Rex",
        "especie": "Cachorro",
        "cliente_id": cliente_id
    }
    client.post("/pets/", json=pet_payload)

    response = client.get("/pets/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_listar_pets_por_tutor(client):
    cliente_payload = {
        "nome": "João",
        "cpf": "12345678901",
        "email": "joao@email.com"
    }
    cliente_response = client.post("/clientes/", json=cliente_payload)
    cliente_id = cliente_response.json()["id"]

    pet_payload = {
        "nome": "Rex",
        "especie": "Cachorro",
        "cliente_id": cliente_id
    }
    client.post("/pets/", json=pet_payload)

    response = client.get(f"/pets/tutor/{cliente_id}")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["cliente_id"] == cliente_id
