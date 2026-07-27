import streamlit as st
import pandas as pd
# Create a simple Streamlit app for mathematcial table with user input
st.title("Mathematical Table")
num1 = st.number_input("Enter the first number:", step=1, value=1)
num2 = st.number_input("Enter the second number:", step=1, value=10)
operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])
#if st.button("Generate Table"):
#    table_data = []
#    for i in range(num1, num2 + 1):
#        if operation == "Addition":
#            result = i + num1
#        elif operation == "Subtraction":
#            result = i - num1
#        elif operation == "Multiplication":
#            result = i * num1
#        elif operation == "Division":
#            if num1 != 0:
#                result = i / num1
#            else:
#                result = "Error: Division by zero"
#        table_data.append({"Number": i, "Result": result})
#    df = pd.DataFrame(table_data)
#    st.write(f"Here is the {operation} table from {num1} to {num2}:")
#    st.dataframe(df)