const fs = require('fs');

function countStudents(path) {
  try {
    const content = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' }).split('\n');
    let total = content.length - 1;
    for (const item of content) {
      if (item.length === 0) {
        total -= 1;
      }
    }
    console.log(`Number of students: ${total}`);
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
