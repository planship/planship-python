# planship-python

Welcome to the Python client for the Planship API.

## Installation and basic usage

Install `planship` with pip, or another package manager of your choice like Poetry

``` console
pip install planship
# or
poetry add planship
```

Import and instantiate the `Planship` class, and start making calls to the Planship API

```python
from planship import Planship

planship = Planship(
    "clicker", # Planship product slug
    "https://api.planship.io", # Planship API endpoint URL
    "273N1SQ3GQFZ8JSFKIOK", # Planship API client ID
    "GDSfzPD2NEM5PEzIl1JoXFRJNZm3uAhX" # Planship API client secret
)

# list product plans
plans = planship.list_plans()

# create a customer with a name and email
customer = planship.create_customer({
    "name": "Darth Vader",
    "email:": "vader@empire.gov"
})

# subscribe the customer to a plan
subscription = planship.create_subscription(customer.id, "medium")

# retrieve customer entitlements
entitlements = planship.get_entitlements(customer.id)

# report usage for a customer
planship.report_usage(customer.id, "api-call", 11)
```

## Complete reference

The complete reference for the `Planship` class can be found [here](./docs/content/planship-class.md).
