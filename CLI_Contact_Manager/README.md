# CLI Contact Manager

A simple Python CLI application to manage contacts with persistent storage using JSON.

## Features

* Add Contact
* View Contacts
* Search Contact by:

  * Name
  * Phone Number
* Delete Contact
* Input Validation
* Persistent Contact Storage using `contacts.json`

## Validations

* Name cannot be blank
* Phone number must:

  * contain only digits
  * be exactly 10 digits
* Email must contain `@`

## Data Persistence

Contacts are automatically saved in:

```text
contacts.json
```

This allows contacts to persist even after closing and reopening the application.

## Run the Project

```bash
python contact_manager.py
```
