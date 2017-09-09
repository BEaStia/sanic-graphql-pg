from graphql.execution.executors.asyncio import AsyncioExecutor
from sanic_graphql import GraphQLView
from sanic import Sanic
from schema import schema
from database import Base, init_db

app = Sanic(__name__)
app.debug = True


@app.listener('before_server_start')
async def init_graphql(app, loop):
    await init_db()


app.add_route(GraphQLView.as_view(schema=schema, graphiql=True), '/graphql')

# Optional, for adding batch query support (used in Apollo-Client)
app.add_route(GraphQLView.as_view(schema=schema, batch=True), '/graphql/batch')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
