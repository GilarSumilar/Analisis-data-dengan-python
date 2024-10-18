import streamlit as st 
import datetime
import pandas as pd

number = st.number_input(label="Umur")
st.write('Umur: ', int(number), 'tahun')

date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

upload_file = st.file_uploader('Pilih file yg ingin di upload')

if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)


gambar = st.camera_input('Cekrek')
if gambar:
    st.image(gambar)


tombol = st.button('Ini tombol')
if tombol:
    st.write(tombol)


Value = st.slider(
    label = 'Tentukan',
    min_value=0, max_value=100, value=(0, 100))
st.write(Value)
    
