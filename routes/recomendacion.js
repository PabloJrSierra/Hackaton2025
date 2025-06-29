const express = require('express');
const router = express.Router();
const { predecirCluster } = require('../controllers/recomendacionController');

router.post('/predecir', predecirCluster);

module.exports = router;