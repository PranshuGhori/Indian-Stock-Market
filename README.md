# 🇮🇳 Investor GPT Brief – India Edition

**Investor GPT Brief – India Edition** is a real-time, AI-powered tool that generates concise, 2-minute investor summaries for publicly listed Indian companies using real financial data and OpenAI's GPT models.

## 🚀 Purpose

Retail investors often face information overload — fragmented news, complex ratios, and long reports. This tool simplifies investing by delivering GPT-powered executive briefs that combine:

- 📊 Key financial KPIs  
- 📰 Recent business news  
- ⚠️ Risks or performance outlook  

## 🧠 How It Works

1. Choose a listed Indian stock (e.g., TCS, INFY, RELIANCE)  
2. The app gathers relevant financial metrics and recent news  
3. GPT-3.5 or GPT-4 generates a clean, 200-word investor brief  
4. Output is readable, professional, and mobile-friendly  

## 🔧 Tech Stack

| Component     | Tech/Tool              |
|---------------|------------------------|
| Interface     | Streamlit              |
| AI Model      | OpenAI GPT-3.5 / GPT-4 |
| Data Handling | Pandas                 |
| Deployment    | Streamlit Cloud        |

## 📦 Setup

```bash
pip install streamlit openai pandas
streamlit run app.py


You must have an OpenAI API key to use this tool. Insert it inside app.py:
client = OpenAI(api_key="sk-...")

Sample Output
TCS (Tata Consultancy Services) is a leading Indian IT services firm with ₹232,000 Cr in revenue and a strong ROE of 43.2%. It recently secured a major BFSI sector contract...


📬 Coming Soon
🔄 Live NSE/BSE data via Screener.in API

📰 Daily newsletter delivery

📥 Save-to-PDF and Email export

📊 Sector-wise filtering and comparison

💡 Author
Pranshu Ghori
Data + Finance Enthusiast | Business Tech Builder
🌐 https://pranshughori.com
🔗 LinkedIn