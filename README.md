\# AI Chat Messaging Application – Proof of Concept (POC)



\## Project Overview

This Proof of Concept (POC) demonstrates a web-based AI Chat Messaging application built using Python (Flask), MongoDB Atlas, and the OpenAI API.



The system allows users to:

\- Send messages through a web interface

\- Receive AI-generated responses

\- Store chat conversations in MongoDB



The application architecture includes a Flask backend, a simple HTML/JavaScript frontend, and integration with an external AI API.



---



\## Technology Stack



Backend:

\- Python 3.11

\- Flask



Frontend:

\- HTML

\- JavaScript (Fetch API)



Database:

\- MongoDB Atlas (Cloud)



AI Integration:

\- OpenAI Chat Completion API



Environment:

\- Python Virtual Environment (venv)

\- dotenv for environment variable management



---



\## Application Flow



1\. User enters a message in the web interface.

2\. Frontend sends a POST request to the Flask backend.

3\. Backend forwards the message to the OpenAI API.

4\. AI response is received.

5\. Both user message and AI reply are stored in MongoDB.

6\. Response is returned to the frontend and displayed.



---



\## Setup Instructions (Local Execution)



1\. Clone the repository:

&nbsp;  git clone https://github.com/harsha-god420/ai-chat-messaging-poc.git



2\. Navigate to the project directory:

&nbsp;  cd ai-chat-messaging-poc



3\. Create virtual environment:

&nbsp;  python -m venv venv

&nbsp;  venv\\Scripts\\activate



4\. Install dependencies:

&nbsp;  pip install -r requirements.txt



5\. Create a `.env` file and add:

&nbsp;  OPENAI\_API\_KEY=your\_api\_key\_here

&nbsp;  MONGO\_URI=your\_mongodb\_connection\_string



6\. Run the application:

&nbsp;  python app.py



7\. Open browser and visit:

&nbsp;  http://127.0.0.1:5000



---



\## APIs Attempted



OpenAI Chat Completion API was integrated using the official Python SDK.



Model attempted:

\- gpt-4o-mini



Purpose:

\- To generate conversational AI responses dynamically.



---



\## Current Status



✔ Backend functioning successfully  

✔ MongoDB integration completed  

✔ Frontend chat interface operational  

✔ OpenAI API integration implemented  



⚠ Live AI responses require active OpenAI billing due to quota limitations.



---



\## Known Limitation



If OpenAI billing is not enabled, the application returns:

Error Code 429 – insufficient\_quota



This does not affect the backend or database functionality.



---



\## Future Enhancements



\- Improved UI/UX design

\- Enhanced error handling

\- Authentication system

\- Deployment configuration

\- Production-ready setup



---



\## Documentation



Detailed implementation report is available in:

AI\_Chat\_Messaging\_POC\_Report.pdf



---



Author:

Harsha

