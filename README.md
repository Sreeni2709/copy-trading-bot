# Copy Trading Bot - Kotak Neo API

A sophisticated copy trading bot that automatically replicates a trader's signals using the **Kotak Neo Trading API**. This bot monitors signals from master traders and executes synchronized trades across follower accounts with advanced risk management.

## 🎯 Features

✅ **Signal Replication**
- Real-time signal monitoring from master trader accounts
- Automatic order execution on follower accounts
- Support for multiple master traders and followers

✅ **Risk Management**
- Position sizing based on follower account size
- Maximum drawdown limits
- Daily loss limits
- Trailing stop-loss
- Profit targets

✅ **Advanced Trading**
- Market orders, Limit orders, Stop-loss orders
- Option trading (CE/PE)
- Partial exit support
- Multi-leg strategies

✅ **Monitoring & Alerts**
- Real-time trade monitoring
- Email/SMS notifications
- Telegram alerts
- Live dashboard
- Trade history logging

✅ **Modern Dashboard**
- React 18 + TypeScript frontend
- Real-time P&L charts
- Live performance metrics
- Responsive design

## 📁 Project Structure

```
copy-trading-bot/
├── backend/                 # Python Flask API
│   ├── config/
│   ├── core/
│   ├── models/
│   ├── utils/
│   ├── database/
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/                # React Dashboard
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   ├── vite.config.ts
│   └── index.html
└── LICENSE
```

## 🚀 Quick Start

### Backend

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your Kotak Neo credentials
python main.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Access dashboard: `http://localhost:5173`

## ⚙️ Configuration

Edit `.env` files with:
- Kotak Neo API credentials
- Master trader settings
- Risk management parameters
- Notification channels

## 📖 Documentation

- [Backend Setup](./backend/README.md)
- [Frontend Setup](./frontend/README.md)

## ⚠️ Disclaimer

This is a trading bot for educational purposes. Trading involves substantial risk. Always test thoroughly before live trading.

## 📄 License

MIT License - See LICENSE file
