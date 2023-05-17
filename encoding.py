import streamlit as st
from deta import Deta

def detabase():
    DETA_KEY = "c0qy5dgedq2_7aSU1pPYRdDoNvwmqdwwVUDZLUGz3mpU"
    deta = Deta(DETA_KEY) 
    return deta.Base("face_reg_project")


def get_all_names():
    data = detabase()
    items = data.fetch().items
    names = [item["key"] for item in items]
    if len(names) > 0:
        return names
    else:
        return []
    
# LIST CHỨA FACE_ENCODING CỦA NHỮNG GƯƠNG MẶT ĐÃ ĐĂNG KÝ
def find_encode_list():
    data = detabase()
    encode_list = []
    names = get_all_names()
    if len(names) > 0:
        for i in range(len(names)):
            name_and_encode = data.get(names[i])
            encode_list.append(name_and_encode['pic'])
            return encode_list
    else:
        return None