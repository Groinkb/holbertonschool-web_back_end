import redis from 'redis';

const client = redis.createClient();
const channel = 'holberton school channel';

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

// Subscribe to the channel
client.subscribe(channel);

// Listen for messages
client.on('message', (channel, message) => {
  console.log(message);

  // If message is KILL_SERVER, unsubscribe and quit
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});