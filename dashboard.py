import streamlit as st
import requests

def classify_item(item):
    data = {'item': item}
    response = requests.post('http://127.0.0.1:5000/classify', json=data)
    result = response.json()['result']
    return result

def main():
    st.title("Item Classifier")
    item = st.text_input("Enter an item:")
    
    if st.button("Classify"):
        result = classify_item(item)
        st.write(result)

if __name__ == "__main__":
    main()
