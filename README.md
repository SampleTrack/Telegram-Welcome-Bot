# 🤖 Telegram Welcome Bot

A professional, fully-featured Telegram group welcome bot built with Python & Pyrogram. Automatically welcomes new members, manages group rules, bans spam bots, and keeps your group clean — all configurable via simple commands.

---

## ✨ Features

- 👋 Auto welcome new members with custom messages
- 📜 Group rules with inline button
- 🤖 Auto ban spam bots on join
- 🧹 Clean join/leave system messages
- ⚙️ Toggle settings via inline buttons
- 📋 Error log file + `/logs` command
- 📢 Log channel support for all events
- 🌍 Multi-group support (one bot, many groups)
- 🗄️ MongoDB for persistent group settings
- 🚀 Ready to deploy on Render, Heroku, Railway or VPS

---

## 📋 Requirements

- Python 3.10+
- MongoDB Atlas account (free)
- Telegram API credentials

---

## ⚙️ Setup Guide

### Step 1 — Get Telegram API Credentials
1. Go to [my.telegram.org](https://my.telegram.org)
2. Login with your phone number
3. Click **"API Development Tools"**
4. Create a new app
5. Copy your `API_ID` and `API_HASH`

### Step 2 — Create Bot Token
1. Open Telegram and search **@BotFather**
2. Send `/newbot`
3. Follow the steps
4. Copy your `BOT_TOKEN`

### Step 3 — Setup MongoDB
1. Go to [mongodb.com/atlas](https://mongodb.com/atlas)
2. Create a free account
3. Create a free cluster
4. Click **Connect → Drivers**
5. Copy your `MONGO_URI`

### Step 4 — Configure Environment
1. Rename `.env.example` to `.env`
2. Fill in all values:

```env
API_ID=12345678
API_HASH=your_api_hash_here
BOT_TOKEN=your_bot_token_here
MONGO_URI=your_mongodb_uri_here
DB_NAME=welcome_bot
LOG_CHANNEL_ID=-100xxxxxxxxxx
SUPPORT_LINK=https://t.me/your_support
BOT_NAME=Welcome Bot
```

### Step 5 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 6 — Run Locally
```bash
python main.py
```

---

## 🚀 Deployment

### Render (Recommended — Free)
1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. New → **Worker Service**
4. Connect your GitHub repo
5. Add environment variables from `.env`
6. Deploy!

### Heroku
1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Run:
```bash
heroku create your-bot-name
heroku config:set API_ID=xxx API_HASH=xxx BOT_TOKEN=xxx MONGO_URI=xxx
git push heroku main
heroku ps:scale worker=1
```

### Railway
1. Go to [railway.app](https://railway.app)
2. New Project → **Deploy from GitHub**
3. Add environment variables
4. Deploy!

### VPS / Linux Server
```bash
git clone your-repo-url
cd telegram-welcome-bot
pip install -r requirements.txt
cp .env.example .env
nano .env  # fill in your values
python main.py
```

For 24/7 on VPS use `screen` or `pm2`:
```bash
# Using screen
screen -S welcomebot
python main.py
# Press Ctrl+A then D to detach

# Using pm2
pm2 start main.py --name welcomebot --interpreter python3
```

---

## 📌 Bot Commands

| Command | Description | Who |
|---|---|---|
| `/start` | Bot info & commands | Everyone |
| `/setwelcome` | Set custom welcome message | Admins |
| `/resetwelcome` | Reset welcome to default | Admins |
| `/setrules` | Set group rules | Admins |
| `/settings` | Toggle bot settings | Admins |
| `/logs` | Get error log file | Bot Owner |

---

## 🎨 Welcome Message Placeholders

| Placeholder | Output |
|---|---|
| `{name}` | Clickable mention of user |
| `{first_name}` | User's first name |
| `{last_name}` | User's last name |
| `{username}` | @username or first name |
| `{group}` | Group name |
| `{id}` | User ID |
| `{count}` | Member count |

**Example:**
```
/setwelcome Hey {name}! Welcome to {group} 🎉
We now have {count} members!
```

---

## 📢 Log Channel Setup

1. Create a Telegram channel
2. Add your bot as **Admin**
3. Copy the channel ID (starts with `-100`)
4. Add to `.env` as `LOG_CHANNEL_ID`

Bot will send logs for:
- ✅ Bot started
- 👤 New member joined
- 🤖 Bot banned
- 🔴 Errors

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| Pyrogram | Telegram MTProto library |
| TgCrypto | Fast encryption for Pyrogram |
| Motor | Async MongoDB driver |
| MongoDB Atlas | Database |
| python-dotenv | Environment variables |
| APScheduler | Background tasks |

---

## 📞 Support

Having issues? Contact support:
- Telegram: [@your_support](https://t.me/your_support)
- Response time: Within 24 hours

---

## 📄 License

This item is licensed under the **Envato Regular License**.
© 2025 All Rights Reserved.
