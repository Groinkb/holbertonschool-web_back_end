import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

// Create Express server
const app = express();
const port = 1245;

// Product list data
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// Function to get product by id
function getItemById(id) {
  return listProducts.find(product => product.id === id);
}

// Create Redis client
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Reserve stock by id
function reserveStockById(itemId, stock) {
  return setAsync(`item.${itemId}`, stock);
}

// Get current reserved stock by id
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock) : 0;
}

// Format product data
function formatProduct(item) {
  return {
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock
  };
}

// API Routes

// Get all products
app.get('/list_products', (req, res) => {
  const formattedProducts = listProducts.map(formatProduct);
  res.json(formattedProducts);
});

// Get product by ID
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  // Get current stock
  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.stock - currentStock;

  // Return product with current stock
  res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity
  });
});

// Reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  // Check if product exists
  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  // Get current stock
  const currentStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.stock - currentStock;

  // Check if stock available
  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  // Reserve item
  await reserveStockById(itemId, currentStock + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

// Start server
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});