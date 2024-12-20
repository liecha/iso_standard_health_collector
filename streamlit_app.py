import streamlit as st
import pandas as pd
from datetime import date
from streamlit_avatar import avatar
import datetime

# DESIGN implement changes to the standard streamlit UI/UX
st.set_page_config(page_title="myHealth:COLLECTOR", page_icon="img/health_logo.png")
# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -4rem;}</style>''',
    unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-znku1x a {color: #9d03fc;}</style>''',
    unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-znku1x a {color: #9d03fc;}</style>''',
    unsafe_allow_html=True)  # lightmode
# Design change height of text input fields headers
st.markdown('''<style>.css-qrbaxs {min-height: 0.0rem;}</style>''',
    unsafe_allow_html=True)
# Design change spinner color to primary color
st.markdown('''<style>.stSpinner > div > div {border-top-color: #9d03fc;}</style>''',
    unsafe_allow_html=True)
# Design change min height of text input box
st.markdown('''<style>.css-15tx938{min-height: 0.0rem;}</style>''',
    unsafe_allow_html=True)
# Design hide top header line
hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# Design hide "made with streamlit" footer menu area
hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}</style>"""

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.markdown(hide_streamlit_footer, unsafe_allow_html=True)

def uploader(text, key_in):
    uploaded_files = st.file_uploader(
                        text, 
                        accept_multiple_files=True,
                        key=key_in #input_key + '_uploader'
                    )
    for uploaded_file in uploaded_files:
        uploaded_file.read()
    return uploaded_files

def calculate_age(date_of_birth):
    date_now = date.today()
    your_years = date_now.year - date_of_birth.year
    your_months = date_now.month - date_of_birth.month
    your_days = date_now.day - date_of_birth.day
    result_string = str(your_years) + ' years old'
    return result_string

def save_data():
    print(st.session_state.gender)
    print('this_value')

result = avatar(
    [
        {
            "url": "https://img.freepik.com/free-photo/androgynous-avatar-non-binary-queer-person_23-2151100175.jpg?t=st=1733571244~exp=1733574844~hmac=885ca26ec02e9b249ca805cfcb47204108aa21b08497f998bfda181ec918c754&w=1380",
            "size": 208,
            "title": "",
            "caption": "",
            "key": "avatar1",
        }])

st.write(
    """
    # Emelie Chandni

    Welcome to our _:blue[personal lifeAtlas space]_! This space gives you an overview of your health, medical records, perscriptions and history.
    Make sure to update your profile with as much information as possible to get the most out of your data collection.
    """
) 

tab1, tab2 = st.tabs(["Home", "Health Data Collector"])            
  
with tab1:
    st.warning(        """
        You have not listed any emergency contact.
        [Go to the emergency collector to fill this in](https://github.com/streamlit/streamlit/issues)
        """,
        icon="⚠️")
    st.info(
        """
        Missing data in your health collection.
        [Let's begin to collect your health data!](https://github.com/streamlit/streamlit/issues)
        """,
        icon="👾",
    )

    st.success(
        """
        Successfully [uploaded data](https://blog.streamlit.io/the-next-frontier-for-streamlit/) to you personal lifeAtlas space.
        """,
        icon="⭐️",
    )

with tab2:
    st.image('img/health_collctor.png')
    st.markdown('The following page aim to help you to create a _:blue[summary]_ of your _:blue[historical]_ and _:blue[current medical state]_.' 
                + 'Please start to answear the questions as best as you can. You could always come back later to complete or fill in answers.')
    st.write('\n')

    df_data = pd.read_csv('data/iso_standard_health_selection.csv')
    df_locations = pd.read_csv('data/worldcities.csv').sort_values(['city']).reset_index()
    index_location = int(df_locations[df_locations['city'] == 'Stockholm'].index[0])
    locations_list = df_locations['city'].values
    titles_list = df_data['title'].unique()
    gender_list = ['','Female', 'Male', 'Non-gender', 'Other']
    subtitles_list = df_data['subtitle'].unique()

    if 'gender' not in st.session_state:
        st.session_state.gender = ''

    for i in range(0, len(titles_list)):
        this_title = '\n' + titles_list[i] + ' \n'
        st.subheader(this_title)
        with st.expander("SECTION - " + subtitles_list[i], expanded=False):
            df_selection = df_data[df_data['title'] == titles_list[i]]
            if df_selection['title'].iloc[0] == 'Data Collection':
                    uploaded_files = st.file_uploader(
                        'Upload health related files that you wish to store in you _:blue[personal atlasLife storage]_', 
                        accept_multiple_files=True,
                        key=input_key + '_uploader'
                    )
                    for uploaded_file in uploaded_files:
                        uploaded_file.read()
                    collection_questions = df_selection['question_primary'].values
                    st.caption("_:blue[Example of data or documents]_ to upload")  
                    for k in range(0, len(collection_questions)):
                        st.caption(" --- " + collection_questions[k])   
                    st.button('Save', key=input_key + '_uploader_button', on_click=save_data)    
            else:
                for j in range(0, len(df_selection)):     
                    input_key = df_selection['variable_name'].iloc[j] + '_key'
                    this_variable = df_selection['variable_name'].iloc[j]
                    this_question = df_selection['question_primary'].iloc[j]
                    this_widget_type = df_selection['widget_type'].iloc[j]
                    if this_widget_type == 'text_input':
                        this_text = st.text_input(this_question, '', key=input_key)
                    if this_widget_type == 'selectbox':
                        if this_variable == 'gender':
                            st.session_state.gender = st.selectbox(this_question, gender_list, key='selector_gender')                            
                        if this_variable[0:5] == 'city_':
                            selected_city = st.selectbox(this_question, locations_list, index=index_location)
                            df_selected_city = df_locations[df_locations['city'] == selected_city] 
                            df_location = df_selected_city[["lat","lng"]].rename(columns={"lng": "lon"})
                            st.map(df_location)
                    if this_widget_type == 'date_input':
                        date_of_birth = st.date_input(this_question, value=None, min_value=datetime.datetime(1914, 1, 1))
                        if date_of_birth:
                            this_age = calculate_age(date_of_birth)
                            st.write("_:blue[Your are]_:", this_age)                        
                    if this_widget_type == 'uploader':
                        uploader(this_question, input_key +'_uploader')
                st.button('Save', key=input_key + '_button', on_click=save_data)  
            
