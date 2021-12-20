import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

st.title("hello")
st.header("header")
st.subheader("subheader")
st.text("like, share, sub")
st.markdown(""" #h1tag ##h2tag ###h3tag :moon: :sunglasses: _Capriola_ **_capriola_**""",True)

data=pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

st.graphviz_chart(""" diagraph{
    watch-> like
    like->share
    share->watch
    share->watch}""")

st.pyplot()
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)