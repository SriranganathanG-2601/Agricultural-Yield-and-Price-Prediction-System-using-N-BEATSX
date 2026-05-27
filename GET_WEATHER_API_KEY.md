# 🔧 How to Get Your Own FREE Weather API Key

## Problem
The demo API key is inactive (401 error). You need your own **FREE** OpenWeatherMap API key.

## ✅ Step-by-Step Setup (2 minutes)

### Step 1: Go to OpenWeatherMap Website
```
https://openweathermap.org/api
```

### Step 2: Sign Up for Free Account
1. Click **"Sign Up"** (top right)
2. Fill in:
   - Email: Your email
   - Password: Create a password
   - Username: Any username
3. Click **"Create Account"**
4. Confirm your email (check inbox)

### Step 3: Get Your API Key
1. Log in to your account
2. Click your username → **"My API keys"**
3. Copy the **default key** (long string of characters)
   - Example: `abc123def456ghi789jkl012mno345`

### Step 4: Add Key to Your App

#### Option A: Quick Fix (Recommended for First Test)
1. Open `frontend/predict.html` in text editor
2. Search for line 500 (Ctrl+G → Go to Line)
3. Find: `const WEATHER_API_KEY = 'e46e49d5b92bcf8d2e62e09242a97ee4';`
4. Replace with: `const WEATHER_API_KEY = 'YOUR_API_KEY_HERE';`
5. Paste your API key between the quotes
6. Save file
7. Refresh browser

**Example**:
```javascript
// Before:
const WEATHER_API_KEY = 'e46e49d5b92bcf8d2e62e09242a97ee4';

// After:
const WEATHER_API_KEY = 'abc123def456ghi789jkl012mno345';
```

#### Option B: Safer Setup (Production)
Store key in environment variable...
```
(For advanced users - see backend documentation)
```

## ✅ Verify It Works

1. Go to Predict page
2. Enter city name: "Mumbai" or "Delhi"
3. Click "Get Weather"
4. Should see weather cards with real data
5. ✅ Success!

## 🆘 Troubleshooting

### "Invalid API key" Error
- [ ] Copy the FULL API key (no extra spaces)
- [ ] Check you saved the file
- [ ] Refresh browser (Ctrl+R)
- [ ] Wait 1-2 minutes for API activation

### "City not found"
- [ ] Use exact city name in English
- [ ] Examples: Mumbai, Delhi, Bangalore, Chennai
- [ ] Avoid abbreviations: ✅ Mumbai, ❌ MUM

### Still Not Working?
1. Check API key in OpenWeatherMap dashboard
2. Verify API is "Active" status
3. Open browser console (F12) for error details
4. Make sure using FREE "Current Weather Data" plan

## 📝 API Key Locations

**In this project**:
- `s:\anti\project\frontend\predict.html` - Line ~500

## ⚠️ Important Notes

- **FREE API Key works for**: ~60 requests/minute, unlimited/month
- **No credit card required** for free tier
- **Your key** in code is fine for demo/development
- **For production**: Use environment variables or backend proxy

## 🔄 How Weather Integration Works

With your API key:
```
You enter "Mumbai"
    ↓
App calls OpenWeatherMap API with YOUR key
    ↓
Gets real-time: Temperature, Humidity, Weather
    ↓
Shows weather cards with live data
    ↓
Backend provides crop recommendations
    ↓
Predictions use REAL conditions instead of historical averages
```

## ✨ What You'll Get

✅ Real-time temperature & humidity  
✅ Weather condition (Clear, Rainy, Cloudy, etc.)  
✅ Smart crop recommendations  
✅ More accurate yield predictions  
✅ Location-specific farming advice  

## Need Help?

**OpenWeatherMap Support**:
- Website: https://openweathermap.org
- FAQ: https://openweathermap.org/faq
- API Docs: https://openweathermap.org/current

**This Project Support**:
- Check [WEATHER_INTEGRATION_GUIDE.md](WEATHER_INTEGRATION_GUIDE.md)
- See [QUICKSTART.md](QUICKSTART.md)

---

**Once you have your API key working, your app will have full real-time weather capabilities!** 🌤️

