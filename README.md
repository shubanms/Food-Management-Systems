# Restaurant Management System

## Table of Contents
- [Introduction](#introduction)
- [Database Schema](#database-schema)
- [Table Descriptions](#table-descriptions)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Restaurant Management System is a database-driven application designed to facilitate the management of restaurants, including tracking locations, employees, customers, orders, and more. It provides a comprehensive set of tables to store and manage relevant information for efficient restaurant operations.

This documentation provides an overview of the database schema, table descriptions, installation instructions, and usage guidelines for the Restaurant Management System.

## Database Schema
The database schema for the Restaurant Management System consists of several interconnected tables:

- LOCATIONS: Stores information about different restaurant locations.
- RESTAURANTS: Represents individual restaurants, linked to specific locations.
- RESTAURANTWASTAGE: Tracks wastage details for each restaurant.
- CUSTOMERS: Stores customer details.
- EMPLOYEES: Contains information about employees, including waiters and chefs.
- WAITERS: Associates employees with restaurants as waiters.
- CHEFS: Associates employees with restaurants as chefs.
- MENUITEMS: Stores menu items offered by each restaurant.
- ORDERSTATUSES: Lists the possible statuses for orders.
- ORDERS: Represents customer orders, linked to customers, waiters, and order statuses.
- ORDERLINE: Contains individual items and quantities within an order.
- DELIVERYEMPLOYEES: Associates delivery employees with regular employees.
- DELIVERY: Tracks delivery details for orders.
- DINEINCUSTOMERS: Stores details of customers dining in at the restaurant.
- DELIVERYCUSTOMERS: Stores details of customers for delivery orders.
- FEEDBACK: Captures customer feedback.

## Table Descriptions
1. LOCATIONS
   - `location_id`: Primary key for the location.
   - `location_name`: Name of the location.
   - `address`: Address of the location.
   - `city`: City where the location is situated.
   - `state`: State where the location is situated.
   - `country`: Country where the location is situated.

2. RESTAURANTS
   - `restaurant_id`: Primary key for the restaurant.
   - `restaurant_name`: Name of the restaurant.
   - `location_id`: Foreign key referencing the location of the restaurant.

3. RESTAURANTWASTAGE
   - `wastage_id`: Primary key for the wastage record.
   - `restaurant_id`: Foreign key referencing the restaurant associated with the wastage.
   - `date`: Date of the wastage record.
   - `wastage_details`: Details of the wastage.

4. CUSTOMERS
   - `customer_id`: Primary key for the customer.
   - `customer_name`: Name of the customer.
   - `address`: Address of the customer.
   - `city`: City where the customer is located.
   - `state`: State where the customer is located.
   - `country`: Country where the customer is located.
   - `phone_number`: Phone number of the customer.
   - `email`: Email address of the customer.

5. EMPLOYEES
   - `employee_id`: Primary key for the employee.
   - `employee_name`: Name of the employee.
   - `address`: Address of the employee.
   - `city`: City where the employee is located.
   - `state`: State where the employee is located.
   - `country`: Country where the employee is located.
   - `phone_number`: Phone number of the employee.
   - `email`: Email address of the employee.

6. WAITERS
   - `waiter_id`: Primary key for the waiter.
   - `employee_id`: Foreign key referencing the employee associated with the waiter.
   - `restaurant_id`: Foreign key referencing the restaurant where the waiter works.

7. CHEFS
   - `chef_id`: Primary key for the chef.
   - `employee_id`: Foreign key referencing the employee associated with the chef.
   - `restaurant_id`: Foreign key referencing the restaurant where the chef works.

8. MENUITEMS
   - `menu_item_id`: Primary key for the menu item.
   - `restaurant_id`: Foreign key referencing the restaurant associated with the menu item.
   - `item_name`: Name of the menu item.
   - `description`: Description of the menu item.
   - `price`: Price of the menu item.

9. ORDERSTATUSES
   - `order_status_id`: Primary key for the order status.
   - `status_name`: Name of the order status.

10. ORDERS
    - `order_id`: Primary key for the order.
    - `customer_id`: Foreign key referencing the customer placing the order.
    - `waiter_id`: Foreign key referencing the waiter serving the order.
    - `order_status_id`: Foreign key referencing the status of the order.
    - `order_date`: Date of the order.
    - `total_amount`: Total amount of the order.

11. ORDERLINE
    - `orderline_id`: Primary key for the order line item.
    - `order_id`: Foreign key referencing the order associated with the line item.
    - `menu_item_id`: Foreign key referencing the menu item included in the order.
    - `quantity`: Quantity of the menu item in the order.

12. DELIVERYEMPLOYEES
    - `delivery_employee_id`: Primary key for the delivery employee.
    - `employee_id`: Foreign key referencing the employee associated with the delivery employee.

13. DELIVERY
    - `delivery_id`: Primarykey for the delivery.
    - `order_id`: Foreign key referencing the order associated with the delivery.
    - `delivery_employee_id`: Foreign key referencing the delivery employee responsible for the delivery.
    - `delivery_date`: Date of the delivery.
    - `address`: Address where the delivery is being made.
    - `city`: City where the delivery is being made.
    - `state`: State where the delivery is being made.
    - `country`: Country where the delivery is being made.

14. DINEINCUSTOMERS
    - `customer_id`: Primary key referencing the customer dining in at the restaurant.
    - `table_number`: Table number assigned to the customer.

15. DELIVERYCUSTOMERS
    - `customer_id`: Primary key referencing the customer for a delivery order.
    - `address`: Address of the customer for the delivery.
    - `city`: City where the customer for the delivery is located.
    - `state`: State where the customer for the delivery is located.
    - `country`: Country where the customer for the delivery is located.

16. FEEDBACK
    - `feedback_id`: Primary key for the feedback.
    - `customer_id`: Foreign key referencing the customer providing the feedback.
    - `feedback_date`: Date of the feedback.
    - `feedback_text`: Feedback message from the customer.

## Installation and Setup
To install and set up the Restaurant Management System, follow these steps:

1. Run dbms.ipynb in Jupyter Notebook or any compatible environment to create the database, create tables, and insert data.

2. Once the database is set up, navigate to the "project" directory in the terminal or command prompt.

3. Run the following command to install the necessary Python dependencies:

   ```console
   C:\Users\User>pip install flask psycopg2
   ```

4. After installing the dependencies, you can start the Flask server by running the following command:

   ```console
   C:\Users\User>Food-Management-Systems>project>python app.py
   ```

5. The server will start running, and you should see an output similar to:

  ```
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

6. Open a web browser and visit http://127.0.0.1:5000/ to access the Restaurant Management System.

Make sure to keep the database connection details (host, database, user, password) in the app.py file properly configured to match your PostgreSQL setup.

You may need to adjust the HTML file paths and other configurations in the app.py file based on your specific project structure and requirements.

With these steps, you should be able to run the dbms.ipynb notebook to set up the database and then run the Flask server to access the Restaurant Management System in the browser.

## Usage
Once the Restaurant Management System is installed and set up, you can use it to manage restaurant-related operations. Here are some examples of common operations:

- Add new restaurants, locations, employees, and customers to the system.
- Track wastage details for each restaurant.
- Place customer orders and manage order status.
- Assign waiters and chefs to specific restaurants.
- Manage menu items offered by each restaurant.
- Track delivery details for delivery orders.
- Capture customer feedback.

Refer to the table descriptions above for more details on each table's purpose and fields.

## Authors
- [@Shuban M S](https://github.com/shubanms)

## Contributing
Contributions to the Restaurant Management System are welcome! If you have any improvements or new features to suggest, please submit a pull request on the GitHub repository.

## License
The Restaurant Management System is licensed under the Apache License 2.0.
