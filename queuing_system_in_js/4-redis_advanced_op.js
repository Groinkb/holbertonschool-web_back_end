import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

// Create a hash
const key = 'HolbertonSchools';
const cities = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};

// Store hash in Redis
for (const [city, students] of Object.entries(cities)) {
  client.hset(key, city, students, redis.print);
}

// Retrieve and display the hash
client.hgetall(key, (err, reply) => {
  console.log(reply);
});