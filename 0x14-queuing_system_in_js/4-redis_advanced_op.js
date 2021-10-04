import { print, createClient } from "redis";

const client = createClient();

(async () => {
  try {
    await client.connect();
    console.log('Redis client connected to the server');
  } catch (e) {
    console.log(`Redis client not connected to the server: ${e.message}`);
  }

})();

const hset = client.hSet('HolbertonSchools', 'Portland', '50', (err, reply) => reply);
hset.then(res => console.log(`Reply: ${res}`));
const hse1 = client.hSet('HolbertonSchools', 'Seattle', '80', (reply) => reply);
hse1.then(res => console.log(`Reply: ${res}`));
const hset2 = client.hSet('HolbertonSchools', 'New York', '20', (reply) => reply);
hset2.then(res => console.log(`Reply: ${res}`));
client.hSet('HolbertonSchools', 'Bogota', '20', (reply) => reply);
hset2.then(res => console.log(`Reply: ${res}`));
const hset3 = client.hSet('HolbertonSchools', 'Cali', '40', (reply) => reply);
hset3.then(res => console.log(`Reply: ${res}`));
client.hSet('HolbertonSchools', 'Paris','2', print);

const getall = client.hGetAll('HolbertonSchools', (err, reply) => console.log(reply));
getall.then(res => {
  console.log(res);
})
