#!/bin/bash

# +----------------------------------+
# |  SSHash Python Binary Installer  |
# +----------------------------------+

# clear the terminal screen
clear

# VARIABLES
file="sshash.py"
outputfilename="sshash"
execpath="/usr/bin/"
dist_path="sshash_binary"

# function to make file into executable binary
function make_binary() {
    # Ensure PyInstaller is installed
    if ! command -v pyinstaller &> /dev/null
    then
        echo "PyInstaller could not be found. Please install it first."
        exit 1
    fi

    # Create the binary using PyInstaller
    pyinstaller --onefile $file --name $outputfilename --distpath $dist_path

    # Check if dist_path exists and is not empty
    if [ ! -d "$dist_path" ] || [ -z "$(ls -A $dist_path)" ]; then
        echo "Failed to create binary. Directory is empty or not found."
        exit 1
    fi

    # Check if execpath is writable
    if [ ! -w "$execpath" ]; then
        echo "The target directory $execpath is not writable."
        exit 1
    fi

    # Copy the binary to the execpath
    cp $dist_path/$outputfilename $execpath/$outputfilename

    # Check if the copy was successful
    if [ $? -eq 0 ]; then
        echo "Binary installed successfully."
    else
        echo "Failed to install the binary."
        exit 1
    fi
}

# set the main function of the installer
function main() {
    make_binary
}

# use the main function
main
