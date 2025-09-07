# Simple-_-PS_-Manager

A simple and secure Python-based password generator and manager that allows users to generate strong random passwords and store them in a CSV file for easy retrieval. Designed for everyday use to improve online security by creating unique passwords for each account.

Features

Random Password Generation
Generates secure passwords with customizable length and character types including:

Uppercase letters

Lowercase letters

Digits

Special characters

CSV Storage
Saves generated passwords along with the associated site and username to a CSV file for safe and organized storage.

Easy-to-Use
Command-line interface requiring minimal input from the user.

Installation

Clone the repository:

git clone <repository-url>


Navigate to the project directory:

cd password-generator


Ensure Python 3.x is installed.

Install any required dependencies (if any, optional for this script as it uses standard libraries).

Usage

Run the Python script:

python password_generator.py


Enter the site name and username when prompted.

The script will generate a secure password and display it in the console.

The password, site, and username will be stored in passwords.csv automatically.

Example
Enter the site name: example.com
Enter the username: john_doe
Generated password: X9v#2pLz!q1R
Password for example.com stored successfully.


The passwords.csv file will contain:

example.com,john_doe,X9v#2pLz!q1R

Security Considerations

The tool stores passwords in plaintext CSV for simplicity.

For sensitive usage, consider encrypting the CSV file or using a secure vault.

Always generate unique passwords for each account.

Contributing

Contributions are welcome! Feel free to submit pull requests or issues to improve the tool’s features, security, and usability.

License

This project is licensed under the MIT License. See the LICENSE file for details.
