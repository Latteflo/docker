from fastapi import FastAPI

app = FastAPI()

# Define a list to store study resources
study_resources = []


@app.get("/")
def read_root():
    return {"Hello": "Latte! You are awesome! 🚀"}


@app.get("/items")
def get_resources():
    return study_resources


@app.post("/items")
def create_resource(resource: str):
    study_resources.append(resource)
    return {"message": "Resource created successfully"}


@app.delete("/items/{item_id}")
def delete_resource(item_id: int):
    if item_id < len(study_resources):
        study_resources.pop(item_id)
        return {"message": "Resource deleted successfully"}
    else:
        return {"message": "Resource not found"}


# Create some initial items
study_resources.append("Docker")
study_resources.append("Kubernetes")
study_resources.append("Python")
