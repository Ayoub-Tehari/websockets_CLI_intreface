Interactive Command Line Interface with Flask and SocketIO

This project provides a web-based interface for executing commands on the server and viewing the output interactively. It utilizes Flask for the web server and SocketIO for real-time communication between the client and server.
Features

    Execute commands on the server.
    View the command output in real-time.
    Supports both API and Web UI for command execution.

Tech Stack

    Flask: Python web framework.
    SocketIO: Enables real-time communication between web clients and servers.
    gevent: Enables asynchronous I/O for handling multiple connections efficiently.
    Flask-CORS: Enables Cross-Origin Resource Sharing (CORS) for API requests.

Project Structure

The project consists of the following files:

    app.py: Main Flask application file.
    exec_cmd.py: Module containing functions for executing commands.
    test.py: Example script demonstrating how to use exec_cmd.py from Python.
    index.html: Web interface for entering and running commands.

Running the Project

    Install dependencies:
    Bash

    pip install Flask gevent Flask-Cors flask-socketio

    Utilisez ce code avec précaution.

Run the application:
Bash

python app.py

Utilisez ce code avec précaution.

    This will start the server on port 5000 by default.

Usage

Web Interface:

    Open http://localhost:5000 in your web browser.
    Enter a command in the text field.
    Click the "Exécuter" (Run) button.
    The command output will be displayed in the "output" section.

API:

    Send a POST request to http://localhost:5000/api/exec with a JSON body containing the command field.
    The response will be a JSON object containing the standard output and error output of the program.
