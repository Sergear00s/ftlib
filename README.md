# FTLIB

FTLIB is a Python library designed to simplify interactions with the [42 API](https://api.intra.42.fr/apidoc). It provides convenient Python functions to handle API parameters, significantly reducing repetitive and complicated code.

## Purpose

FTLIB helps you:

- Parameterize API requests easily through Python functions.
- Efficiently handle API pagination using the built-in `api.page` method with multithreading support.
- Reduce repetitive code related to OAuth2 authentication, request creation, and data management.

The modular design enables you to interact with various API endpoints using clearly defined Python methods, simplifying your development process.

If a specific endpoint is not available within the existing modules, you can directly use the **api** module's `get`, `post`, `patch`, or `delete` methods to make custom API calls without worrying about OAuth2 authentication. For endpoints requiring pagination, the `api.page` method is available.

## Modules Included

FTLIB provides the following modules:

- **achievement** – Retrieve and assign achievements.
- **api** – Manage custom API calls and efficiently handle pagination (`api.page` method).
- **campus** 
- **candidatures**
- **credentials** – Handle OAuth2 authentication and token management.
- **cursus** 
- **dump** – *(Currently under development.)*
- **evaluations** 
- **exam** 
- **exceptions** – Custom exceptions for better error handling.
- **journal** 
- **projects** 
- **quest**
- **scale_teams** 
- **title** 
- **users**
- **wallet (transaction)**

## Installation

Install via pip:

```bash
pip install git+https://github.com/serg00ns/ftlib
```

## Contributing

Fork the repository, improve the code, and merge request.

---

[Repository Link](https://github.com/serg00ns/ftlib)
