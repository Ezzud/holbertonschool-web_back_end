const fs = require('fs');

function readDB(filepath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filepath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const students = {};
      const lines = data.trim().split('\n').slice(1);

      lines.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
      });
      resolve(students);
    });
  });
}

module.exports = readDB;
