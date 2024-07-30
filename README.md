# pastehub

pastehub is a web application that allows users to create and share text snippets ("pastes") with an expiration time. Users can register, login, create pastes, and comment on existing pastes. The application is built using React.js for the frontend, Flask for the backend, PostgreSQL for the database, AWS S3 for file storage, and Redis for caching.

## Features

- **User Authentication:** Users can register and log in to the application.
- **Create Paste:** Users can create a new paste with an expiration time. Each paste generates a unique URL.
- **Comment on Pastes:** Users can comment on any paste.
- **View Pastes:** Users can view pastes and their associated comments.
- **Manage Pastes:** Logged-in users can view all their pastes.

## Tech Stack

- **Frontend:** React.js
- **Backend:** Flask
- **Database:** PostgreSQL
- **Storage:** AWS S3
- **Caching:** Redis

## Installation

### Prerequisites

- Python 3.11+
- Node.js
- PostgreSQL
- Redis
- AWS S3 account

### Backend Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/ranaashutosh2923/pastehub.git
   cd pastehub/flask_api
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the environment variables:**
   Create a `.env` file in the `flask_api` directory and add the following variables:
   ```env
   SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost:5432/pastehub
   JWT_SECRET_KEY=your_jwt_secret_key
   AWS_ACCESS_KEY_ID=your_aws_access_key_id
   AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
   AWS_REGION=your_aws_region
   AWS_BUCKET_NAME=your_aws_bucket_name
   ```

5. **Run the database and redis server**

6. **Run the backend server:**
   ```sh
   flask run
   ```

### Frontend Setup

1. **Install the dependencies:**
   ```sh
   npm install
   ```

2. **Start the frontend development server:**
   ```sh
   npm start
   ```

## Usage

1. **Register:** Create a new account by providing a username, email, and password.
2. **Login:** Log in with your credentials.
3. **Create a Paste:** Create a new paste with content and set an expiration time.
4. **View Paste:** View the paste and share the unique URL with others.
5. **Comment:** Add comments to any paste.
6. **My Pastes:** Logged-in users can view all their pastes.

## API Endpoints

### Authentication

- **Register:** `POST /register`
- **Login:** `POST /token`

### Paste Management

- **Create Paste:** `POST /create_paste` (JWT required)
- **Get Paste:** `GET /:url_hash`
- **Get My Pastes:** `GET /get_my_pastes` (JWT required)

### Comment Management

- **Create Comment:** `POST /create_comment` (JWT required)