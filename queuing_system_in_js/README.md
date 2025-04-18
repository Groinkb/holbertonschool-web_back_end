# Queuing System in JavaScript

This project implements a queuing system using Redis and Node.js. The project covers Redis basics, Node.js Redis client, task processing with Kue, and building an Express API with Redis for data storage.

## Learning Objectives

- Running a Redis server
- Performing simple operations with Redis client
- Using Redis client with Node.js
- Storing hash values in Redis
- Dealing with async operations in Redis
- Using Kue as a queue system
- Building Express apps that interact with Redis server
- Building Express apps that interact with Redis server and queue

## Requirements

- All code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All files should end with a new line
- Code should use the `.js` extension

## Installation

### Redis Installation
```bash
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make
```

### Starting Redis Server
```bash
src/redis-server &
```

### Verify Redis is Running
```bash
src/redis-cli ping  # Should return PONG
```

### Node.js Dependencies
```bash
npm install
```

## Tasks Overview

1. **Install Redis and Basic Operations**
   - Set up Redis 
   - Perform basic operations and store dump

2. **Node Redis Client**
   - Connect to Redis with Node.js

3. **Redis Basic Operations in Node.js**
   - Implement set and get operations

4. **Async Operations with Redis**
   - Implement async/await with Redis operations

5. **Redis Advanced Operations**
   - Store and retrieve hash values in Redis

6. **Redis Pub/Sub**
   - Implement publisher/subscriber pattern

7. **Job Creation with Kue**
   - Create job queue with Kue

8. **Job Processing with Kue**
   - Process jobs from a queue

9. **Track Job Progress with Kue**
   - Monitor and update job progress

10. **Job Processor with Blacklist**
    - Implement job processing with conditions

11. **Job Creation Function**
    - Create a reusable job creation function

12. **Testing Job Creation**
    - Write tests for job creation

13. **In-stock API**
    - Build Express API with Redis for product stock management

## Author
BM