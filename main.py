import streamlit as st


def main() -> None:
    """
    Entry point of the streamlit app.

    Sets the page configuration, displays the main title and
    introductory text, and instructs users to navigate using the sidebar.
    """
    st.set_page_config(page_title="Home", layout="wide", page_icon="Home")
    st.title("Welcome to the receipt reader app!")
    st.write("Use the sidebar to navigate between pages.")


if __name__ == "__main__":
    main()
