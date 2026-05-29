def test_criar_cliente_valido(client):
    payload = {
        "nome": "João",
        "cpf": "12345678901",
        "email": "joao@email.com",
        "telefone": "11999999999",
        "endereco": "Rua X"
    }
    response = client.post("/clientes/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["cpf"] == "12345678901"
    assert data["email"] == "joao@email.com"
    assert "id" in data

def test_criar_cliente_cpf_duplicado(client):
    payload = {
        "nome": "João",
        "cpf": "12345678901",
        "email": "joao@email.com",
        "telefone": "11999999999",
        "endereco": "Rua X"
    }
    client.post("/clientes/", json=payload) # Cria o primeiro
    
    payload2 = {
        "nome": "Maria",
        "cpf": "12345678901", # CPF Igual
        "email": "maria@email.com",
        "telefone": "11999999999",
        "endereco": "Rua Y"
    }
    response2 = client.post("/clientes/", json=payload2)
    assert response2.status_code == 400
    assert "CPF já cadastrado" in response2.json()["detail"]

def test_criar_cliente_email_duplicado(client):
    payload = {
        "nome": "João",
        "cpf": "12345678901",
        "email": "joao@email.com",
        "telefone": "11999999999",
        "endereco": "Rua X"
    }
    client.post("/clientes/", json=payload) # Cria o primeiro
    
    payload2 = {
        "nome": "Maria",
        "cpf": "10987654321", 
        "email": "joao@email.com", # Email Igual
        "telefone": "11999999999",
        "endereco": "Rua Y"
    }
    response2 = client.post("/clientes/", json=payload2)
    assert response2.status_code == 400
    assert "Email já cadastrado" in response2.json()["detail"]

def test_listar_clientes(client):
    payload = {
        "nome": "João",
        "cpf": "12345678901",
        "email": "joao@email.com",
        "telefone": "11999999999",
        "endereco": "Rua X"
    }
    client.post("/clientes/", json=payload)
    
    response = client.get("/clientes/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_buscar_cliente_por_id(client):
    payload = {
        "nome": "João",
        "cpf": "12345678901",
        "email": "joao@email.com",
        "telefone": "11999999999",
        "endereco": "Rua X"
    }
    create_response = client.post("/clientes/", json=payload)
    cliente_id = create_response.json()["id"]

    response = client.get(f"/clientes/{cliente_id}")
    assert response.status_code == 200
    assert response.json()["id"] == cliente_id
