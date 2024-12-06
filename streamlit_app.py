import streamlit as st
import pandas as pd

# DESIGN implement changes to the standard streamlit UI/UX
st.set_page_config(page_title="myHealth:COLLECTOR", page_icon="img/rephraise_logo.png",)
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
st.markdown(hide_streamlit_footer, unsafe_allow_html=True)


def gen_mail_format(sender, recipient, style, email_contents):


    contents_str, contents_length = "", 0
    for topic in range(len(email_contents)):  # aggregate all contents into one
        contents_str = contents_str + f"\nContent{topic+1}: " + email_contents[topic]
        contents_length += len(email_contents[topic])  # calc total chars

    return 'some text'


def main_gpt3emailgen():

    st.image('img/health_collctor.png')  # TITLE and Creator information
    st.markdown('The following page aim to help you to create a _:blue[summary]_ of your _:blue[historical]_ and _:blue[current medical state]_.' 
                + 'Please start to answear the questions as best as you can. You could always come back later to complete or fill in answers.')
    st.write('\n')  # add spacing

    df_data = pd.read_csv('data/iso_standard_health_selection.csv')
    titles_list = df_data['title'].unique()
    subtitles_list = ['Personal Information Collector', 'Personal Data Collector']

    for i in range(0, len(titles_list)):
        this_title = '\n' + titles_list[i] + ' \n'
        st.subheader(this_title)
        with st.expander("SECTION - " + subtitles_list[i], expanded=True):
            df_selection = df_data[df_data['title'] == titles_list[i]]
            for j in range(0, len(df_selection)):
                input_key = df_selection['variable_name'].iloc[j] + '_key'
                print(input_key)
                this_question = df_selection['question_primary'].iloc[j]
                print(this_question)
                input_c1 = st.text_input(this_question, 'Type your answer here...', key=input_key)

if __name__ == '__main__':
    # call main function
    main_gpt3emailgen()
