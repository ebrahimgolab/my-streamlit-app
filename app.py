import streamlit as st
import pandas as pd
import numpy as np

st.title("سلام دنیا 👋 (اولین اپ Streamlit)")

df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["ستون A", "ستون B"]
)

st.line_chart(df)

name = st.text_input("اسمت چیه؟")
if name:
    st.success(f"خوش اومدی {name}!")
