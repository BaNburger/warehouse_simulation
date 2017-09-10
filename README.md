# General Purpose #
This simulation was built to help develop optimisation algorithms for the warehousing. The data simulates blik sensor data. The original work was done by Bastian Burger (blik) and it is further worked on with Solopex. Without any further agreements, only these two parties may use and change the code as they please.

## Usage ##
To run the program, execute the top-folder with the '''python3''' command.
In version 0.1, the warehouse parameters are directly stored in the warehouse.py file. All other parameters are stored in the __main__.py file.

## Versions ##
0.1: initial release

## ToDos ##
- The populate function should place items in close proximity. If put so, the items should form a grid
- The warehouse module should create a dynamic warehouse with forbidden areas and different locations
- The handlingdevice module should allow dynamic handling of goods
- A module should be written to insert and take out items over time
- A module should be written to plan fulfillments over time
- When dynamic, the simulation should write to a database
- The loadcarriers need a destination and base database
- A data base of destinations and delivery times should be created
- The good allocation can be built in the third dimension
