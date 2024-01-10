import streamlit as st

# Title
st.set_page_config(
    page_title="PeiHsin (Amy) Wang - AI Product Manager, Data Scientist, and Data Engineer",
    page_icon=":potted_plant:",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

# Avatar and Name 
col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.image('hiking_avatar.jpeg')
with col2:
    st.markdown(
        """
    # PeiHsin (Amy) Wang 
    (She/Her)
                
    - Master student in Information System at [Univeristy of Washington Foster School of Business](https://foster.uw.edu/academics/degree-programs/master-of-science-in-information-systems/)
    - Product Manager & Business Analyst at [Airit](https://www.airiti.com/)
    """
    )

# About
st.markdown(
    """
    ## About

    👋 Hi, I'm all about innovation, problem-solving, and fostering teamwork to create impactful solutions that empower individuals. With 4+ years of experience in product management, I've gained expertise in the entire product life cycle, particularly in strategy, product design, and data planning.

    🚀 Driven by a growing desire to validate and bring ideas to life independently, I've ventured into the realms of data and AI engineering. My recent projects have revolved around data planning and developing LLM applications. To advance into this realm, I'm currently pursuing a second master's degree in Information Systems at the University of Washington Foster School, focusing on AI, data warehousing, and cloud technology.

    🧘‍♂️ When I'm not at my desk, you'll find me striking yoga poses or exploring the great outdoors on a hike. Let's not forget, adventures are best shared! So feel free to invite me if you're seeking partners to go bouldering, backpacking, or scuba diving! Who's up for the ride? Let's connect!

    """
)
    
# Education
st.markdown(
    """
    ## Education
    - MS, Information Systems, Univeristy of Washington Foster School of Business, 2024.06
    """
)

# Work Experience
    
# Projects
# st.markdown(
#     """
#     ## Projects
#     """
# )    
# col1, col2, col3 = st.columns(3)
# # Card with image and text
# for col in [col1, col2, col3]:
#     col.markdown(
#         """
#         <style>
#         .profile-img img {
#             width: 100%;
#             border-radius: 10%;
#         }
#         </style>

#         <div class="profile-img">

#         ![](https://avatars.githubusercontent.com/u/7678108?v=4)
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )    