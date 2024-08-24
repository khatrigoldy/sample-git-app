import streamlit as st

st.title('Kid Molester')

col1,col2 = st.columns(2)
with col1:
    st.image('Faculty_of_mathematical_sciences,_University_of_Delhi.jpg')
    with col2:
        st.write(""""
        This site is used to created for killing of innocent children.
        """)

st.header('courses offer')
st.subheader('operational research')
st.subheader('stats')
st.subheader('mathematics')
st.subheader('cs')
st.subheader('mca')
st.subheader('data science')


st.sidebar.title('menu')
st.sidebar.markdown(""""
-home
-about
-contact
""")