export default function handleResponseFromAPI(promise) {
  promise
    .then((resolve) => (resolve({
      status: 200,
      body: 'Success',
    })))
    .catch((error) => {
      Error(error);
    })
    .then(() => {
      console.log('Got a response from the API');
    });
}
