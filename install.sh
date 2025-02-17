#!/bin/bash
# Simple installer for hello application

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Extract the executable
tar xzf "$SCRIPT_DIR/hello.tar.gz"

# Remove quarantine attribute
xattr -d com.apple.quarantine hello 2>/dev/null || true

# Make executable
chmod +x hello

echo "Installation complete! You can now run ./hello" 