import streamlit as st

st.set_page_config(layout='wide')

st.markdown("# Daniel du Preez")
st.sidebar.markdown("# Home")
st.sidebar.markdown("[Github](https://github.com/DanDuPreez)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/daniel-du-preez/)")
st.sidebar.markdown("[Kaggle](https://www.kaggle.com/drakendan)")
st.sidebar.markdown("[Medium](https://medium.com/@dandupreez)")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Profile Pic.png", width=300)
    st.markdown("[Github](https://github.com/DanDuPreez)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/daniel-du-preez/)")
    st.markdown("[Kaggle](https://www.kaggle.com/drakendan)")
    st.markdown("[Medium](https://medium.com/@dandupreez)")

with col2:
    st.markdown("# Data Analyst / Python Developer")
    content = """
    Write something about yourself
    """
    st.info(content)
