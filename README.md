# Bakery Pricing Software

This Python package provides interface for packing and pricing bakery product orders.


## Algorithms

The problem can be described as follow:
allocate the number of bakery products m to a finite types of packs with sizes
(number of units) v<sub>1</sub>, v<sub>2</sub>, ..., v<sub>n</sub>
The allocation can be described as a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>.
An optimal solution is to minimize total number of packs a<sub>1</sub>+a<sub>2</sub>+, ..., +a<sub>n</sub>.

A straightforward solution to this problem is the exhaustive search.
 However, it is computationally expensive when m is large.
Here, I propose a greedy heuristic approximation. Please see the description of algorithm in
 [documentation](https://github.com/chuanwuliu/bakery-pricing-software/blob/master/docs/algorithms.pdf)

## Run the Code
### Prerequisites:
    * Python 3.6
    * Git
 
   ### Download and run
   ```bash
   # Download the repo
   git clone https://github.com/chuanwuliu/bakery-pricing-software.git
   
   # Install the dependencies
   pip3 install -r bakery-pricing-software/requirements.txt
   
   # Run the software with example input
   python -m bakery-pricing-software -input ./bakery-pricing-software/tests/input_example.json
   ```
   ### Interface
   ```bash
   # The command line interface
   python -m bakery-pricing-software -input path/to/your/input.json
   ```   
   * The input must be in JSON format with code-quantity key-value pair, an example input is 
      ```json
        {
          "VS5": 10,
          "MB11": 14,
          "CF": 13
        }
     ```
More example inputs can be found in bakery-pricing-software/tests/
  * The output in generated in JSON format. An example output is
      ```json
    {
        "VS5": {
            "order": 10,
            "price": 13.98,
            "packs": {
                "5 $ 6.99": 2
            }
        },
        "MB11": {
            "order": 14,
            "price": 84.8,
            "packs": {
                "8 $ 9.95": 1,
                "2 $ 24.95": 3
            }
        },
        "CF": {
            "order": 13,
            "price": 36.89,
            "packs": {
                "5 $ 9.95": 2,
                "3 $ 16.99": 1
            }
        }
    }
    ```

## Configuration of Products
This software allows the bakery to update their product configuration. See
bakery-pricing-software/software/products.json for the current configuration.
The bakery can also config the production capacity in the configuration.

## Input Exceptions

The software will raise errors in these cases:
  * Order code is not found in the product list.
  * Order quantity is negative
  * Order quantity is not integer
  * Order quantity exceeds the production capacity
  * No solution.

## Test Cases:

Following cases are automated tested:
  * The example input given in the specification
  * The input with large number quantities (>10k)
  * All errors listed in Errors are also tested
  * The greedy heuristic are validated against the exhaustive search

Run the test cases with pytest
```bash
cd bakery-pricing-software/tests/
pytest
```

## Contact:
Chuanwu Liu: dr.liuchuanwu@gmail.com
