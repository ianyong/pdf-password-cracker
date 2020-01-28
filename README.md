# PDF Password Cracker

A simple PDF password cracker written in Python with the ability to set constraints on the search space.

## Getting Started

Install pikepdf.

```
pip install pikepdf
```

## Usage

The program takes in 2 arguments, `file name` and `constraints`, with the latter being optional.

* To brute force a password without any constraints,

```
python password_cracker.py <file name>
```

The program will attempt to brute force the password using alphanumeric characters. Note that the program does not terminate until a password is found when running in this mode.

* To brute force a password with constraints,

```
python password_cracker.py <file name> <constraints>
```
Please see below for a more detailed explanation on the constraints.

## Constraints

You can specify the constraints on the search space through entering a string.

For example, `5/dt/u` will result in the program trying all possible passwords of length 4 where the first chracter is `5`, second character is a digit, third chracter is `t` and last character is an uppercase letter.

#### Specifiers

* /d - digits
* /a - alphabet (lowercase and uppercase letters)
* /u - uppercase letters
* /l - lowercase letters
* /c - alphanumeric chracters

The program will terminate if a non-recognised specifier is used.
