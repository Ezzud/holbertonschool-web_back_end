const { Router } = require('express');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

const routes = Router();

routes.get('/', AppController.getHomepage);
routes.get('/students', StudentsController.getAllStudents);
routes.get('/students/:major', StudentsController.getAllStudentsByMajor);

module.exports = routes;
