import pickle
import streamlit as st
import pandas as pd
import numpy as np
st.title('KẾT QUẢ HỌC TẬP LỚP LÝ 4')
y = st.text_input('Nhập họ và tên (Lưu ý: ghi hoa chữ cái đầu)')
x = st.number_input('Nhập Password')
if st.button('Enter'):
    df = pd.read_excel('DS_10Ly4 - Copy.xlsx')
    df1 = df[df['Họ và tên'] == y]
    if df1['Password'].values != x:
        st.warning('Bạn đã nhập sai Password hoặc họ và tên, vui lòng nhập lại')
    else:
        if df[df['Họ và tên'] == 'Nguyễn Lục Hoàng Minh']:
            df2 = pd.DataFrame(
                {
                    "Họ và tên": df['Họ và tên'],
                    "HS1": df['HS1'],
                    'BT01 Đúng/Sai': df['BT01 Đúng/Sai'],
                    'BT02 Moment': df['BT02 Moment'],
                    'Điểm cộng': df['Điểm cộng'],
                    'Điểm KTGK': df['Điểm KTGK'],
                    'Điểm KTCK': df['Điểm KTCK'],
                    'Điểm KTTX': df['KTTX']
                }
            )
            hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
            st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
            st.table(df2)
        else:
            df1 = pd.DataFrame(
                {
                    "Họ và tên": df1['Họ và tên'],
                    "HS1": df1['HS1'],
                    'BT01 Đúng/Sai': df1['BT01 Đúng/Sai'],
                    'BT02 Moment': df1['BT02 Moment'],
                    'Điểm cộng': df1['Điểm cộng'],
                    'Điểm KTGK': df1['Điểm KTGK'],
                    'Điểm KTCK': df1['Điểm KTCK'],
                    'Điểm KTTX': df1['KTTX']
                }
            )
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
if df1['Password'].values != x:
        st.warning('Bạn đã nhập sai Password hoặc họ và tên, vui lòng nhập lại')
    else:
        df1 = pd.DataFrame(
            {
                "Họ và tên": df1['Họ và tên'],
                "HS1": df1['HS1'],
                'BT01 Đúng/Sai': df1['BT01 Đúng/Sai'],
                'BT02 Moment': df1['BT02 Moment'],
                'Điểm cộng': df1['Điểm cộng'],
                'Điểm KTGK': df1['Điểm KTGK'],
                'Điểm KTCK': df1['Điểm KTCK'],
            }
        )
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
