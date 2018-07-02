# Trojan CLI

**Current Version: 1.0**

## Latest Updates

1. Added user controller

## Software Description

Trojan CLI is a command line tool for configuring trojan servers. This software supports only user-related operations at the moment.

## Usage

Download Trojan CLI
```
$ git clone https://k4yt3x.com/k4yt3x/Trojan_CLI.git
$ cd Trojan_CLI/
```

Launch software
```
$ sudo python3 trojan_cli.py
```

To add one user called "Alice"
```
>>> adduser Alice
```
Then the password will be displayed on the screen.

To delete user called "Alice"
```
>>> deluser Alice
```
Then user Alice will be deleted from the server configuration.