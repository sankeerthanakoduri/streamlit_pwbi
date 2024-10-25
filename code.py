# Import necessary libraries
import streamlit as st 

# Basic info
st.text('{this is streamlit generated}')
st.title(':blue[PWBI_Dashboard]')
st.info('Displaying PWBI Dashboard in Streamlit')
st.subheader(':rainbow[new way of demonstrating your dashboards through Streamlit]')

# Create username & password along with `c_code` value
users_db = {
    'keeru': {'password': '123', 'c_code': '200001'},
    'rajeev': {'password': '456', 'c_code': '200003'},
    'veena': {'password': '789', 'c_code': '200005'},
    'krishna': {'password': '147', 'c_code': '200006'}
}

# Published Power BI URL (updated to include `filterPaneEnabled=false` to remove filters)
base_power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=2045ef36-426e-452c-bde9-fb7bd15ee1b1&autoAuth=true&ctid=1e3bab2c-ff49-4d6c-827a-5017e6fd859c&filterPaneEnabled=false"

# Function to authenticate users
def authenticate(username, password):
    if username in users_db and users_db[username]['password'] == password:
        return True, users_db[username]['c_code']
    return False, None

# Function to generate Power BI URL with filter based on `c_code`
def generate_power_bi_url(c_code):
    filter_url = f"&$filter=Item_mst/c_code eq '{c_code}'"
    return base_power_bi_url + filter_url

# User input fields for username and password
username = st.text_input('Username')
password = st.text_input('Password', type='password')

# Login button logic
if st.button('Login'):
    is_authenticated, user_c_code = authenticate(username, password)
    
    if is_authenticated:
        st.success(f"Welcome {username}, you have access to data for {user_c_code}")
        
        # Generate the Power BI URL with the user's `c_code` filter
        power_bi_filtered_url = generate_power_bi_url(user_c_code)
        
        # Embed the filtered Power BI report using an iframe without the filter pane
        st.markdown(f'''
            <iframe width="100%" height="800px" src="{power_bi_filtered_url}" frameborder="0" allowFullScreen="true"></iframe>
        ''', unsafe_allow_html=True)
    else:
        st.error('Invalid username or password')

# Logout button logic
if st.button('Logout'):
    st.write('Logged out')
