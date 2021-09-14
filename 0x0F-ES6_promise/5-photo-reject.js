export default function uploadPhoto(filename) {
  return new Promise(() => {
    throw `${filename} cannot be processed`;
  });
}
