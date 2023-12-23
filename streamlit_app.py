import streamlit as st

st.set_page_config(
    page_title='Sandbox',
    layout='wide',
    initial_sidebar_state='expanded'
)

def main():
    sidebar()
    body()
    pass

# Build sidebar for navigation
def sidebar():
    st.sidebar.header('Streamlit Sandbox')
    st.sidebar.markdown('## Portfolio')

# Main stage to display apps within
def body():
    st.header('Portfolio')
    st.text('This application will combine user requests & agile project status from multiple sources')


# Run Main
if __name__ == '__main__':
    main()