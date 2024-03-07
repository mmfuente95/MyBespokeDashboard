import streamlit as st
import requests

def classify_item(item):
    data = {'item': item}
    # Update the URL to match the deployed app URL
    # Example URL: 'https://your-app-name.streamlit.io/classify'
    response = requests.post('https://mybespokedashboard-iyfaupeeciwhi3relcmxbm.streamlit.io/classify', json=data)
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
