import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
import matplotlib.pyplot as plt

# Download VADER lexicon
nltk.download("vader_lexicon")
analyzer = SentimentIntensityAnalyzer()
translator = Translator()

# Page config
st.set_page_config(page_title="Multilingual Sentiment ChatBot", page_icon="🌍", layout="centered")

st.title("🌍 Multilingual Sentiment ChatBot")
st.markdown("Talk to me in any language and I'll analyze your sentiment. 🌐")

# Language selection
languages = {
    'Telugu': 'te',
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Hindi': 'hi',
    'Portuguese': 'pt',
    'Chinese': 'zh-cn',
    'Arabic': 'ar'
}
selected_language = st.selectbox("Choose your language:", list(languages.keys()))
selected_language_code = languages[selected_language]

# Input box
user_input = st.text_input(f"Type your sentence in {selected_language}:")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Analyze sentiment
if user_input:
    translated_input = translator.translate(user_input, dest="en").text
    scores = analyzer.polarity_scores(translated_input)
    compound = scores["compound"]
    pos = scores["pos"]
    neu = scores["neu"]
    neg = scores["neg"]

    if compound >= 0.05:
        sentiment = "😊 Positive"
        english_response = "That sounds great! I'm happy for you. 🌟"
    elif compound <= -0.05:
        sentiment = "😞 Negative"
        english_response = "I'm sorry to hear that. Want to talk more about it?"
    else:
        sentiment = "😐 Neutral"
        english_response = "Hmm, sounds neutral. Got anything else on your mind?"

    translated_response = translator.translate(english_response, dest=selected_language_code).text

    # Save messages
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", f"**{sentiment}**<br>{translated_response}"))

    # Show sentiment scores
    st.markdown("### 🧠 Sentiment Scores")
    st.markdown(f"- **Positive**: {pos:.2f}")
    st.progress(pos)
    st.markdown(f"- **Neutral**: {neu:.2f}")
    st.progress(neu)
    st.markdown(f"- **Negative**: {neg:.2f}")
    st.progress(neg)
    st.markdown(f"- **Compound (Confidence)**: `{compound:.2f}`")

    # Bar chart visualization
    fig, ax = plt.subplots()
    sentiments = ['Positive', 'Neutral', 'Negative']
    scores_list = [pos, neu, neg]
    bar_colors = ['#66BB6A', '#FFA726', '#EF5350']
    ax.bar(sentiments, scores_list, color=bar_colors)
    ax.set_ylim([0, 1])
    ax.set_ylabel('Score')
    ax.set_title('Sentiment Confidence Scores')
    st.pyplot(fig)

# Show latest chat in main area
if st.session_state.chat_history:
    last_user, last_bot = st.session_state.chat_history[-2:]
    st.markdown(f'<div class="message user">{last_user[1]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="message bot">{last_bot[1]}</div>', unsafe_allow_html=True)

# Sidebar: full chat + sentiment recap
with st.sidebar:
    st.markdown("## 💬 Full Chat History")
    for sender, message in st.session_state.chat_history:
        role = "🧑 You" if sender == "user" else "🤖 Bot"
        st.markdown(f"**{role}:** {message}", unsafe_allow_html=True)

    st.markdown("---")
    if user_input:
        st.markdown("## 📊 Last Sentiment Scores")
        st.markdown(f"- Positive: {pos:.2f}")
        st.markdown(f"- Neutral: {neu:.2f}")
        st.markdown(f"- Negative: {neg:.2f}")
        st.markdown(f"- Compound: `{compound:.2f}`")

    if st.button("🗑️ Clear History"):
        st.session_state.chat_history.clear()

# CSS Styling
st.markdown("""
    <style>
    .message {
        padding: 1em;
        border-radius: 10px;
        margin-bottom: 1em;
        max-width: 80%;
        display: flex;
        align-items: center;
        color: #000;
        font-size: 1rem;
        line-height: 1.4;
    }
    .user {
        background-color: #C1E1C1;
        margin-left: auto;
        justify-content: flex-end;
    }
    .bot {
        background-color: #F1F0F0;
        margin-right: auto;
        justify-content: flex-start;
    }
    </style>
""", unsafe_allow_html=True)





