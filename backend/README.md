# Copy Trading Bot - Backend

Python backend for Kotak Neo API copy trading bot.

## 🚀 Installation

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
python main.py
```

## 📝 Configuration

Edit `.env` with your Kotak Neo API credentials:

```env
KOTAK_CONSUMER_KEY=your_key
KOTAK_CONSUMER_SECRET=your_secret
KOTAK_SESSION_TOKEN=your_token
KOTAK_SID=your_sid
KOTAK_SERVER_ID=your_server_id
```

## 📁 Project Structure

```
backend/
├── config/              # Configuration management
├── core/                # Core trading logic
│   ├── broker.py       # Kotak Neo API wrapper
│   ├── signal_monitor.py
│   ├── order_executor.py
│   ├── position_manager.py
│   └── risk_manager.py
├── models/              # Data models
├── utils/               # Utilities
├── database/            # Database models
├── tests/               # Unit tests
├── main.py              # Entry point
└── requirements.txt     # Dependencies
```

## 🔧 API Endpoints

- `GET /api/dashboard` - Dashboard metrics
- `GET /api/positions` - Open positions
- `GET /api/signals` - Signal history
- `GET /api/followers` - Follower accounts
- `GET /api/alerts` - Alerts

## 📦 Dependencies

- neo-api-client - Kotak Neo API
- pandas, numpy - Data processing
- python-dotenv - Environment config
- pydantic - Data validation
- loguru - Logging
