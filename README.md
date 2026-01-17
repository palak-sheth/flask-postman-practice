# Flask REST API Project

This project implements a Flask-based REST API with token authentication, structured logging, request IDs, and three functional endpoints (`/chat`, `/summarize`, `/extract`). The project is tested using Postman with collections and environments.

---

## **1. Features**

- REST endpoints using Flask
- JSON input + JSON output
- Bearer Token authentication
- Environment variables via `.env`
- Structured JSON logging
- Request IDs for traceability
- Error handling with JSON responses
- Tested using Postman Collections & Environments

---

## **2. Endpoints Overview**

| Endpoint     | Method | Description       |
|-------------|--------|-------------------|
| `/chat`     | POST   | Returns a reply   |
| `/summarize`| POST   | Summarizes text   |
| `/extract`  | POST   | Extracts keywords |

---

## **3. Endpoint Usage**

---

### ✓ **POST `/chat`**

**Request Body**
```json
{
  "message": "Hello Flask!"
}
```

**Response**
```json
{
  "reply": "You said: Hello Flask!"
}
```

---

### ✓ **POST `/summarize`**

**Request Body**
```json
{
  "text": "This is a long text that needs summarization."
}
```

**Response**
```json
{
  "summary": "This is a long text that needs summar..."
}
```

---

### ✓ **POST `/extract`**

**Request Body**
```json
{
  "text": "Flask logging internship development tokens"
}
```

**Response**
```json
{
  "keywords": ["logging", "internship", "development", "tokens"]
}
```

---

## **4. Authentication (Bearer Token)**

All endpoints require a token.

Example header:
```
Authorization: Bearer SECRET123
```

Token value is loaded from `.env` file.

---

## **5. Environment Setup**

### **Step 1: Install Dependencies**
```
pip install -r requirements.txt
```

### **Step 2: Create `.env` File**
```
API_TOKEN=SECRET123
```

### **Step 3: Run the Server**
```
python app.py
```

Default server URL:
```
http://127.0.0.1:5000
```

---

## **6. Project Structure**

```
project/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## **7. Logging**

Logs are formatted in structured JSON format for easy parsing.

**Example Log**
```json
{
  "event": "chat_request_received",
  "request_id": "9c94a7b3-8a1b-41b7-90f0-b9c214e9f1c6",
  "payload": {"message": "Hello Flask!"}
}
```

---

## **8. Error Handling**

Example responses:

**Unauthorized (401)**
```json
{"error": "Unauthorized"}
```

**Internal Server Error (500)**
```json
{"error": "Internal Server Error"}
```

---

## **9. Postman Testing**

This project includes:

✔ Postman Collection  
✔ Postman Environment  

Testing steps:

1. Open Postman
2. Import collection
3. Import environment
4. Set token in environment
5. Send requests
6. Verify JSON responses
7. Check terminal logs

---

## **10. Deliverables Checklist**

✔ Flask app running locally  
✔ `/chat` `/summarize` `/extract` endpoints  
✔ JSON Request / Response  
✔ Token Authentication  
✔ Request IDs for traceability  
✔ Structured Logs  
✔ Postman Collection  
✔ Postman Environment  
✔ README.md Completed  

---

## **11. Technologies Used**

- Python 3
- Flask
- Dotenv
- Postman

---

## **12. Status**

- Project completed successfully
