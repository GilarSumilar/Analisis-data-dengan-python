import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Belajar analisis data')

with st.sidebar:

    st.text('Ini merupakan sidebar')

    values = st.slider(
        label='select a range values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values: values')


# Membuat coloumb
st.markdown('**Belajar Columns**')
col1, col2, col3 = st.columns([1, 2, 2])

with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")



st.empty()



# Membuat tab
st.markdown('**Belajar TAB**')
tab1, tab2, tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])

with tab1:
    st.header("Tab1")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with tab2:
    st.header("Tab1")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with tab3:
    st.header("Tab1")
    st.image("https://static.streamlit.io/examples/owl.jpg")


# Membuat cotainer
st.markdown("**Container**")

with st.container():
    st.write("Di dalam container")

    x = np.random.normal(15, 5, 20)

    fig, ax = plt.subplots()
    ax.hist(x=x, bins=15)
    st.pyplot(fig)

st.write("Di luar container")

# Exoander : Anda dapat menganggap elemen layout ini 
# sebagai sebuah container yang dapat diperluas atau diciutkan secara interaktif. 

st.markdown("**Expander**")
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig) 
 
with st.expander("Klik untuk lihat"):
    st.write(
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
        in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
        nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
        sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
    )
