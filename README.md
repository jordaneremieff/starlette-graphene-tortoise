# starlette-graphene-tortoise

An example of a basic [Starlette](https://github.com/encode/starlette) app using [Tortoise ORM](https://github.com/tortoise/tortoise-orm) and [Graphene](https://github.com/graphql-python/graphene).

## Setup

```
# Setup the dev environment and install the dependencies
./scripts/setup

# Activate the virtualenv
. venv/bin/activate

# Create the database
python init_db.py

## Running

### From the virtualenv
```
uvicorn myapp.app:app --debug
```

### With docker
```docker-compose up -d```


## GraphQL queries & mutations

Navigate to `http://localhost:8000/graphql` in your browser to access the GraphiQL console to start making queries.

### Create a user

Query:

```
mutation CreateUser($name: String!) {
  createUser(name: $name) {
    user {
      id
      name
    }
  }
}
```

Query variables:

```
{"name": "Jordan"}
```

### Update a user

Query:

```
mutation UpdateUser($id:Int!, $name: String!) {
  updateUser(id: $id, name: $name) {
    user {
      id
      name
    }
  }
}
```

Query variables:

```
{"id" 1, "name": "Jordan Eremieff"}
```

### Query an individual user

Query:

```
query User($id: Int!) {
  user(id: $id) {
    id
    name
  }
}
```

Query variables:

```
{"id": 1}
```

### Query all users

Query:

```
query AllUsers {
  allUsers {
    id
    name
  }
}
```
