# What Ducks Want

The application collects data about how, where, when, and what ducks are fed across the world. The application also allows the user to provide a repeat frequency.

 **Since this is just a MVP, we are making a comprise on some of the advanced features.**

## Tech Stack

**Language and Framework:** We have decided to use Python and the Flask framework. Python provides us a wide range of functionalities to analyze and summarize the data we collect. That would be something we might need to implement in future. ( Smart Dashboards). We are making that decision in advance.

**Database:** The application we need to support doesn't require consistency. We are just collecting data and we would seldom have updates to the data. Therefore, we would prefer going with a NoSQL database. In this case, we are using MongoDB.

**Containerization:** We use Docker to Containerize the application.


# Database Design

```
Table foodtype {
  id varchar [pk, increment]
  name varchar[not_null]
}

Table food {
  id varchar [pk, increment]
  name varchar[not_null]
  type_id varchar
 }

// The main database table
Table park {
  id varchar [pk, increment]
  count_ducks int[not_null]
  food_id varchar[not_null]
  name varchar
  hour int[not_null]
  minute int
  lat int
  lng int
}

Ref: foodtype.id > food.type_id
Ref: park.food_id > food.id

```
![Database Design](https://user-images.githubusercontent.com/18748713/134434446-e56f9e02-75f8-4897-a420-568625d4d64a.png)

# Ideal Architecture

For a production level application, we could follow the following Architecture. But since we are working on a small scale application, we are just working on the docker container that would be deployed in the `app` portion of the Kubernetes cluster.

![Architecture Diagram](https://user-images.githubusercontent.com/18748713/134438916-69e49ee1-5efb-4087-a5f0-fe67d9434b44.png)

![Architecture Diagram](https://user-images.githubusercontent.com/18748713/134438923-1c8ec149-52ba-454b-b1b1-3daaa2109e7d.png)

# API Design

**All parameters are mandatory unless mentioned otherwise.**

### POST /food_types

Create a new food type with the given name.

**Parameters**

`name` : The name of the food type.

### GET /food_types

Returns all the food types.

### POST /foods

Create a new food item with the given name and type.

**parameters**

`name` : name of the food
`type` : type of food (id)

### GET /foods

Returns all foods unless a `type` is provided.

**Parameters**

`type` : Type of food (id).

### POST /parks

Create an entry for a park with the given details

**parameters**

`count`: Number of ducks in the park.
`food` : Type of food (id)
`name` : Name of the park (optional).
`hour` : Time when the ducks are fed.
`min` : Time when the ducks are fed (optional - Default 0).
`lat` : Where the ducks are fed.
`lng` : Where the ducks are fed.

### GET /parks

Returns all the parks (paginated 10 per page)


### Time Spent

**Backend** - 4 hours
**Front end** - 3 hours
**Deployment and Documentation** 1 hour
