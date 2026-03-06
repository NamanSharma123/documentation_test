const API_BASE = 'http://127.0.0.1:8000';

// GET all products
export async function getProducts() {
    const response = await fetch(`${API_BASE}/products/`);
    return await response.json();
}

// CREATE a new product
export async function createProduct(data) {
    const response = await fetch(`${API_BASE}/products/`, {
        method: 'POST',
        headers: {'content-type': 'application/json'},
        body: JSON.stringify(data),
    });
    return await response.json();
}
