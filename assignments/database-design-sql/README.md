# 📘 Assignment: Database Design & SQL

## 🎯 Objective

Master relational database design and SQL query fundamentals. You will design database schemas, write SQL queries to create, read, update, and delete data, and understand how to structure data for efficient retrieval and storage.

## 📝 Tasks

### 🛠️ Design a Relational Database Schema

#### Description
Create a database schema for a library management system. Plan tables for books, authors, and borrowers, then implement the schema using SQL CREATE TABLE statements with appropriate data types, constraints, and relationships.

#### Requirements
Completed program should:

- Design at least 3 related tables (books, authors, borrowers)
- Define primary keys and foreign key relationships
- Include appropriate data types (VARCHAR, INT, DATE, BOOLEAN)
- Add constraints (NOT NULL, UNIQUE, CHECK) where appropriate
- Write SQL CREATE TABLE statements to build the schema


### 🛠️ Write CRUD Operations

#### Description
Implement SQL queries to Create, Read, Update, and Delete records in the library database. Write queries that add new books, retrieve book information, update borrower records, and remove records.

#### Requirements
Completed program should:

- Write INSERT statements to add books, authors, and borrowers
- Write SELECT queries with WHERE clauses to find specific records
- Write UPDATE statements to modify existing records
- Write DELETE statements to remove records
- Handle edge cases (duplicate entries, missing data)


### 🛠️ Query Data with JOINs and Aggregations

#### Description
Write complex queries that combine data from multiple tables and perform calculations. Use JOINs to retrieve related information and aggregation functions to summarize data.

#### Requirements
Completed program should:

- Write INNER JOIN queries to find books by specific authors
- Write LEFT JOIN queries to find borrowers with their borrowed books
- Use COUNT, SUM, AVG aggregation functions
- Group results using GROUP BY and HAVING clauses
- Sort results with ORDER BY


### 🛠️ Integrate Database with FastAPI (Stretch Goal)

#### Description
Connect the database to a FastAPI application to create a complete REST API that reads from and writes to the database. Demonstrate how to query the database from Python code.

#### Requirements
Completed program should:

- Set up SQLite or PostgreSQL connection from Python
- Use SQLAlchemy ORM or raw SQL queries
- Implement API endpoints that interact with database tables
- Handle database transactions and error cases
- Return query results in JSON format
