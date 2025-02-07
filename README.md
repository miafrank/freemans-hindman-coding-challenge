## Install Python

[Template from my GH](https://github.com/miafrank/base_python_setup)

If you do not have Python, please install the latest 3.x version from `python.org`. You can check this by running: 

```
$ python --version
```

Alternatively you can install Python using [Homebrew](https://docs.brew.sh/Homebrew-and-Python)

```
brew install python@3.12
```

## Installing Pipenv

### Install pip 

Make sure you have pip available, you should if you are using Python downloaded from python.org.

Check this by running:

```
$ pip --version
```

If you do not have Pipenv installed already, install with [Homebrew](https://brew.sh/). [Pipenv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies) is the offical package management tool reccomended by Python (similar to `npm`): 

```
$ brew install pipenv
```

Alternatively, you can install Pipenv with pip: 

```
$ pip install --user pipenv
```

## Install dependencies from Pipfile in this project

```
$ pipenv install
```

## Run Tests

```
$ cd /path/to/this/project
$ pytest
```


# Q & A: 

### Q
C). Currently this code only runs via unit tests. How might we run an operation 
like this in production, at scale?


### A
To run this process at scale, one approach that stands out involves setting up a database that securely stores both unique IDs and their corresponding specialties. By implementing database transactions and other optimization techniques, we can uphold data integrity while maximizing performance.

In real-world scenarios, drawing from practical experience, we'd typically automate a batching/matching process to handle the workload efficiently. Here are some viable strategies:

1. Automated process that would continuously monitor the database for any new or updated records, using criteria such as `created_at` or `updated_at` timestamps. This ensures that our system remains up-to-date.

2. Partitioning strategy where IDs are grouped into batches based on predefined ranges. For instance, we might create batches where IDs fall within specific ranges, such as `batch_id.between(100-200)`, which may align with particularly specialty categories like "UX" or "front-end development".

3. A dynamic approach where batches would dynamically generate (potentially leveraging a queue) based on factors such as pending requests or system load.
