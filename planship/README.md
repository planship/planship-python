# planship-python

Welcome to the Python client for [Planship](https://planship.io).

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
    "clicker-demo",                         # Planship product slug
    "https://api.planship.io",              # Planship API endpoint URL
    "273N1SQ3GQFZ8JSFKIOK",                 # Planship API client ID
    "GDSfzPD2NEM5PEzIl1JoXFRJNZm3uAhX"      # Planship API client secret
)

# List product plans
plans = planship.list_plans()

# Create a customer with a name and email
customer = planship.create_customer({
    "name": "Darth Vader",
    "email:": "vader@empire.gov"
})

# Subscribe the customer with a given ID to a plan with a slug "medium"
subscription = planship.create_subscription(customer.id, "medium")

# Retrieve entitlements for a customer with a give ID
entitlements = planship.get_entitlements(customer.id)

# Report usage for a customer with given ID for a given metering ID
planship.report_usage(customer.id, "api-call", 11)
```

The complete reference for the `Planship` class can be found [here](./docs/content/planship-class.md).

## Links

- [Planship documentation](https://docs.planship.io)
- [Planship Python client at PyPI](https://pypi.org/project/planship/)
- [Planship Console sign-up](https://app.planship.io/auth/sign-up)
