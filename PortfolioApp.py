import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import base64
import requests

# Function to load Lottie animations from a URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Main function to define the layout and content of the Streamlit app
def main():
    st.set_page_config(
        layout="wide",
        page_icon="🎓",
        page_title="Şeyda Nur Yılmaz - Portfolio"
    )

    # Load Lottie animations
    lottie_about_me = load_lottie_url("https://lottie.host/f497c30c-9c91-41d9-99fd-ccaa68652051/ZMY8cKf295.json")
    lottie_about_me_second = load_lottie_url("https://lottie.host/12a5674a-f605-4841-bdb0-b99eddb80e5f/0paH1NB1lA.json")
    lottie_projects = load_lottie_url("https://lottie.host/bf9f689a-85b1-497a-8de8-d83876100418/ZDGx6W2bI6.json")
    lottie_contact = load_lottie_url("https://lottie.host/c32ec37e-8c1c-4969-9deb-63cb7ea89350/03ncnNsz6g.json")
    
    # Custom CSS for Lottie Integration
    st.markdown("""
        <style>
            .lottie-container {
                width: 100%;
                height: 300px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Custom CSS
    st.markdown("""
        <style>
            h1 {
                color: orange;
                font-family: 'Arial', sans-serif;
                font-size: 38px;
            }
            h2 {
                color: orange;
                font-family: 'Arial', sans-serif;
                font-size: 32px;
            }
            h3 {
                color: #C49549;
                font-family: 'Arial', sans-serif;
                font-size: 26px;
            }
            h4 {
                color: #C49549;
                font-family: 'Arial', sans-serif;
                font-size: 24px;
            }
            p {
                color: #FFFFFF;
                font-family: 'Arial', sans-serif;
                font-size: 20px;
            }
            a {
                color: #2980B9;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                color: #FF5733;
                text-decoration: underline;
            }
            .divider {
                margin: 20px 0;
                height: 1px;
                background-color: #DDDDDD;
            }
            .container {
                padding: 20px;
                background-color: #1C2126;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .form-container {
                padding: 20px;
                background-color: #1C2126;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .form-container input, .form-container textarea {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #DDDDDD;
                border-radius: 5px;
                font-family: 'Arial', sans-serif;
            }
            .form-container button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-family: 'Arial', sans-serif;
                font-size: 16px;
            }
            .form-container button:hover {
                background-color: #45A049;
            }
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap='small', vertical_alignment='center')

    with col1:
        # Header Section
        st.markdown("""
            <h1>Greetings 👋</h1>
            <h2>Welcome to My Personal Portfolio</h2>
            """, 
        unsafe_allow_html=True)

        try:
            cv_file = "Seyda Nur Yilmaz, CV.pdf"  

            with open(cv_file, "rb") as cv:
                cv_data = cv.read()
            
            b64_cv = base64.b64encode(cv_data).decode()
            to_cv = f'<a href="data:application/octet-stream;base64,{b64_cv}" download="Seyda_Nur_Yilmaz_CV.pdf">Resume</a>'

        except:
            print("Resume cannot be found")

            to_cv = 'Resume is not available'

        st.markdown(f"""
            <div style='text-align: justify;'>
                <p> Hi, it is Şeyda Nur Yılmaz. I recently completed my bachelor's degree in Geophysical Engineering at Istanbul Technical University and am now embarking on a new chapter as an intern at K-UTEC Salt Technologies in Germany. 
                    My passion for geophysical sciences has driven me to gain hands-on experience in seismic, electrical, and magnetic surveying, as well as data processing and interpretation. In addition to my technical expertise, I've led the ITU Geophysical Engineering Club, organizing events and securing sponsorships. 
                    I am eager to further develop my skills and contribute to innovative projects in the field.</p>
            </div>
            <div style='text-align: justify;'>
                <p>
                <a href="https://www.linkedin.com/in/şeyda-nur-yılmaz-09b1b4240/">LinkedIn</a> |
                <a href="https://github.com/yilmazseyda">GitHub</a> | 
                {to_cv} 
                </p>
            </div>
            <div class="divider"></div>
        """, unsafe_allow_html=True)
    
    with col2:
        st_lottie(lottie_about_me, height=350)

    # Navigation Menu
    with st.container():
        selected = option_menu(
            menu_title=None,
            options=['About Me', 'Projects', 'Contact'],
            icons=['person', 'code-slash', 'chat-left-text-fill'],
            orientation='horizontal',
            styles={
                "container": {"padding": "0!important", "background-color": "#4C5258"},
                "icon": {"color": "orange", "font-size": "25px"}, 
                "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#838990"},
                "nav-link-selected": {"background-color": "#1C2126"},
            }
        )

    # About Section
    if selected == 'About Me':
        st.markdown("""
            <div class="container" style="text-align: center;">
                <h2>About Me</h2>
            </div>
            <br>
        """, unsafe_allow_html=True)

        cola, colb = st.columns(2, gap='small', vertical_alignment='center')

        with cola:
            st.markdown(f"""
                    <div class="container" style="width: 100%; height: 400px; max-width: 1500; min-width: 300px; margin: 0 auto;">
                        <div style="display: flex; gap: 30px;">
                            <div style="flex: 1;">
                                <h3 style="font-size: 22px; font-family: Arial, sans-serif; text-align: center;"><strong>Education</strong></h3>
                                <ul style="font-size: 18px; font-family: Arial, sans-serif;">
                                    <li><strong>Istanbul Technical University</strong>
                                        <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                            <li>Bachelor in Science, Geophysical Engineering</li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    <div class="divider"></div>
                    <div style="display: flex; gap: 20px;">
                        <div style="flex: 1;">
                            <h3 style="font-size: 22px; font-family: Arial, sans-serif; text-align: center;"><strong>Experience</strong></h3>
                            <ul style="font-size: 18px; font-family: Arial, sans-serif;">
                                <li><strong>K-UTEC Salt Technologies, Germany</strong>
                                    <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                        <li>Geophysical Engineering Intern (3 months)</li>
                                    </ul>
                                </li>
                                <li><strong>GEOPHYSIK GGD, Germany</strong>
                                    <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                        <li>Geophysical Engineering Intern (3 months)</li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </div>
                    </div>
                """, unsafe_allow_html=True)
        
        with colb:
            with st.container():
                st_lottie(lottie_about_me_second, height=450)


    # Projects Section
    if selected == 'Projects':
        st.markdown("""
            <div class="container" style="text-align: center;">
                <h2>Projects</h2>
            </div>
            <br>
        """, unsafe_allow_html=True)

        col3, col4 = st.columns(2, gap='small', vertical_alignment='center')
        
        with st.container(border=True):
            with col3:
                st_lottie(lottie_projects, height=350, key="Projects")

            with col4:
                graduation_file = "Graduation Project.pdf"
                
                try:
                    with open(graduation_file, "rb") as grad:
                        graduation_data = grad.read()

                    b64_grad = base64.b64encode(graduation_data).decode()
                    to_grad = f'<a href="data:application/octet-stream;base64,{b64_grad}" download="Graduation Project.pdf">Paper</a>'
                
                except:
                    print("Graduation Project cannot be found!")

                    to_grad = '<strong style="color: red;">Graduation Project is not available</strong>'

                st.markdown(f"""
                    <div class="container" style="text-align: justify;">
                        <div style="display: flex; gap: 40px;">
                            <div style="flex: 1; text-align: center;">
                                <ul style="font-size: 18px; font-family: Arial, sans-serif;">
                                    <li><strong style="font-size: 20px;">Investigation of Salt Domes in the Gulf of Mexico with Single Channel Seismic Reflection Data</strong>
                                        <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                            <li>Graduation Project | {to_grad}</li>
                                        </ul>
                                    </li>
                                    <li><strong style="font-size: 20px;">Application of Geophysical Methods, Processing, and Interpretation on an Old Coal Mine</strong>
                                        <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                            <li>Term Project</li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)


    # Contact Section
    if selected == 'Contact':
        st.markdown("""
            <div class="container" style="text-align: center;">
                <h2>Get in Touch with Me!</h2>
            </div>
            <br>
        """, unsafe_allow_html=True)
        col5, col6 = st.columns(2, gap='small', vertical_alignment='center')

        with col5:
            st.markdown("""
                <div class="container form-container">
                    <form action="https://formsubmit.co/yilmazseyd18@itu.edu.tr" method="POST">
                        <input type="text" name="name" placeholder="Your Name" required>
                        <input type="email" name="email" placeholder="Your Email" required>
                        <textarea name="message" placeholder="Your Message" required></textarea>
                        <div style="text-align: center;">
                            <button type="submit" style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
                                Send
                            </button>
                        </div>
                    </form>
                </div>
            """, unsafe_allow_html=True)


        with col6:
            st_lottie(lottie_contact, height=350)


if __name__ == '__main__':
    main()
