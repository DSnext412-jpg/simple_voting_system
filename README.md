<div align="center">

# 🗳️ Simple Voting System

### A lightweight web-based voting application built with Flask & MySQL.

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

<br>

**Login → View Candidates → Vote → View Results**

</div>

---

## 📌 About

**Simple Voting System** is a beginner-friendly web application that
demonstrates how a voting workflow can be implemented using
**Python Flask and MySQL**.

Users can log in, view available candidates, cast a vote, and view
the current voting results.

The application also tracks whether a user has already voted to prevent
multiple votes from the same account.

---

## ✨ Features

- 🔐 User login
- 🚪 Logout functionality
- 👥 Candidate listing
- 🗳️ Vote casting
- 1️⃣ One vote per user
- 📊 Live voting results
- 🏆 Winner detection
- 🤝 Tie detection
- 🗄️ MySQL database integration
- 🔗 Foreign-key relationships
- 🎨 HTML/CSS based interface
- 🧩 Simple Flask architecture

---

## 🧠 How It Works

```text
                    ┌───────────────┐
                    │     USER      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │     LOGIN     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   CANDIDATES  │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  SELECT VOTE  │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    VOTE      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    RESULTS    │
                    └───────────────┘
