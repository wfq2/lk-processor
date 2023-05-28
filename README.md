# lk-processor

## Project Setup

- (Language) Python 3.11.3
- IDE Used: Pycharm
- Install Pipenv: ```pip install pipenv```
- Install dependencies: ```pipenv install --dev```
- Running the script: first activate pipenv shell ```pipenv shell```
and run the processor from the console ```python src/main.py {input_file_name} {output_file_name}```
- Input files live in the input_files directory, and output files will be places into output_files directory
- Alternatively the script can be run through tests, by running the test_main() function

## Project Description

My overall approach to a problem like this is to separate functionality like so:
1. Retrieve Data (persistence.py)
2. Parse Data / Clean it / Format it (persistence.py)
3. Core business logic (transforms.py)
4. Output Data (persistence.py)

The parsing / cleaning logic could get pretty complex.  For now it's very simple based on the test
dataset, and just updates a wrongly formatted date.  Given some more information we could also catch:
- wrong industries
- pal & exposure values that don't make sense
- wrong tickers / identifiers
- non-existent analysts

By the time the data gets to the core business logic, we should be able to assume it is accurate.  This will help
keep it simple and easier to test (current tests assume correct information).

Lastly I added a few test scenarios that were easier to validate transformations on.