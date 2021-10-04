import { redis, createClient } from "redis";

const client = createClient();

(async () => {
  try {
    await client.connect();
    console.log('Redis client connected to the server');
  } catch (e) {
    console.log(`Redis client not connected to the server: ${e.message}`);
  }

})();

function setNewSchool(schoolName, value) {
  const setkey = client.set(schoolName, value, (reply) => {
    return reply
  });
  setkey.then(res => {
    console.log(`Reply: ${res}`);
  });
}

function displaySchoolValue(schoolName) {
  const getkey = client.get(schoolName, (reply) => {
    return reply
  });
  getkey.then(res => {
    console.log(res);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
