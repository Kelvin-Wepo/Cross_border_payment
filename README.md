
# Money Transfer App

The Money Transfer App is a Django-based application that allows users to securely transfer money, manage their savings, and view their transaction history. This project is designed to provide a convenient and reliable platform for individuals to perform financial transactions.

## Features

1. **User Registration and Authentication**: Users can register for an account and log in to the application using their mobile number, mobile money provider, and mobile money account ID.

2. **Money Transfer**: Users can transfer money to other registered users, with the ability to view transaction details such as the amount, fee, and exchange rate.

3. **Savings Management**: Users can create savings accounts, set recurring deposits, and track their savings progress.

4. **User Roles and Permissions**: The application supports different user roles, such as regular users and administrators, with corresponding permissions to perform specific actions.

## Technologies Used

- **Django**: The core web framework used for building the application.
- **Django ORM**: The object-relational mapping (ORM) library used for interacting with the database.
- **SQLite**: The default database used for development, but the application can be configured to use other database engines.
- **Tailwind CSS**: A utility-first CSS framework used for styling the application.
- **Lucide**: An open-source library of customizable icons used in the application.
- **Recharts**: A charting library used for visualizing financial data.

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/Kelvin-Wepo/Cross_border_payment.git
   ```

2. **Create a virtual environment and activate it**:
   ```
   cd money-transfer-app
   python -m venv env
   source env/bin/activate
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```
   python manage.py migrate
   ```

5. **Create a superuser account**:
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```
   python manage.py runserver
   ```

The application should now be accessible at `http://localhost:8000/`.

## Usage

1. **Register a new user**: Visit the registration page and provide the required information to create a new user account.

2. **Transfer money**: Log in to the application and navigate to the "Transfer" section. Enter the recipient's details and the amount to be transferred.

3. **Manage savings**: In the "Savings" section, users can create new savings accounts, set recurring deposits, and view their savings history.

4. **View transaction history**: The application provides a transaction history section where users can see details of their past money transfers.

5. **Administer the application**: Superusers and administrators can access the Django admin interface to manage users, groups, permissions, and other application-specific data.

## Contributing

Contributions to the Money Transfer App are welcome. If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).