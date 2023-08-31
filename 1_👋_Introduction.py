import streamlit as st

st.set_page_config(page_title = 'Home',page_icon = '👋')

st.title('Who am I?')
st.sidebar.success('Select the pages')

st.header('The Waste Classifier')

col1,col2 = st.columns(2)
col1.image('banner-yolov8.jpg',width=280)
col2.text('The waste classifier uses a state of the\nart ML algorithm - "YOLO" \nto detect and classify the waste objects\nin an image.\nThe algorithm was trained on the dataset\nof 4000 images to categories\n7 types of waste materials')
st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    font-family: 'Courier New', monospace;
}
</style>
""", unsafe_allow_html=True)
st.text("")
st.text("")
st.markdown('''<div class=big-font>How to use the web app?
<ul>
<li>Select the "Classifier Demo" page from the side bar</li>
<li>Upload the image and wait for the Yolo Model to generate the output.</li>
<li>The classifier also has integrate the "Chat GPT model" to generate the results for reduce, recycle and reuse.</li>
</ul></div>''',unsafe_allow_html=True)
