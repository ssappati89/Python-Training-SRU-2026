import streamlit as st
import pandas as pd
st.title("Demo App")
st.write("This is a simple demo app using Streamlit.")
st.write("You can use this app to display data and create interactive visualizations.") 
# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
# Display the DataFrame
st.write("Here is a sample DataFrame:")
st.dataframe(df)