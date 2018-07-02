# Trojan CLI

**Current Version: 1.0.1**

## Latest Updates

1. Added username verifications
1. Added express actions

## Software Description

Trojan CLI is a command line tool for configuring trojan servers. This software supports only user-related operations at the moment.

</br>

## Download and Install
```
$ git clone https://k4yt3x.com/k4yt3x/Trojan_CLI.git  # Clone repo
$ cd Trojan_CLI/                                      # Enter repo directory
```

## Express Actions
```
$ sudo python3 trojan_cli.py -a Alice    # Add user Alice
$ sudo python3 trojan_cli.py -d Alice    # Delete user Alice
```

## Interactive Shell

```
$ sudo python3 trojan_cli.py -i  # Enter interactive shell
>>> adduser Alice                # Add user Alice
>>> deluser Alice                # Delete user Alice
```