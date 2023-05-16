import streamlit as st
from login import hs_login, gv_login

st.title('KẾT QUẢ HỌC TẬP LỚP LÝ 4')
option = st.selectbox('Bạn là?', ('Học sinh', 'Giáo viên'))

if option == 'Giáo viên':
    gv_login()
else:
    hs_login()


    
