const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
const PORT = 3000;

// Enable CORS
app.use(cors());

// Proxy endpoint
app.get('/api/gold-price', async (req, res) => {
  try {
    const response = await axios.get('http://api.btmc.vn/api/BTMCAPI/getpricebtmc?key=9999');
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Không thể lấy dữ liệu' });
  }
});

app.listen(PORT, () => {
  console.log(`Server proxy đang chạy tại http://localhost:${PORT}`);
});