# Screening System

A Django-based screening system with gRPC support, Celery workers, and PostgreSQL database.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### 1. Development Setup

- Python 3.13
- Poetry:

```bash
# Install the dependencies
poetry install

# Activate the virtual environment
poetry shell
```

### 2. Start the Application

Run the following command to start all services:

```bash
docker compose up --build
```

This will start the following services:
- **PostgreSQL Database** (port 5432)
- **Redis** (port 6379)
- **Django Web Server** (port 8000)
- **gRPC Server** (port 50051)
- **Celery Worker** (background tasks)

### 3. Access the Application

Once all services are running, you can access:
- **Web Application**: http://localhost:8000
- **gRPC Server**: localhost:50051

## Services Overview

| Service | Description | Port | Health Check |
|---------|-------------|------|--------------|
| **web** | Django web server | 8000 | `/health/startup-probe/` |
| **grpc** | gRPC server | 50051 | - |
| **worker** | Celery background worker | - | `celery inspect ping` |
| **postgres** | PostgreSQL database | 5432 | `pg_isready` |
| **redis** | Redis cache/message broker | 6379 | - |

## Available Endpoints

### REST API Endpoints
- **Swagger**: `GET /api/v1/docs/`

- **Create Candidate**: `POST /api/v1/candidates/`

- **Retrieve Candidate**: `GET /api/v1/candidates/{id}`

- **Health Check**: `GET /health/startup-probe/`
  - Returns application health status
  - Used by Docker health checks

### gRPC Endpoints

The gRPC server provides the following services defined in `app/grpc/proto/candidate.proto`:

#### CandidateController Service

- **GetCandidateStatus**
  - **Request**: `CandidateIdRequest { id: string }`
  - **Response**: `Candidate { status: string, screening_log: ScreeningLog }`
  - **Description**: Retrieve candidate status and screening information

#### Message Types

- **Candidate**
  ```protobuf
  message Candidate {
      string status = 1;
      ScreeningLog screening_log = 2;
  }
  ```

- **ScreeningLog**
  ```protobuf
  message ScreeningLog {
      bool is_duplicate = 1;
      bool is_blacklisted = 2;
      bool is_email_format_valid = 3;
  }
  ```

- **CandidateIdRequest**
  ```protobuf
  message CandidateIdRequest {
      string id = 1;
  }
  ```

## Development Commands

### Stop Services
```bash
docker compose down
```

### View Logs
```bash
# All services
docker compose logs -f

# Specific service
docker compose logs -f web
docker compose logs -f grpc
docker compose logs -f worker
```

### Rebuild Services
```bash
docker compose up --build --force-recreate
```

### Database Management
```bash
# Run migrations
docker compose exec web python manage.py migrate

# Create superuser
docker compose exec web python manage.py createsuperuser

# Access Django shell
docker compose exec web python manage.py shell
```

### Monitor Celery Worker
```bash
# Check worker status
docker compose exec worker celery -A app inspect ping

# View active tasks
docker compose exec worker celery -A app inspect active
```

## Architecture

The system consists of:
- **Django Web Application**: Handles HTTP requests and admin interface
- **gRPC Server**: Provides high-performance API for candidate operations
- **Celery Workers**: Process background tasks asynchronously
- **PostgreSQL**: Primary database for persistent data
- **Redis**: Message broker for Celery and caching

## Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure ports 5432, 6379, 8000, and 50051 are available
2. **Database connection**: Wait for PostgreSQL health check to pass before accessing the application
3. **Environment variables**: Verify `.env` file is properly configured

### Check Service Health

```bash
# Check if all containers are running
docker compose ps

# Check specific service logs
docker compose logs [service_name]
```
