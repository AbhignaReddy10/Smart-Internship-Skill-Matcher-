import streamlit as s
s.set_page_config(page_title="SMART INTERNSHIP MATCHER")

#css
s.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #262730;
        color: white;
    }
    .stSelectbox>div>div {
        background-color: #262730;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(90deg, #7C3AED, #9333EA);
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
    }
    .stProgress > div > div > div > div {
        background-color: #7C3AED;
    }
    </style>
""", unsafe_allow_html=True)


s.title("Smart Internship-Skill Matcher")
s.write("Match your skills with internship roles and find the skill gaps")

#we now define roles and skills available
roles= {
    "Backend Developer":["python","sql","git","data structures"],
    "ML intern":["python","numpy","pandas","machine learning"],
    "Web Developer":["html","css","javascript","git"]
     }

selected_role=s.selectbox("Select role",list(roles.keys()))
user_input=s.text_input("Enter your skills seperated by commas")

if s.button("Check Match"):
    if not user_input.strip():
        s.error("Enter atleast one skill")
    else:    
        internship_skills= [skill.lower() for skill in roles[selected_role]]
        cleaned_skills=[skill.strip().lower() for skill in user_input.split(",")]

        matched_skills=[]
        missing_skills=[]


        for skill in internship_skills:
            if skill in cleaned_skills:
                
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        match_percentage=(len(matched_skills)/len(internship_skills))*100

        s.subheader("Match Results")
        s.progress(int(match_percentage))
    
        s.metric("Match Score", f"{match_percentage:.1f}%")

    
        
        
        s.write("###Matched Skills")
        if matched_skills:
            for skill in matched_skills:
                    s.write("-",skill)
        else:
            s.write("No matching skills found.")

        s.write("###Missing Skills")
        if missing_skills:
            for skill in missing_skills:
                s.write("-",skill)
        else:
            s.balloons()
            s.success("Perfect Match!")        

    
    