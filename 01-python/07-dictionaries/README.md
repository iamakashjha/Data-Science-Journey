# Day 35 – Python Dictionaries: The Power of Key–Value Data

Most important Python data structures for Data Science: **Dictionaries**.

If lists are like Excel columns, dictionaries are like database records.

You'll use dictionaries constantly when working with:

- JSON files
- APIs
- Configuration files
- Machine Learning results
- Feature mappings
- Frequency counting

### Learning Objectives

By the end of today, you should be able to:

- Create and use dictionaries
- Access, add, update, and remove key-value pairs
- Iterate through dictionaries
- Understand nested dictionaries
- Count frequencies using dictionaries
- See why dictionaries are heavily used in Data Science


### Key Takeaway

Think of Python collections like this:

| Data Structure | Best For            |
| -------------- | ------------------- |
| **List**       | Ordered collections |
| **Tuple**      | Fixed records       |
| **Set**        | Unique values       |
| **Dictionary** | Key-value mappings  |


As a Data Scientist, dictionaries help you represent structured data:
```
customer = {
    "customer_id": 101,
    "name": "Rahul",
    "city": "Delhi",
    "total_orders": 12
}
```
This mirrors how data is often received from APIs and stored in JSON.