import { createClient } from "redis";

(async () => {
  try {
    const client = createClient();
    await client.connect();
    console.log('Redis client connected to the server');
  } catch(e) {
    console.log(`Redis client not connected to the server: ${e}`);
  }

})();
