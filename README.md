# Django Note-Taking App API

This project is a simple note-taking application with a RESTful API built using Django REST Framework. It allows users to perform basic CRUD operations on notes, including sharing notes with other users and tracking version history.

Application also has feature for signup and login and also authentication and authorization functionality using JWT Token.

## Features

- User registration and login
- Create, update, and delete notes
- Share notes with other users
- View version history of a note

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [User Registration](#user-registration)
  - [User Login](#user-login)
  - [Create a New Note](#create-a-new-note)
  - [Get a Note](#get-a-note)
  - [Share a Note](#share-a-note)
  - [Update a Note](#update-a-note)
  - [Get Note Version History](#get-note-version-history)
- [Authentication](#authentication)

## Getting Started

### Prerequisites

- Python
- Django
- Django REST Framework

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/note-taking-api.git

2. Navigate to the project directory:


   ```bash
   cd note-taking-app

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

4. Run migrations:

   ```bash
   python manage.py migrate
5. Start the development server:

   ```bash
   python manage.py runserver
The API should now be accessible at http://localhost:8000/.

## API Endpoints
### User Registration
#### Endpoint: POST /signup
#### Sample Payload
      {
        "email": "user@example.com",
        "username": "user",
        "first_name": "John",
        "last_name": "Doe",
        "password": "securepassword123",
      }
#### Functionality:
Allows users to create an account by providing necessary information such as username, email, and password.
#### Output:
If the registration is successful, return a success message or status code. If there are validation errors or the username/email is already taken, return appropriate error messages or status codes.
### User Login
#### Endpoint: POST /login
#### Sample Payload
      {
        "email": "user@example.com",
        "password": "securepassword123"
      }
#### Functionality:
Allows users to log in to their account by providing their credentials (username/email and password).
#### Output:
If the login is successful, return an authentication token or a success message with the user details. If the credentials are invalid, return an error message or status code.

### Create a New Note
#### Endpoint: POST /notes/
#### Sample Payload
      {
        "content": "here is the content",
        "title": "here is title"
      }
#### Functionality: 
Create a new note. Only authenticated users can create a new note.
Note: The note owner needs to be stored in the database because notes are shareable.
Output: If the request is valid, return a success message with status code. If the request is invalid, return an error message or status code.
### Get a Note
#### Endpoint: GET /notes/{id}
#### Functionality:
GET a note by its ID. Only authenticated users. A note is viewable by its owner and the shared users only.
#### Output:
If the request is valid, return a success message with the note content. If the request is invalid, return an error message with status code.
### Share a Note
#### Endpoint: POST /notes/share
#### Sample Payload
      {
        "note_id": 1,
        "shared_with_users": [1, 2]
      }
#### Functionality:
Share a note with other users. You can parse multiple users in this request. Once the note admin executes this POST API, the users embedded in the request body will be able to view and edit the note.
Output: If the request is valid, return a success message with the appropriate status code. If the request is invalid, return an error message or status code.
### Update a Note
#### Endpoint: PATCH /notes/{id}
      {
        "content": "updated content",
        "title": "updated title"
      }
#### Functionality:
The note will be editable by admin, and all the shared users. All the users who have access to the note will be able to perform an edit anywhere on the note. For the sake of simplicity, let’s assume no existing sentences can be edited. But new sentences can be added in between existing lines of the note. All the updates to the notes need to be tracked with a timestamp and stored somewhere.
#### Output:
If the request is valid, return a success message with the appropriate status code. If the request is invalid, return an error message or status code.
### Get Note Version History
#### Endpoint: GET /notes/{id}/version-history/
#### Functionality:
Accessible by users having access only. GET the version history of the note. This includes all the changes made to the note since it has been created. The response will contain a list of timestamp, user who made the change, and the changes made to the note since its creation. If possible, you can track the line number of change as well.
#### Output:
If the request is valid, return the response with the appropriate status code. If the request is invalid, return an error message or status code

## Authentication
Authentication is required for creating, updating, and retrieving notes. Use the JWT token obtained after logging in to authenticate API requests. Include the access token in the Authorization header using the "Bearer" scheme.
