# Learning Tech: DIY Change Data Capture On Localhost

Hey there! So, imagine your data is like a lively neighborhood, and every day, 
new things are happening—new people moving in, kids starting school, and maybe 
some folks leaving. Now, change data capture (CDC) is like having a super 
observant neighbor who keeps tabs on all these happenings and lets you know 
what's different every day.

In tech terms, CDC is a cool way to track and capture changes in your database, 
like when new data is added, existing data is updated, or when something is 
deleted. It's like having a snapshot of your data's daily adventures, making 
it easier for you to stay in the loop without having to sift through the entire 
neighborhood gossip.

Setting up CDC is like putting on your neighborhood watch hat—it helps you 
keep track of all the comings and goings in your data world. 
So, let's build this system for free on our local laptop to better understand
how to monitor our data and the tools used! First, let's introduce the tools
that we are going to use: Kafka, Debezium, and Postgres

## Tools and Terminology
## Apache Kafka
[Kafka](https://kafka.apache.org/) is one of the backbones of the real-time data revolution. Picture it as the bustling 
central hub where data streams converge and diverge, forming a bustling metropolis of information 
exchange. Kafka ensures that no byte of data is left unexplored, connecting your applications in a 
seamless dance of communication.

At its core, Kafka is an open source distributed event streaming platform. That's a lot of dense wording,
but we can summarize it by saying that its a robust, flexible, and efficient PubSub platform. One end
will write to topics, and consumers will listen and react to the messages received from the publisher.
It helps decouple and scale our applications with asyncronous data processing.

## Debezium
Now, let's introduce Debezium, the game-changer in the realm of change data capture. 
Imagine a world where you not only store data but also capture every subtle change in 
real-time - that's the magic Debezium brings to the table.

Debezium acts as a connector between your databases and Apache Kafka, the distributed 
streaming platform. It taps into the database's transaction log, capturing every insert, 
update, or delete operation. This change data is then streamed to Kafka topics, creating a 
real-time pipeline of events that reflects the evolving state of your database.

Why is this important? Well, Debezium's Change Data Capture allows you to react instantly 
to database changes, opening doors to a plethora of use cases, from maintaining data 
replicas to triggering real-time analytics or feeding data into microservices architectures.

In simpler terms, Debezium is your data detective, keeping an eye on the ever-changing 
landscape of your database and broadcasting those changes to the rest of your data ecosystem.

## Postgres
Finally, let's meet PostgreSQL, the unsung hero of the relational database world. 
If databases were superheroes, PostgreSQL would be the one quietly ensuring data 
integrity and reliability behind the scenes. This open-source, object-relational database 
system has been winning hearts for its extensibility, standards compliance, and robustness.

What sets PostgreSQL apart? Well, it goes beyond just storing data; it's your trustworthy 
companion for handling complex queries, transactions, and scaling with ease. Whether 
you're a small startup or a large enterprise, PostgreSQL's flexibility and adherence to 
SQL standards make it a go-to choice for developers and database administrators alike.

