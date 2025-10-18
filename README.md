# HKMU Food ordering and tracking app


## Getting Started

Clone and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running Locally

Start the development server on http://0.0.0.0:5001

```bash
uvicorn app.main:app --reload --port 5001
```

## Workflow (recommended but not forced)

Currently there are 2 branches will trigger the deployment to vercel cloud accordingly.

- "main" branch will trigger the deployment to production environment.
- "dev" branch will trigger the deployment to development environment.

1. Create a new branch from dev branch for your feature or bug fix.
2. Make your changes and commit them with clear and concise messages.
3. Push your branch to the remote repository.
4. Create a pull request (PR) to merge your branch into the dev branch.
5. Test the changes in the dev environment.
6. If everything looks good, merge the dev branch into the main branch.
7. Deploy the main branch to production(automatically).

### API Docs

- Swagger UI: `http://localhost:5001/api/docs`
- ReDoc: `http://localhost:5001/api/redoc`
- OpenAPI JSON: `http://localhost:5001/api/openapi.json`