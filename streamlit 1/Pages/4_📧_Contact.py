import streamlit as st

st.header(":mailbox: Get In Touch With Us!")

contact_form = """
<form action="https://formsubmit.co/mbuyiselom94@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
      <textarea name="message" placeholder="Your Message Here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

#use local css file
def local_css(File_name):
    with open(File_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")
    