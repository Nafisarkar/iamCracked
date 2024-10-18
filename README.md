
# iamCracked Software

**iamCracked** is a collection of hacking modules that can be dynamically loaded and executed based on the modules included in the `modules` directory.

## Features

- Dynamically loads and executes hacking modules from the `modules` directory.
- Each module file should be a Python script with a `main` function that contains the hacking functionality.
- The `main` function of each module is executed when the module is loaded.

## Requirements

- **Python 3.x**
- Required Python modules should be installed in the `modules` directory.

## Installation

1. Place your hacking module scripts in the `modules` directory.
2. Ensure that each module script has a `main` function that contains the hacking functionality.
3. Run the `main.py` script to execute the software.

### Dependencies

To install the required dependencies, create a `requirements.txt` file and add the following:

```
pycryptodome
```

Save this file in the same directory as your script.

To install the dependencies, open a terminal, navigate to the directory containing the `requirements.txt` file, and run:

```bash
pip install -r requirements.txt
```

This will install the `pycryptodome` library, which is required for password decryption functionality.

> Make sure to run this command in an environment where Python and pip are installed. If you're using a virtual environment, activate it before running the command.

## Usage

After the dependencies are installed, you can run the software using:

```bash
python iamCracked.py
```

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

## License

This software is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

If you have any questions or issues, feel free to contact the software developer at:
- Discord: [_sakuno]


## Acknowledgements

This software was created for **educational and ethical hacking purposes**. The developers do not condone any unauthorized or unethical hacking activities.

Special thanks to the following repositories that contributed to this project:

- [firefox_decrypt](https://github.com/unode/firefox_decrypt): Code from this repository was adapted to work with our system, enhancing the Firefox password decryption functionality.

We appreciate the open-source community and the valuable resources they provide, which have been instrumental in the development of this educational tool.

