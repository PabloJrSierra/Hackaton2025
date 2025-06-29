import express, { json } from 'express';
const app = express();
import recomendacionRoutes from './routes/recomendacion.js';
import cors from 'cors';

app.use(cors());
app.use(json());
app.use('/api', recomendacionRoutes);

app.listen(3001, () => console.log("Servidor corriendo en puerto 3001"));
