import streamlit as st
import pandas as pd
from openai import OpenAI

client = OpenAI(api_key="")

company_data = {
    "TCS": {
        "sector": "IT Services",
        "revenue": "232,000",
        "eps": "115.2",
        "pe": "32.5",
        "roe": "43.2",
        "margin": "24.8",
        "market_cap": "1,300,000",
        "news": "TCS announced a major BFSI sector contract renewal."
    },
    "INFY": {
        "sector": "IT Services",
        "revenue": "148,500",
        "eps": "55.7",
        "pe": "27.3",
        "roe": "30.8",
        "margin": "21.4",
        "market_cap": "710,000",
        "news": "Infosys sees strong deal pipeline growth, but margin pressure continues."
    },
    "RELIANCE": {
        "sector": "Conglomerate",
        "revenue": "800,000",
        "eps": "95.5",
        "pe": "22.4",
        "roe": "12.1",
        "margin": "10.5",
        "market_cap": "1,800,000",
        "news": "Jio Financial demerger complete; retail and energy expansions underway."
    }
}

st.set_page_config(page_title="Investor GPT Brief – India", layout="centered")
st.title("🇮🇳 Investor GPT Brief – India Edition")
st.write("Type a stock to get a 2-minute GPT-powered investor summary with key financial insights.")

company_name = st.selectbox("Select a Company", list(company_data.keys()))
selected = company_data[company_name]

prompt = f"""
You are a financial research assistant. Write a 200-word investor summary for {company_name}, an Indian stock. Use this data:
- Sector: {selected['sector']}
- Revenue: ₹{selected['revenue']} Cr
- EPS: ₹{selected['eps']}
- P/E Ratio: {selected['pe']}
- ROE: {selected['roe']}%
- Net Profit Margin: {selected['margin']}%
- Market Cap: ₹{selected['market_cap']} Cr

Also include this recent update:
{selected['news']}

Summarize the company's financial health, industry position, recent developments, and end with a brief outlook or risk to watch.
"""

if st.button("Generate Summary"):
    with st.spinner("Analyzing company data..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        summary = response.choices[0].message.content
        st.success("Here's your GPT-powered investor brief:")
        st.markdown(summary)
