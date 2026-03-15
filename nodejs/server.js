const express = require('express');
const cors = require('cors');
const lunar = require('lunar-javascript');

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok', service: 'nodejs' });
});

// Main convert endpoint
app.post('/convert', (req, res) => {
  const { type, action, day, month, year, is_leap } = req.body;
  
  if (!type) {
    return res.status(400).json({ error: 'Missing type parameter' });
  }
  
  try {
    if (type === 'chinese') {
      return handleChineseConversion(req, res);
    }
    
    return res.status(400).json({ error: `Unknown type: ${type}` });
  } catch (error) {
    console.error('Conversion error:', error);
    res.status(500).json({ error: error.message });
  }
});

function handleChineseConversion(req, res) {
  const { action, day, month, year, is_leap } = req.body;
  
  if (!action) {
    return res.status(400).json({ error: 'Missing action parameter' });
  }
  
  if (action === 'to') {
    // Gregorian -> Chinese
    if (!day || !month || !year) {
      return res.status(400).json({ error: 'Missing day, month, or year' });
    }
    
    try {
      const solarDate = lunar.Solar.fromYmd(year, month, day);
      const lunarDate = solarDate.getLunar();
      
      const result = {
        year: lunarDate.getYear(),
        month: lunarDate.getMonth(),
        day: lunarDate.getDay(),
        is_leap: false,
        chinese_year: lunarDate.getYearInChinese(),
        chinese_month: lunarDate.getMonthInChinese(),
        chinese_day: lunarDate.getDayInChinese()
      };
      
      res.json(result);
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
    
  } else if (action === 'from') {
    // Chinese -> Gregorian
    if (!day || !month || !year) {
      return res.status(400).json({ error: 'Missing day, month, or year' });
    }
    
    try {
      // lunar-javascript doesn't have direct Lunar -> Solar conversion
      // We need to iterate or use a workaround
      // For simplicity, we'll return an error indicating this needs more work
      res.status(400).json({ error: 'Chinese to Gregorian conversion not yet implemented' });
    } catch (error) {
      res.status(500).json({ error: error.message });
    }
    
  } else {
    res.status(400).json({ error: `Unknown action: ${action}` });
  }
}

// Start server
app.listen(PORT, () => {
  console.log(`Node.js service running on port ${PORT}`);
});
