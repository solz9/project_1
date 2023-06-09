import streamlit as st
import cv2
import pandas as pd
import numpy as np
import face_recognition
from deta import Deta
from encoding import get_all_names, detabase, find_encode_list

hs = pd.read_excel('DS_10Ly4 - Copy.xlsx')
gv = pd.read_excel('passgv.xlsx')
hs = hs.drop(columns=['Họ và tên đệm', 'Tên'])
name = hs['Họ và tên'].values.tolist()
name = [name[i].lower() for i in range(len(name))]
hs['họ và tên'] = name

base = detabase()
regis_name = get_all_names()
encode_list = find_encode_list()

# def face_input_regis():
y = st.text_input('Nhập họ và tên').lower()
x = st.text_input("Nhập mật khẩu", type="password")
uploaded_file = st.camera_input("Lấy ảnh")
st.set_option('deprecation.showfileUploaderEncoding', False)
df1 = hs[hs['họ và tên'] == y]
if st.button('Enter'):
    identical = [i for i in range(len(regis_name)) if y == regis_name[i]]
    if df1['Password'].values != x:
        st.warning('Bạn đã nhập sai mật khẩu hoặc họ và tên, vui lòng nhập lại')
    elif len(identical) > 0:
        st.error('Gương mặt này đã được đăng ký')
    else:
        if uploaded_file:
            bytes_data = uploaded_file.getvalue()
            cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            faceframe = face_recognition.face_locations(cv2_img)
            if len(faceframe) > 0 and encode_list != None:                 
                img_encode = face_recognition.face_encodings(cv2_img, faceframe)[0]
                match_regis = face_recognition.compare_faces(encode_list, img_encode)
                match_index_regis = [i for i in range(len(match_regis)) if match_regis[i] == True]
                if len(match_index_regis) > 0:
                    base.put({'key':y, 'pic': img_encode.tolist()})
                    st.success('Đăng ký gương mặt thành công')
            elif len(faceframe) == 0:
                st.warning('Vui lòng chụp lại')
            else:
                img_encode = face_recognition.face_encodings(cv2_img, faceframe)[0]
                base.put({'key':y, 'pic': img_encode.tolist()})
                st.success('Đăng ký gương mặt thành công, bạn có thể hủy đăng ký gương mặt [tại đây](https://solz9-project-1-face-delete-tvwgbm.streamlit.app/)')
                
