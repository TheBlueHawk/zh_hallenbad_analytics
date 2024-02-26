# Zürich Hallenbad City occupancy tracking

This project contains a Python script for periodically fetching the current visitor count from the Hallenbad City webpage and logging it with a timestamp.

## Prerequisites

- Python 3
- pip
- git (for cloning the repository)

## Setup Instructions

Follow these steps to set up the project on your own machine.

### 1. Clone the Repository

First, clone this repository to your local machine using git:

```sh
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create a Virtual Environment

Create a virtual environment named `hallenbad` in the project directory:

```sh
python3 -m venv hallenbad
```

Activate the virtual environment:

- On macOS and Linux:

  ```sh
  source hallenbad/bin/activate
  ```

- On Windows:

  ```cmd
  .\hallenbad\Scripts\activate
  ```

### 3. Install Required Packages

With the virtual environment activated, install the required packages:

```sh
pip install websocket-client
```

### 4. Identify Python and Script Paths

You will need to know the absolute paths to both your Python interpreter within the virtual environment and the `log_hallendbad_data.py` script for setting up the cron job.

- Python path:

  ```sh
  which python
  ```

  Or on Windows:

  ```cmd
  where python
  ```

- Script path:

  Use the absolute path to where `log_hallendbad_data.py` is located.

### 5. Create a Cron Job

Open your crontab file for editing:

```sh
crontab -e
```

Add a line to execute the script every 20 minutes:

```sh
*/20 * * * * /path/to/your/virtualenv/python /path/to/your/script/log_hallendbad_data.py
```

Make sure to replace `/path/to/your/virtualenv/python` and `/path/to/your/script/log_hallendbad_data.py` with the actual paths you identified earlier.

## Usage

Once set up, the script will automatically run every 20 minutes, logging the visitor count and timestamp to a file named `visitor_count_log.txt` in the script's directory.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to its development.

## License

[MIT License](LICENSE)
```
