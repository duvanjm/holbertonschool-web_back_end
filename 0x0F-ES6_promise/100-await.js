import { uploadPhoto, createUser } from './utils';

const asyncUploadUser = async () => {
  let obj = {
    photo: null,
    user: null,
  };
  try {
    obj = {
      photo: await uploadPhoto(),
      user: await createUser(),
    };
    return obj;
  } catch (error) {
    return obj;
  }
};

export default asyncUploadUser;
