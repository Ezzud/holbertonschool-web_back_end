const { readDB } = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    const databaseFile = process.argv[2];
    try {
      const students = await readDB(databaseFile);
      let output = 'This is the list of our students\n';
      Object.keys(students)
        .sort((a, b) => a.localeCompare(b))
        .forEach((field) => {
          const list = students[field].join(', ');
          output += `Number of students in ${field}: ${students[field].length}. List: ${list}\n`;
        });
      res.status(200).send(output.trim());
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const databaseFile = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    try {
      const students = await readDB(databaseFile);
      const list = students[major].join(', ');
      res.status(200).send(`List: ${list}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
