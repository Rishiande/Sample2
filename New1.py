import streamlit as st
st.header('HAPPY TEACHERS DAY')
a=st.number_input('ENTER ANY VALUE')
if st.button('HIT  ME'):
  st.success(f'YOUR LUCKY NMBER IS {a}')
 
