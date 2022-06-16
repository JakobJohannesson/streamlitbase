import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Run to start environment
# source ~/desktop/streamlit_app/env/bin/activate

"# Streamlit Deployments are the best"




arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

# This outputs the figure

st.pyplot(fig)