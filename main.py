import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from config import Base
from config import engine
from type.graphql import Query, Mutation

Base.metadata.create_all(bind=engine)

app = FastAPI()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix='/graphql')
