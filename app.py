from flask import Flask, render_template
app = Flask(__name__)
# Dummy Data for Conference
conference_info = {
    "name": "Google Cloud Tech Day 2026",
    "date": "October 15, 2026",
    "location": "Moscone Center, San Francisco, CA",
    "description": "Unlock the power of the cloud with a full day of deep dives into Google Cloud's latest innovations."
}
# 8 Talks + 1 Lunch Break
schedule = [
    {
        "id": 1,
        "time": "09:00 - 10:00",
        "title": "Keynote: The Future of Cloud AI",
        "category": ["AI", "Keynote"],
        "description": "Join Google Cloud leaders as they unveil the next generation of AI infrastructure and models.",
        "speakers": [
            {"first_name": "Sundar", "last_name": "Pichai", "linkedin": "https://www.linkedin.com/in/sundarpichai/"}
        ],
        "is_break": False
    },
    {
        "id": 2,
        "time": "10:00 - 10:45",
        "title": "Mastering Kubernetes on GKE",
        "category": ["Compute", "DevOps"],
        "description": "Learn best practices for scaling and securing your Kubernetes clusters on Google Kubernetes Engine.",
        "speakers": [
            {"first_name": "Kelsey", "last_name": "Hightower", "linkedin": "https://www.linkedin.com/in/kelseyhightower/"},
            {"first_name": "Tim", "last_name": "Hockin", "linkedin": "https://www.linkedin.com/in/thockin/"}
        ],
        "is_break": False
    },
    {
        "id": 3,
        "time": "10:45 - 11:30",
        "title": "BigQuery: Petabyte-Scale Analytics",
        "category": ["Data", "Analytics"],
        "description": "Dive deep into BigQuery architecture and learn how to optimize your queries for speed and cost.",
        "speakers": [
            {"first_name": "Jordan", "last_name": "Tigani", "linkedin": "https://www.linkedin.com/in/jordantigani/"}
        ],
        "is_break": False
    },
    {
        "id": 4,
        "time": "11:30 - 12:15",
        "title": "Serverless with Cloud Run",
        "category": ["Compute", "Serverless"],
        "description": "Build and deploy scalable containerized applications on a fully managed serverless platform.",
        "speakers": [
            {"first_name": "Steren", "last_name": "Giannini", "linkedin": "https://www.linkedin.com/in/steren/"}
        ],
        "is_break": False
    },
    {
        "id": 99,
        "time": "12:15 - 13:15",
        "title": "Lunch Break & Networking",
        "category": ["Break"],
        "description": "Enjoy a catered lunch and connect with fellow developers and cloud experts.",
        "speakers": [],
        "is_break": True
    },
    {
        "id": 5,
        "time": "13:15 - 14:00",
        "title": "Vertex AI: From Model to Production",
        "category": ["AI", "ML"],
        "description": "A practical guide to building, deploying, and managing ML models using Vertex AI pipelines.",
        "speakers": [
            {"first_name": "Cassie", "last_name": "Kozyrkov", "linkedin": "https://www.linkedin.com/in/kozyrkov/"}
        ],
        "is_break": False
    },
    {
        "id": 6,
        "time": "14:00 - 14:45",
        "title": "Modernizing Legacy Apps with Anthos",
        "category": ["Hybrid Cloud", "Modernization"],
        "description": "Strategies for modernizing monolithic applications and managing them across hybrid and multi-cloud environments.",
        "speakers": [
            {"first_name": "Priyanka", "last_name": "Vergadia", "linkedin": "https://www.linkedin.com/in/pvergadia/"},
            {"first_name": "Gaurav", "last_name": "Karas", "linkedin": "https://www.linkedin.com/in/gauravkaras/"} # Fictional
        ],
        "is_break": False
    },
    {
        "id": 7,
        "time": "14:45 - 15:30",
        "title": "Security in the Cloud: Zero Trust",
        "category": ["Security"],
        "description": "Implementing Zero Trust security model using BeyondCorp Enterprise and Cloud Identity.",
        "speakers": [
            {"first_name": "Maya", "last_name": "Kaptur", "linkedin": "https://www.linkedin.com/in/mayakaptur/"} # Fictional
        ],
        "is_break": False
    },
    {
        "id": 8,
        "time": "15:30 - 16:15",
        "title": "Building Global Apps with Cloud Spanner",
        "category": ["Database"],
        "description": "How to use Cloud Spanner for mission-critical, relational database workloads that require high availability.",
        "speakers": [
            {"first_name": "Delept", "last_name": "Shrivast", "linkedin": "https://www.linkedin.com/in/deleptshrivast/"} # Fictional
        ],
        "is_break": False
    }
]
@app.route('/')
def home():
    return render_template('index.html', conference=conference_info, schedule=schedule)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
