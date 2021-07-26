import json
import streamlit as st

data = json.load(open("templates.json", "r"))

if 'product_number' not in st.session_state:
    st.session_state.product_number = 0

if "annotations" not in st.session_state:
    st.session_state.annotations = {}

# Previous and next buttons
prev, next = st.beta_columns(2)

# Modify the product_number status when next button is clicked
if next.button("Next"):

    if (st.session_state.product_number + 1) >= len(data):
        st.session_state.product_number = 0
    else:
        st.session_state.product_number += 1

# Modify the product_number status when previous button is clicked
if prev.button("Previous"):

    if (st.session_state.product_number - 1) < 0:
        st.session_state.product_number = len(data) - 1
    else:
        st.session_state.product_number -= 1

template = data[st.session_state.product_number]
template_area, submit = st.beta_columns([10,3])

ta = template_area.text_area("Template", value = template)

if submit.button("Submit"):
    st.session_state.annotations[st.session_state.product_number] = ta

st.write(st.session_state.annotations)

if st.button("Dump"):
    json.dump(st.session_state.annotations, open("modified_templates.json", "w"))