import pandas as pd
import streamlit as st


hs = pd.read_excel('DS_10Ly4 - Copy.xlsx')
gv = pd.read_excel('passgv.xlsx')
hs = hs.drop(columns=['Họ và tên đệm', 'Tên'])
name = hs['Họ và tên'].values.tolist()
name = [name[i].lower() for i in range(len(name))]
hs['họ và tên'] = name

def gv_login():
    x = st.text_input("Nhập mật khẩu", type="password")
    if st.button('Enter'):
        if gv['Password'].values != x:
            st.warning('Bạn đã nhập sai Password hoặc họ và tên, vui lòng nhập lại')
        else:
            df = hs.drop(columns=['họ và tên', 'Password'])
            hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
            st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
            st.table(df)

def hs_login():
    y = st.text_input('Nhập họ và tên').lower()
    x = st.text_input("Nhập mật khẩu", type="password")
    df1 = hs[hs['họ và tên'] == y]
    if st.button('Enter'):
        if df1['Password'].values != x:
            st.warning('Bạn đã nhập sai Password hoặc họ và tên, vui lòng nhập lại')
        else:
            df1 = hs[hs['họ và tên'] == y].drop(columns=['họ và tên', 'Password'])
            hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

                        # Inject CSS with Markdown
            st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

                        # Display an interactive table
            st.table(df1)