import os
import streamlit as st

video_path = r"D:\Smart-Traffic-Management-System-main\images\rush.mp4"

st.write(f"Trying to load video from: {video_path}")
st.write(f"File exists: {os.path.exists(video_path)}")

if os.path.exists(video_path):
    st.video(video_path)
else:
    st.error("Video file not found! Check the path.")
