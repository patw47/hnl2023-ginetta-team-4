
import streamlit as st

st.set_page_config(page_title="Home", page_icon="")



#st.markdown("# Home")
st.title('Hi, I am Laur')  
st.write("As an expert in Swiss law, I have comprehensive knowledge of variuos Swiss legal codes, statutes, and case laws. Feel free to ask me any legal questions, and I will provide detailed answers.")
	

# Change the title of the sidebar
st.sidebar.title("")


with st.sidebar: 
    

    # Centered plus button in the middle of the sidebar
    if st.button("New chat", key="new_chat", help="Click to open a new window"):
        # Create an empty container
        popup_container = st.empty()

        # Content to display in the pop-up container
        popup_container.subheader("You clicked the plus button!")
        popup_container.write("This is a pop-up-like container.")










prompt = st.chat_input("Ask your question")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    st.write(f"User has sent the following prompt: {prompt}")
