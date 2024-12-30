"""
This is a simple FastAPI application that returns a JSON response with a greeting message.

To run this application locally, use the following command:
    uvicorn src.main:app --reload

To deploy this application, follow these steps:
1. Ensure you have Docker installed on your machine.
2. Create a Dockerfile with the following content:
    ```
    FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

    COPY ./src /app

    WORKDIR /app

    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
    ```
3. Build the Docker image:
    docker build -t my-fastapi-app .
4. Run the Docker container:
    docker run -d --name my-fastapi-container -p 80:80 my-fastapi-app
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
