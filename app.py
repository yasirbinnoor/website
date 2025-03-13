import streamlit as st

# Set the title of the web app
st.title("Welcome to My Streamlit Web App")

# Add a header
st.header("An Attractive Streamlit Website")

# Add a subheader
st.subheader("This is a subheader")

# Add some text
st.text("This is a simple text")

# Add a markdown
st.markdown("### This is a markdown")

# Add an image
st.image("https://via.placeholder.com/800x400.png?text=Streamlit+Image", caption="Sample Image")

# Add a button
if st.button("Click Me"):
    st.write("Button clicked!")

# Add a selectbox
option = st.selectbox(
    "Select an option",
    ["Option 1", "Option 2", "Option 3"]
)
st.write("You selected:", option)

# Add a slider
slider_value = st.slider("Select a value", 0, 100, 50)
st.write("Slider value:", slider_value)

# Add a text input
text_input = st.text_input("Enter some text")
st.write("You entered:", text_input)

# Add a sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("This is a sidebar")

# Add a sidebar selectbox
sidebar_option = st.sidebar.selectbox(
    "Select an option in the sidebar",
    ["Sidebar Option 1", "Sidebar Option 2", "Sidebar Option 3"]
)
st.sidebar.write("You selected:", sidebar_option)

# Add a sidebar slider
sidebar_slider = st.sidebar.slider("Select a value in the sidebar", 0, 100, 25)
st.sidebar.write("Sidebar slider value:", sidebar_slider)