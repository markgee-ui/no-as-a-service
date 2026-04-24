#  NaaS: No as a Service

> "Delivering high-performance rejections with 99.9% uptime. Because your time is valuable, and their request isn't."

NaaS is a full-stack application designed to automate the process of saying "No." Built with a **FastAPI** backend and a **React** frontend, it provides a variety of ways to decline requests, from a standard "No" to a randomized "Hard pass."

---

## Prerequisites

Before you begin, ensure you have the following installed:
* **Python 3.8+**
* **Node.js (v14 or higher)**
* **npm** (comes with Node.js)

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/naas-project.git
cd naas-project
```

### 2. Backend Setup (FastAPI)
1. **Navigate to the backend directory:**
   ```bash
   # (If your main.py is in the root, stay here)
   ```
2. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```
3. **Start the server:**
   ```bash
   python -m uvicorn main:app --reload
   ```
   The backend will be running at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

### 3. Frontend Setup (React)
1. **Open a new terminal window** and navigate to the UI folder:
   ```bash
   cd naas-ui
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Start the React development server:**
   ```bash
   npm start
   ```
   The UI will open automatically at **http://localhost:3000**.

---

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/no` | Returns a simple "No". |
| `GET` | `/maybe` | Returns a "Maybe" that is actually a "No". |
| `GET` | `/random` | Returns a random rejection from our curated list. |

---

## Troubleshooting

**"Even the API said no to working right now"**
If you see this message in the UI:
1. Ensure the Python backend is running on port 8000.
2. Check that you have enabled **CORS** in `main.py`.
3. If using a browser like Chrome, try a "Hard Refresh" (`Ctrl + F5`).

---

## License
This project is licensed under the **"I'm Not Doing It"** License - which is basically MIT, but with more attitude.

---
