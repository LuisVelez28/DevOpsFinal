# app/tests/test_routes.py
import pytest
from httpx import AsyncClient, ASGITransport 
from app import app

@pytest.mark.asyncio
async def test_metrics_endpoint():
    """Prueba que el endpoint /metrics responde correctamente."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/metrics")
    
    assert response.status_code == 200
    assert "http_requests_total" in response.text

@pytest.mark.asyncio
async def test_add_client_successfully():
    """Prueba que se puede añadir un nuevo cliente correctamente."""
    client_data = {"name": "Cliente de Prueba"}
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/clients", json=client_data)
        
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["message"] == "Client added"
    assert "client_id" in response_json