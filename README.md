# Flask DevOps Pipeline

> A production-style Flask app containerized with Docker and automatically deployed to AWS EC2 via GitHub Actions CI/CD pipeline.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white)

---

## Architecture

Developer pushes code → GitHub Actions triggers → SSH into EC2 → Pull latest image → Restart Docker container → Live at EC2 public IP

---

## Tech Stack

| Layer | Technology |
|---|---|
| App | Python + Flask |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud | AWS EC2 (Free Tier) |
| Reverse Proxy | Nginx |
| Monitoring | AWS CloudWatch |

---

## Features

- Flask app with `/` and `/health` endpoints
- Fully containerized with Docker
- Auto-deploy on every `git push` via GitHub Actions
- Nginx reverse proxy (port 80 → 5000)
- CloudWatch monitoring + CPU alerts

---

## Project Structure

```
flask-devops-pipeline/
├── app.py                        # Flask application
├── Dockerfile                    # Container configuration
├── requirements.txt              # Python dependencies
├── .github/workflows/deploy.yml  # CI/CD pipeline
└── devops-commands-reference.md  # Quick reference cheatsheet
```

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/sneha020902/flask-devops-pipeline.git
cd flask-devops-pipeline

# Build and run with Docker
docker build -t flask-devops .
docker run -p 5000:5000 flask-devops

# Visit http://localhost:5000
```

---

## Author

**Sneha Agrawal** — M.Sc. Computer Science @ Bauhaus-Universität Weimar
🔗 [LinkedIn](https://www.linkedin.com/in/-snehaagrawal/) · [GitHub](https://github.com/sneha020902) · [Portfolio](https://sneha020902.github.io)
