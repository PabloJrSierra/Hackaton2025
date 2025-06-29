const { spawn } = require('child_process');
const path = require('path');

const predecirCluster = (req, res) => {
  const datos = req.body.datos; // Array de números [1.2, 0.3, 4.5...]

  const scriptPath = path.join(__dirname, '../utils/predict.py');

  const proceso = spawn('python', [scriptPath, ...datos]);

  proceso.stdout.on('data', (data) => {
    res.json({ cluster: data.toString().trim() });
  });

  proceso.stderr.on('data', (data) => {
    console.error(`Error Python: ${data}`);
    res.status(500).send("Error en predicción.");
  });
};

module.exports = { predecirCluster };