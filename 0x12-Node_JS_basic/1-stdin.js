console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (data) => {
  process.stdout.write(`Your name is: ${data}`);
  if (process.stdin.isTTY) {
    process.exit();
  } else {
    process.stdout.write('This important software is now closing\n');
    process.exit();
  }
});
