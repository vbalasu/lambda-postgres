# lambda-postgres

This project demonstrates how you can access a postgres database from a lambda function

Note that you have to update `.chalice/config.json` to configure the Subnet and Security group
to match that of the Postgres database, in this case, an Aurora Serverless instance

You can run the following command to get the table row counts:

`curl $(chalice url)`

Or you can execute a SELECT query as follows:

`curl -X POST $(chalice url)select -d @select.json -H "Content-Type: application/json"`