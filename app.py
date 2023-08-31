import streamlit as st

def find_largest_number(a, b, c):
    return max(a, b, c)

st.title("Find the Largest Number Among Three")

st.write("Enter three numbers to find the largest one:")
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
num3 = st.number_input("Enter the third number")

if st.button("Find Largest"):
    if num1 == num2 == num3:
        st.write("All numbers are equal.")
    else:
        largest = find_largest_number(num1, num2, num3)
        st.write(f"The largest number is: {largest}")
