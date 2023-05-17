import streamlit as st
import pandas as pd
from encoding import get_all_names, detabase

base = detabase()
hs = pd.read_excel('DS_10Ly4 - Copy.xlsx')
gv = pd.read_excel('passgv.xlsx')
hs = hs.drop(columns=['Họ và tên đệm', 'Tên'])
name = hs['Họ và tên'].values.tolist()
name = [name[i].lower() for i in range(len(name))]
hs['họ và tên'] = name
regis_name = get_all_names()
with st.form('Info'):
    y = st.text_input('Nhập họ và tên').lower()
    x = st.text_input("Nhập mật khẩu", type="password")
    button = st.form_submit_button('Enter')
    df1 = hs[hs['họ và tên'] == y]
    if button:
        if df1['Password'].values != x:
            st.warning('Bạn đã nhập sai mật khẩu hoặc họ và tên, vui lòng nhập lại')
        if y not in regis_name:
            st.warning('Bạn chưa đăng ký gương mặt, vui lòng đăng ký [tại đây](http://localhost:8506/)')
        else:
            base.delete(y)
            st.success('Hủy đăng ký gương mặt thành công, vui lòng đăng ký lại [tại đây](https://solz9-project-1-face-regis-1f193f.streamlit.app/)')
