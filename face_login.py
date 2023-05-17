import streamlit as st
import numpy as np
from deta import Deta
import cv2
import pandas as pd
import face_recognition
from encoding import get_all_names, find_encode_list, detabase

hs = pd.read_excel('DS_10Ly4 - Copy.xlsx')
gv = pd.read_excel('passgv.xlsx')
hs = hs.drop(columns=['Họ và tên đệm', 'Tên'])
name = hs['Họ và tên'].values.tolist()
name = [name[i].lower() for i in range(len(name))]
hs['họ và tên'] = name

# KẾT NỐI VỚI DATABASE'
base = detabase()

# TẠO RA LIST CHỨA NAME NHỮNG AI ĐÃ ĐĂNG KÝ GƯƠNG MẶT
names = get_all_names()
encode_list = find_encode_list()
# TÌM RA TÊN GƯƠNG MẶT MATCH VỚI INPUT 
def face_match(face_input_encode):
    if encode_list is not None:
        match = face_recognition.compare_faces(encode_list, face_input_encode)
        match_index = [i for i in range(len(match)) if match[i] == True]
        if match_index is not None: 
            return names[match_index[0]]
        else:
            return None
    else:
        return None
uploaded_file = st.camera_input("Chụp ảnh")
st.set_option('deprecation.showfileUploaderEncoding', False)
button = st.button("Submit")
if button:
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        input_face_frame = face_recognition.face_locations(cv2_img)
        if len(input_face_frame) < 1:
            st.warning("Vui lòng chụp lại ảnh hoặc [đăng nhập bằng mật khẩu](https://solz9-project-1-password-login-x3pltx.streamlit.app/)")
        else:
            input_face_encode = face_recognition.face_encodings(cv2_img, input_face_frame)[0]
            input_name = face_match(input_face_encode)
            if input_name is not None:
                df1 = hs[hs['họ và tên'] == input_name].drop(columns=['họ và tên', 'Password'])
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
            else:
                st.warning("Vui lòng chụp lại ảnh hoặc nếu chưa đăng ký gương mặt, vui lòng đăng ký [tại đây](https://solz9-project-1-face-regis-1f193f.streamlit.app/) hoặc [đăng nhập bằng mật khẩu](https://solz9-project-1-password-login-x3pltx.streamlit.app/)")
        





