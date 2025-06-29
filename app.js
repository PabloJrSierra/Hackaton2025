const express = require('express');
const app = express();
const recomendacionRoutes = require('./routes/recomendacion');
const cors = require('cors');

app.use(cors());
app.use(express.json());
app.use('/api', recomendacionRoutes);

app.listen(3001, () => console.log("Servidor corriendo en puerto 3001"));
