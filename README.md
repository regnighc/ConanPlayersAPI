# ConanPlayersAPI

ConanPlayersAPI is a lightweight, efficient API wrapper designed to manage and retrieve Conan Exiles player lists. Built using Flask and containerized with Docker, this project offers a streamlined solution for integrating player data into your applications.

## Features
- **Lightweight & Fast:** Quickly fetch and manage player lists with minimal overhead.
- **Flask-Powered:** Leverage the simplicity and flexibility of Flask for rapid API development.
- **Dockerized:** Enjoy consistent deployment and easy scalability with Docker.

## API Endpoint
The primary endpoint for accessing player data follows this pattern:

/players/IPADDRESS/QUERYPORT

Replace `IPADDRESS` and `QUERYPORT` with the actual address and port of your server. This design allows you to target specific servers for their player lists.

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)

### Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/regnighc/ConanPlayersAPI.git
   cd ConanPlayersAPI
   
2. docker build -t conanplayersapi .

3. docker run -d -p 5000:5000 conanplayersapi

![image](https://github.com/user-attachments/assets/de186e32-3feb-4696-9c79-30984c263a4d)

