Problem 1
---------

Find the count of all the products
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Input
~~~~~
.. code-block:: json
    [
        {
            "rice": 629,
            "name": "Homefab India Set of 2 Royal Silky Aqua Blue Designer Curtains (HF158)"
        },
        {
            "rice": 499,
            "name": "Homefab India Set of 2  Beautiful Marble Plain Black Curtains (HF342)"
        },
        {
            "rice": 350,
            "name": "Set of 2 - measuring cups & measuring spoon"
        }
    ]

Expected Output
~~~~~~~~~~~~~~~
.. code-block:: json
    {
        "count": 3
    }


Problem 2
---------

Find the count of all active products
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Input
~~~~~

.. code-block:: json
    [
        {
            "endDate": "2017-04-04",
            "startDate": "2017-01-30",
            "price": 260,
            "category": "Kitchen",
            "name": "Stainless Steel Cutter Peeler Tool Pineapple Seed Clip Home Kitchen Gadgets"
        },
        {
            "endDate": "2017-12-04",
            "startDate": "2017-01-30",
            "price": 149,
            "category": "Kitchen",
            "name": "20.5cm Fruit Cutter Chef Kitchen Cutlery Knife Knives Choice - 07"
        },
        {
            "endDate": null,
            "startDate": "2017-01-30",
            "price": 1737,
            "category": "Electronics",
            "name": "LETV LeEco Le 2 32GB Rose Gold"
        },
        {
            "endDate": null,
            "startDate": "2018-01-30",
            "price": 999,
            "category": "Electronics",
            "name": "Nokia 1100"
        },
        {
            "endDate": null,
            "startDate": "2018-01-30",
            "price": 499,
            "category": "Furniture",
            "name": "Homefab India Set of 2  Beautiful Marble Plain Black Curtains (HF342)"
        }
    ]

Output assuming current date: `2017-09-23`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json
    {
      "count": 2
    }


Problem 3
---------

### Count products by grouping as per category

### Input
```json
[
    {
        "endDate": "2017-04-04",
        "startDate": "2017-01-30",
        "price": 260,
        "category": "Kitchen",
        "name": "Stainless Steel Cutter Peeler Tool Pineapple Seed Clip Home Kitchen Gadgets"
    },
    {
        "endDate": "2017-12-04",
        "startDate": "2017-01-30",
        "price": 149,
        "category": "Kitchen",
        "name": "20.5cm Fruit Cutter Chef Kitchen Cutlery Knife Knives Choice - 07"
    },
    {
        "endDate": null,
        "startDate": "2017-01-30",
        "price": 1737,
        "category": "Electronics",
        "name": "LETV LeEco Le 2 32GB Rose Gold"
    },
    {
        "endDate": null,
        "startDate": "2018-01-30",
        "price": 999,
        "category": "Electronics",
        "name": "Nokia 1100"
    },
    {
        "endDate": null,
        "startDate": "2018-01-30",
        "price": 499,
        "category": "Furniture",
        "name": "Homefab India Set of 2  Beautiful Marble Plain Black Curtains (HF342)"
    }
]
```

### Output assuming current date: `2017-09-23`
```json
{
    "Electronics": 1,
    "Kitchen": 1
}
```

Problem 4
---------

### Get total price of active products

### Input
```json
[
    {
        "endDate": "2017-04-04",
        "startDate": "2017-01-30",
        "price": 260,
        "category": "Kitchen",
        "name": "Stainless Steel Cutter Peeler Tool Pineapple Seed Clip Home Kitchen Gadgets"
    },
    {
        "endDate": "2017-12-04",
        "startDate": "2017-01-30",
        "price": 149,
        "category": "Kitchen",
        "name": "20.5cm Fruit Cutter Chef Kitchen Cutlery Knife Knives Choice - 07"
    },
    {
        "endDate": null,
        "startDate": "2017-01-30",
        "price": 1737,
        "category": "Electronics",
        "name": "LETV LeEco Le 2 32GB Rose Gold"
    },
    {
        "endDate": null,
        "startDate": "2018-01-30",
        "price": 999,
        "category": "Electronics",
        "name": "Nokia 1100"
    },
    {
        "endDate": null,
        "startDate": "2018-01-30",
        "price": 499,
        "category": "Furniture",
        "name": "Homefab India Set of 2  Beautiful Marble Plain Black Curtains (HF342)"
    }
]
```

### Output assuming current date: `2017-09-23`
```json
{
    "totalValue": 1186
}
```
