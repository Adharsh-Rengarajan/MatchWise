# MatchWise

**MatchWise** is an AI-driven job search platform that revolutionizes the traditional job-matching process. Unlike traditional keyword-based systems, MatchWise uses cutting-edge **Generative AI** and **Large Language Models (LLMs)** to intelligently match students and hiring managers based on comprehensive resume and job description analysis.

## Key Features

### For Candidates:
1. **Personalized Job Recommendations**  
   Candidates can add their job preferences and receive highly personalized content tailored to their interests and career goals.
   
2. **SWOT Analysis**  
   Get a detailed **SWOT (Strengths, Weaknesses, Opportunities, Threats)** analysis based on your profile and job preferences to help guide your career development.

3. **Profile Browsing**  
   Explore other candidates' profiles to see how you compare and learn from their experiences.

4. **Job Saving**  
   Save jobs you're interested in for easy access and future applications.

5. **Mock Tests**  
   Take mock tests relevant to the jobs you're interested in to assess your skills and readiness.

### For Recruiters:
6. **Candidate Profile Access**  
   Recruiters can view detailed candidate profiles to make informed hiring decisions.

7. **AI-Driven Candidate Matching**  
   Using Generative AI, recruiters receive a list of highly matched candidates based on both resume content and job requirements.

8. **Job Posting**  
   Recruiters can post job openings directly on the platform, ensuring they reach a qualified and engaged pool of candidates.

## Tech Stack

MatchWise is built using a modern tech stack to ensure scalability, security, and seamless user experience:

- **Frontend:** React  
- **Backend:** Flask  
- **Database:** MongoDB  

## Getting Started

### Prerequisites

To run the project locally, you'll need the following installed on your machine:

- Node.js (for the frontend)
- Python 3.x (for the backend)
- MongoDB (for database storage)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/matchwise.git
    ```

2. Install the frontend dependencies:
    ```bash
    cd matchwise/frontend
    npm install
    ```

3. Set up the backend:
    - Navigate to the backend folder:
    ```bash
    cd ../backend
    ```

    - Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up MongoDB and connect the database to the backend by updating the database credentials in the config file.

5. Start the development server:
    - For the frontend:
    ```bash
    npm start
    ```

    - For the backend:
    ```bash
    flask run
    ```

### Usage

Once the platform is running, you can:
- Sign up and create a candidate or recruiter profile.
- Begin adding job preferences and exploring relevant job listings.
- Candidates can start interacting with their profiles and taking mock tests.
- Recruiters can post job openings and view matched candidate profiles.
