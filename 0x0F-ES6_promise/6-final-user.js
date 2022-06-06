import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    // eslint-disable-next-line consistent-return
    .then((values) => {
      if (values[0] === 'fulfilled') {
        return values;
      }
    })
    // eslint-disable-next-line no-console
    .catch((err) => console.log(err));
}
