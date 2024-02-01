# pcheck - Pinterest Checker

## Overview

pcheck is a user-friendly command-line tool designed to retrieve information about pins and boards from a Pinterest user's profile. The application aims to simplify the process of tracking changes, monitoring activities, and obtaining relevant data from specific boards and pins on Pinterest. It provides users with a quick and convenient way to access the information they are interested in.

## Features

- **Information Retrieval:** Obtain detailed data about pins and boards associated with a Pinterest user account.

- **Sync Changes:** Keep track of updates and changes in the specified boards and pins.

- **User-Friendly Interface:** pcheck is designed for ease of use, allowing users to quickly gather the information they need.

## Getting Started

### Prerequisites

Before using pcheck, make sure you have the following installed:

- [Python](https://www.python.org/) (version 3.7 or higher)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/pcheck.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pcheck
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run pcheck with the desired Pinterest username:

    ```bash
    python pcheck.py --username <pinterest_username>
    ```

2. Follow the on-screen instructions to retrieve information about boards and pins.

### Examples

- Retrieve information about a user's boards:

    ```bash
    python pcheck.py --username user123 --boards
    ```

- Get details about a specific pin:

    ```bash
    python pcheck.py --username user123 --pin <pin_id>
    ```

### Commands

1. **Get information about a specific board:**

   ```bash
   python main.py -b <Board_ID> --boards -a <Access_Token>
   ```

2. **Get information about a specific pin:**

   ```bash
   python main.py -p <Pin_ID> -a <Access_Token>
   ```

3. **Get information about boards of a specific user:**

   ```bash
   python main.py -u <Username> --user-boards -a <Access_Token>
   ```

4. **Get information about pins of a specific user:**

   ```bash
   python main.py -u <Username> --user-pins -a <Access_Token>
   ```

### Options

- `-ps` or `--page-size`: Set the page size when fetching lists of boards or pins.

   ```bash
   python main.py -u <Username> --user-boards -a <Access_Token> -ps 10
   ```

### Notes

- Replace `<Board_ID>`, `<Pin_ID>`, `<Username>`, and `<Access_Token>` with your actual values.

## Contributions

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
