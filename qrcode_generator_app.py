import streamlit as st
import segno
import time

# page set up
st.set_page_config(
    page_title="QR CODE GENRATOR",
    page_icon="😃")

# add a banner
st.image("images/banner.jpg")

st.title("QR CODE GENERATOR")

# add a text box and store in a variable
url = st.text_input("Please enter the url you want to encode:")


# definition to create a qr code
def generate_qrcode(url):
    # segno library, make_qr function
    qrcode = segno.make_qr(url)
    qrcode.to_pil(scale=5,
                  dark="red").save("images/qrcode_streamlit.png")


if url:
    with st.spinner("Generate the QR Code..."):
        time.sleep(2)
    generate_qrcode(url)
    st.image("images/qrcode_streamlit.png",
             caption="Here is the QR Code"
             )

st.markdown("<br><hr><center>Made by Sela")