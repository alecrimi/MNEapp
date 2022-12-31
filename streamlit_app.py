import streamlit as st
import dipy as dipy
import os
from dipy.io.streamline import load_tractogram, save_tractogram,load_trk
#import nibabel as nib
from dipy.viz import window, actor, has_fury, colormap
'''
# Display a file upload widget
upload = st.file_uploader("Upload a TRK file", type=['trk'])


# Cache the uploaded file
def get_uploaded_image():
  if upload is not None:
        st.write(upload.name)
        
        # Create a directory and save the image file before proceeding. 
        file_path = os.path.join("data/", upload.name)
        with open(file_path, "wb") as user_file:
            user_file.write(upload.getbuffer())

        return file_path # fixed indentation

user_trk = get_uploaded_image()
'''
'''
# Load the TRK file using DiPy
user_trk= 'CST_L.trk' #'https://github.com/alecrimi/MNEapp/blob/main/CST.trk' #?raw=true

if user_trk is not None:
    trk = load_tractogram(user_trk, 'same') # load_tractogram(user_trk, 'same' ) #trk, hdr = dipy.io.streamline.load_trk(trk_file)
    #trk = nib.streamlines.load(user_trk)
    st.write("TRK file successfully loaded!")

    # Display the TRK file using the Streamlit 3D scatterplot widget
    # Prepare the display objects.
    color = colormap.line_colors(trk)

    streamlines_actor = actor.line(trk, color)

    # Create the 3D display.
    scene = window.Scene()
    scene.add(streamlines_actor)
    
    #st.pyplot(dipy.viz.window.show(trk, title='TRK file', size=(600, 600)))
    st.pyplot(window.show(scene))
else:
    st.write("No TRK file selected")
'''
import streamlit as st
import pyvista as pv

# Load the PyVista object
obj = pv.read('Brain.obj')

# Add the object to the Streamlit app, allowing rotation
st.pyvista_mesh(obj, rotate=True)
