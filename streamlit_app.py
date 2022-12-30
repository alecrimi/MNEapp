import streamlit as st
import dipy as dipy
import dipy.io as dipy_io

# Display a file upload widget
trk_file = st.file_uploader("Upload a TRK file")

# Load the TRK file using DiPy
if trk_file is not None:
    trk, hdr = dipy_io.read_trk(trk_file)
    st.write("TRK file successfully loaded!")

    # Display the TRK file using the Streamlit 3D scatterplot widget
    st.pyplot(dipy.viz.window.show(trk, title='TRK file', size=(600, 600)))
else:
    st.write("No TRK file selected")
