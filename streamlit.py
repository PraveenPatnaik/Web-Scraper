from pyngrok import ngrok

!streamlit run app.py &

public_url = ngrok.connect(port=8501)
print(f"🌐 Your Streamlit app is live at: {public_url}")
