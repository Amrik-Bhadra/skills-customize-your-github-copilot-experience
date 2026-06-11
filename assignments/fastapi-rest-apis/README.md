# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, fast REST APIs using the FastAPI framework. You will create a complete API with multiple endpoints, request/response models, and error handling to understand how web services handle data and client requests.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application with basic GET and POST endpoints. Create endpoints that allow clients to create and retrieve data from an in-memory list.

#### Requirements
Completed program should:

- Initialize a FastAPI application
- Create a GET endpoint `/items` that returns all items
- Create a GET endpoint `/items/{item_id}` that retrieves a specific item by ID
- Create a POST endpoint `/items` that adds a new item to the list
- Return appropriate HTTP status codes (200, 201, 404)


### 🛠️ Add Request/Response Models

#### Description
Implement Pydantic models to validate request and response data. This ensures type safety and automatic API documentation.

#### Requirements
Completed program should:

- Define a Pydantic model for item data (e.g., name, description, price)
- Use the model for request validation in POST endpoints
- Use the model for response serialization
- Include field validation (required fields, string length, numeric ranges)
- Generate automatic API documentation at `/docs`


### 🛠️ Implement Error Handling and Status Codes

#### Description
Add proper error handling and HTTP status codes for various scenarios like not found, invalid input, and internal errors.

#### Requirements
Completed program should:

- Return 404 status when an item is not found
- Return 422 status for validation errors
- Implement custom error messages
- Use HTTPException for error handling
- Test all endpoints return appropriate status codes


### 🛠️ Add Query Parameters and Filtering (Stretch Goal)

#### Description
Extend the API to support filtering items by attributes using query parameters.

#### Requirements
Completed program should:

- Add optional query parameters to the GET `/items` endpoint (e.g., `?min_price=10&max_price=50`)
- Filter the items list based on query parameters
- Return filtered results with appropriate documentation
- Handle edge cases (invalid parameter values, no matches)
