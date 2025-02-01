from flask import Flask, render_template

app = Flask(__name__)

# Data for the website
about_me = (
    "Hello, my name is Chenxi Wu, but you can call me Chen. I am currently studying an Integrated Master's in Computer Science (MEng) at The University of York."
    " I am a motivated individual who thrives in collaborative environments and possesses strong skills in communication and teamwork, which I have developed and refined through various extracurricular activities, work experience, as well as previous employment.<br><br>"
    "My technical background includes proficiency in programming languages such as Python, Java, and C, alongside experience in Data analysis and software development methodologies."
    " I am also passionate about User-Centric design and Agile principles, which help equip me to contribute effectively to delivering high-quality, customer-focused products.<br><br>"
    "As I approach graduation, I am actively seeking opportunities for a graduate role as a Product Owner or Product Manager. While I understand these roles can be challenging to secure immediately after graduation, I am also deeply interested in roles related to human experience in technology or data analysis as a starting point in my career.<br><br>"
    " But enough about the 'boring' stuff, here's a little more about me. Outside of my academic and professional life, I enjoy playing badminton, hitting the gym, and exploring new technologies."
    " I also love playing New York Times games and watching movies, with my favorite films being 'Fury' and the 'John Wick' series. I have a golden lab named Milo, and I thoroughly enjoy going on long walks with him. <br><br>"
    " I also have a passion for traveling and have visited many incredible destinations, including Turkey, Mallorca, China, and Berlin. These experiences have given me a deeper appreciation for diverse cultures and cuisines.<br><br>"
    " When it comes to food, sushi is my absolute favorite, although I have a love for all kinds of cuisine. I enjoy trying new dishes and exploring the culinary traditions of different cultures."
)

projects = [
    {
        "name": "3rd Year Individual Project", 
        "description": (
            "This project aimed to develop an innovative end-user tool designed to help academic writers maintain consistency between hierarchical arguments, linear outlines, and written text.<br><br>"
            "The tool integrated the creation of structured arguments, using methodologies such as Goal Structuring Notation (GSN), with detailed outlines and corresponding text. "
            "It provided functionality to ensure that changes made to any of these components were synchronized across the argument, outline, and text, enabling round-tripping of updates.<br><br>"
            "By designing intuitive user interfaces and implementing robust text and model manipulation techniques, the tool addressed the need for a cohesive workflow for academic writers. "
            "The project also included a research phase to identify the specific needs of academic users and evaluate the tool's effectiveness through user testing.<br><br>"
            "Fellow students carried out representative writing tasks with the tool and provided feedback on its usability and utility. "
            "This project demonstrated the practical benefits of the tool by using it to develop and refine its own argument, outline, and final report, showcasing its potential to enhance consistency and productivity in academic writing."
        )
    },
    {
        "name": "4th Year Group Project", 
        "description": (
            "This project focuses on enhancing the software development lifecycle by integrating AI-driven solutions into key phases, including development, validation, and testing.<br><br>"
            "The initiative includes the implementation of an AI-powered docstring generator, which automates the creation of comprehensive and standardized documentation for Python functions, fostering improved code clarity and developer collaboration.<br><br>"
            "Additionally, the project leverages AI to automate the generation of robust and efficient unit tests, streamlining the testing process and enhancing software reliability.<br><br>"
            "Furthermore, it incorporates AI-driven code improvement suggestions, enabling developers to optimize their code for performance, maintainability, and adherence to best practices.<br><br>"
            "By combining these intelligent tools, the project aims to deliver an innovative, seamless process that boosts productivity and software quality while addressing both functional and non-functional requirements. "
            "Ultimately, the project strives to empower software development teams with AI-enhanced workflows that maintain high standards of quality and collaboration."
        )
    }
]

module_results = {
    "Software 1: Foundations of Programming for Computer Science": "95%",
    "Engineering 1: Introduction to Software & Systems Engineering": "85%",
    "Data 1: Introduction to Data Science": "81%",
    "Human Factors: Technology in Context": "79%",
    "Systems & Devices 3: Advanced Computer Systems": "76%",
    "Software 3: Functional Programming with Applications": "73%",
    "Autonomous Robotic Systems Engineering": "73%",
    "Human-Computer Interaction 2: User Experience": "72%",
    "Systems & Devices 1: Introduction to Computer Architectures": "71%",
    "Human-Computer Interaction 1: Introduction to User Centred Design": "71%",
    "Qualitative Approaches to Investigating UX": "66%",
    "Theory 1: Mathematical Foundations of Computer Science": "65%",
    "Data 2: Data Analysis & Management": "65%",
    "Evolutionary & Adaptive Computing": "64%",
    "Software 2: Object Oriented Data Structures & Algorithms": "61%",
    "Theory 3: Computability & Complexity": "61%",
    "Intelligent Systems 2: Machine Learning & Optimisation": "61%",
    "Project: Computer Science": "52%",
    "Research Methods in Computer Science": "Pending",
    "Network Security": "Pending",
    "Quantum Computation": "Pending",
    "Player Experiences in Digital Games": "Pending",
    "Group Project (Integrated Masters)": "Pending"
}

social_media_links = {
    "LinkedIn": "https://www.linkedin.com/in/chenxi-wu-3a8b6b2b9/",
    "GitHub": "https://github.com/Chenxwu",
    "Instagram": "https://www.instagram.com/chenx1.w/",
    "Whatsapp": "https://wa.me/07960833328"
}

employment = [
    {
        "job_title": "Junior Software Developer",
        "company": "Glide UK",
        "duration": "July – September 2023",
        "description": (
            "Worked collaboratively with cross-functional teams to gather requirements, develop efficient code, and deliver robust solutions. Modernized legacy code by aligning it with current coding standards, enhancing the software development process and establishing a strong foundation for a career in technology."
        )
    },
    {
        "job_title": "Team Building Instructor",
        "company": "Wise Up",
        "duration": "June 2022 – September 2024 (Seasonal/Summer Work)",
        "description": (
            "Engaged with students of all age groups, facilitating team-building activities to foster teamwork, effective communication, and motivation. This experience significantly strengthened my public speaking abilities and developed my leadership skills."
        )
    },
    {
        "job_title": "Warehouse Operative",
        "company": "Hermes (Evri)",
        "duration": "June – September 2021",
        "description": (
            "Managed tasks on the warehouse floor, including sorting and scanning parcels and preparing damaged items for returns. This role enhanced my organizational abilities, communication skills, and attention to detail."
        )
    }
]

volunteering = [
    {
        "title": "Duke of Edinburgh Silver Award",
        "organization": "PDSA (Maidstone)",
        "year": "2018",
        "description": (
            "Participated in volunteering activities as part of the Duke of Edinburgh Silver Award program. "
            "Contributed to the work at PDSA in Maidstone, gaining valuable experience in teamwork, organization, and community service."
        )
    }
] 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about-me')
def about_me_page():
    return render_template('about_me.html', about_me=about_me)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/module-results')
def module_results_page():
    return render_template('module_results.html', module_results=module_results)

@app.route('/social-media-links')
def social_media_links_page():
    return render_template('social_media_links.html', social_media_links=social_media_links)

@app.route('/employment')
def employment_page():
    return render_template('employment.html', employment=employment, volunteering=volunteering)

if __name__ == '__main__':
    app.run(debug=True)
