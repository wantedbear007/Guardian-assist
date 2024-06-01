
<body>
  <h1>FastAPI React PDF Processing App</h1>
  <p>This repository contains a web application designed to upload PDF files to AWS S3, process them using Google GenAI LLM, and allow users to ask questions related to the content of the PDF file. The application utilizes FastAPI for the backend, React for the frontend, and integrates with AWS S3, Google GenAI, PostgreSQL with Supabase, and PyPDF2 for PDF content extraction.</p>

  <h2>Architecture Overview</h2>

  <h3>Backend (FastAPI)</h3>
  <ul>
    <li><strong>Framework</strong>: FastAPI (Python)</li>
    <li><strong>Technologies</strong>:
      <ul>
        <li>PyPDF2: For reading the content of PDF files.</li>
        <li>PostgreSQL with Supabase: Database solution for storing pdf meta data.</li>
      </ul>
    </li>
    <li><strong>Endpoints</strong>:
      <ul>
        <li><code>/</code>: Endpoint to check health of the servers.</li>
        <li><code>/v1/upload/</code>: Endpoint for uploading PDF files to AWS S3.</li>
        <li><code>/v1/chat/</code>: Endpoint for users to ask questions related to the content of the processed PDF files.</li>
        <li><code>/docs/</code>: Endpoint to test the API using OpenAPI</li>
      </ul>
    </li>
  </ul>

  <h3>Frontend (React)</h3>
  <ul>
    <li><strong>Framework</strong>: React (TypeScript + vite)</li>
    <li><strong>Features</strong>:
      <ul>
        <li>File Upload: Allows users to select and upload PDF files to the backend.</li>
        <li>Chat Interface: Provides a user-friendly interface for users to ask questions related to the content of the PDF files.</li>
      </ul>
    </li>
  </ul>

  <h3>Dockerization</h3>
  <ul>
    <li><strong>Docker-Compose</strong>: Provides a Docker Compose file for running the entire backend.</li>
    <li><strong>Dockerfile</strong>: Defines Docker images for the backend services, making it easy to deploy and scale.</li>
  </ul>

  <h2>Setup Instructions</h2>

  <ol>
    <li><strong>Backend Setup</strong>:
      <ol>
        <li>Clone the repository.</li>
        <li>Navigate to the <code>backend</code> directory.</li>
        <li>Install dependencies: <code>pip install -r requirements.txt</code>.</li>
        <li>Start the FastAPI server: <code>uvicorn main:app --reload</code>. or run <code>python main.py</code></li>
      </ol>
    </li>
    <li><strong>Frontend Setup</strong>:
      <ol>
        <li>Navigate to the <code>frontend</code> directory.</li>
        <li>Install dependencies: <code>npm install or bun install or yarn install</code>.</li>
        <li>Start the React development server: <code>npm start or bun run dev or yarn dev</code>.</li>
      </ol>
    </li>
    <li><strong>Docker Deployment</strong>:
      <ol>
        <li>Ensure Docker and Docker Compose are installed.</li>
        <li>Navigate to the root directory of the repository.</li>
        <li>Run <code>docker-compose up --build</code> to build and start the Docker containers.</li>
      </ol>
    </li>
    <li><strong>Accessing the Application</strong>:
      <ol>
        <li>Open your web browser and navigate to <code>http://http://localhost:5173/</code> or look for port number in the terminal.</li>
        <li>You should see the frontend interface for uploading files and interacting with the chat.</li>
      </ol>
    </li>
  </ol>

  <h2>Contributing</h2>
  <p>Contributions are welcome! If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.</p>

</body>
</html>
