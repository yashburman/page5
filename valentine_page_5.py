# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 01:43:33 2024

@author: Sreejit
"""

import streamlit as st

# Page title
st.title("I couldn't come up with a nice title for this one :triumph:")

# Image and text side by side
col1, col2 = st.columns(2)

# Image on the left
image_path = "img5.jpeg"  # Replace with the actual path to your image
col1.image(image_path, use_column_width=True, caption="Our nose looks soo cute")

col2.write("""
This day was so intense and passionate, a celebration of our love where we embraced each other's desires. We did everything we wanted , touching, talking, cuddling, tying, and getting tied :smirk:.

We danced to your favorite songs, and you wore my T-shirt. You fit perfectly into my arms, like we were meant to be together. When I move my hand to the side of your face and kiss you, it just feels so right.

Your lips are all I want to taste, and your eyes are all I want to look at forever.

Love,

Your lover
""")

st.header("[Will you be mine and my...](https://mdg6rteskwzpdwrgtzzg87.streamlit.app/)")
