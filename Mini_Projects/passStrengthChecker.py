import streamlit as st
import re

# ---- Custom CSS ----
st.set_page_config(page_title="Password Strength Checker", layout="centered")
st.markdown("""
    <style>
        .main-container {
            background-color: #f9f9f9;
            color: red;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            font-family: 'Segoe UI', sans-serif;
        }
        .suggestions {
            margin-top: 10px;
            color: #d9534f;
            font-size: 16px;
        }
        .footer {
            margin-top: 30px;
            font-size: 14px;
            color: #888;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Container Starts ----
st.markdown("<div>", unsafe_allow_html=True)
st.title("🔐 Password Strength Checker")

# ---- Password Input ----
password = st.text_input("Enter your password", type="password")

# ---- Password Strength Checker ----
def check_password_strength(pwd):
    score = 0
    suggestions = []

    if len(pwd) >= 8:
        score += 1
    else:
        suggestions.append("⚠️ Use at least 8 characters.")

    if re.search(r'[A-Z]', pwd):
        score += 1
    else:
        suggestions.append("⚠️ Add at least one uppercase letter.")

    if re.search(r'[a-z]', pwd):
        score += 1
    else:
        suggestions.append("⚠️ Add at least one lowercase letter.")

    if re.search(r'\d', pwd):
        score += 1
    else:
        suggestions.append("⚠️ Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd):
        score += 1
    else:
        suggestions.append("⚠️ Use at least one special character.")

    return score, suggestions

# ---- Show Results ----
if password:
    score, suggestions = check_password_strength(password)
    levels = ["🟥 Very Weak", "🟧 Weak", "🟨 Moderate", "🟩 Strong", "🟩 Very Strong", "🟩 Excellent"]
    st.subheader("Password Strength:")
    st.progress(score / 5)
    st.success(levels[score])

    if suggestions:
        st.markdown("<div class='suggestions'>", unsafe_allow_html=True)
        for item in suggestions:
            st.markdown(f"- {item}")
        st.markdown("</div>", unsafe_allow_html=True)

# ---- Password Rules ----
with st.expander("📋 Password Rules"):
    st.markdown("""
    - Minimum **8 characters**
    - At least **one uppercase** letter
    - At least **one lowercase** letter
    - At least **one digit**
    - At least **one special character** (e.g., !, @, #, etc.)
    """)

# ---- End Container ----
st.markdown("</div>", unsafe_allow_html=True)

# ---- Footer ----
# st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
