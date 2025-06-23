import re
"WAP to find out the even number till user input"
# num = int(input("Enter a number: "))
# # if(num > 0):
# if(num !=  0):
#     for i in range(1, num+1):
#         if(i % 2 == 0):
#             print(i)
# # elif(num < 0):
# #     for i in range(num , 1):
# #         if( i % 2 == 0):
# #             print(i)
# else: 
#     print("Enter number greater than zero")

"WAP to write fibbonacci series"
# num = int(input("Enter the numbers of terms: "))
# a = 0
# b = 1

# for i in range(num):
#     print (a, end =" ")
#     next = a+b
#     a = b
#     b = next

"WAP to find out the sum of first n natural number with avg"
# count = 0
# sum = 0

# num = int(input("Enter the number: "))
# for i in range(1, num+1):
#     sum +=i
#     count += 1
# avg = (sum/count)
# print("Sum of first ", num, "natural numbers is " ,sum )
# print("Average of first ", num, "natural numbers is " ,avg )


"Password Strength Checker"
"""Input a password
Check for length, uppercase, digits, and special characters"""

# import re
"""def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    strength_levels = {
        5: "Very Strong 💪",
        4: "Strong 👍",
        3: "Moderate ⚖️",
        2: "Weak 😕",
        1: "Very Weak ❌",
        0: "Extremely Weak ❌"
    }

    return strength_levels.get(score, "Invalid")

# Main Program
pwd = input("Enter your password: ")
strength = check_password_strength(pwd)
print("Password Strength:", strength)"""

# Install first with: pip install streamlit
import streamlit as st


st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password", type="password")

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Include digits.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("Add special characters (!@#...).")

    strength = {
        5: "Very Strong 💪",
        4: "Strong 👍",
        3: "Moderate ⚖️",
        2: "Weak 😕",
        1: "Very Weak ❌",
        0: "Extremely Weak ❌"
    }

    return strength[score], suggestions

if password:
    strength, suggestions = check_password_strength(password)
    st.success(f"Password Strength: {strength}")
    if suggestions:
        st.info("Suggestions to improve:")
        for tip in suggestions:
            st.markdown(f"- {tip}")

