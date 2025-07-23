import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    h1 {
        color: #1f77b4;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    .stButton>button {
        color: white;
        background-color: #28a745;
        border-radius: 12px;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #218838;
    }
    .stTextInput, .stNumberInput {
        color: black;
    }
    h3, p, .stMarkdown, .stSlider {
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("Budget Planner 💰")

# Display an image below the title
st.image("https://www.example.com/finance-image.jpg", use_column_width=True)

# Step 1: Enter total budget
st.markdown("### 📌 Step 1: Enter Your Total Budget")
budget = st.number_input("Total Budget:", min_value=0)

st.markdown("<hr>", unsafe_allow_html=True)

# Step 2: Initialize session state
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = []

# Step 3: Add a financial task
st.markdown("### 📌 Step 2: Add an Expense")
expense_name = st.text_input("Expense Name (e.g., Rent, Food):")
expense_amount = st.number_input("Expense Amount:", min_value=0)

if st.button("Add Expense ➕"):
    if expense_name and expense_amount > 0:
        st.session_state['expenses'].append({'name': expense_name, 'amount': expense_amount})
        st.success(f"Expense '{expense_name}' of {expense_amount} added!")
    else:
        st.warning("Please enter a valid expense name and amount.")

# Step 4: Display the expenses
if st.session_state['expenses']:
    st.markdown("### 📝 Your Expenses:")
    total_spent = sum(exp['amount'] for exp in st.session_state['expenses'])
    for exp in st.session_state['expenses']:
        st.write(f"- **{exp['name']}**: **{exp['amount']}**")
    
    # Calculate remaining budget
    remaining = budget - total_spent
    st.markdown(f"### 📊 Total Expenses: **{total_spent}**")
    st.markdown(f"### 💵 Remaining Balance: **{remaining}**")

st.markdown("<hr>", unsafe_allow_html=True)

# Clear all expenses
if st.button("Clear All Expenses 🗑️"):
    st.session_state['expenses'] = []
    st.success("All expenses cleared!")