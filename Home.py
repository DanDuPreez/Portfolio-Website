import streamlit as st

st.set_page_config(layout='wide')

st.markdown("# Home")
st.sidebar.markdown("# Home")

col1, col2 = st.columns(2)

with col1:
    st.image('images/Profile Pic.png', width=300)

with col2:
    st.title('Daniel du Preez')
    content = '''
    Write something about yourself
    '''
    st.info(content)
