#!/bin/bash

# Array of files with URLs and local names
FILES=(
    "https://umd.box.com/s/f48oq3kd2pebylyqpw35kyb1jjbgvvg5"
    "https://umd.box.com/s/gd8w3qawvj4le6ta0od373oavv9zjwu1"
)

# Function to download and unzip each file
download_and_unzip() {
    local file_url=$1
    local file_name=$2

    echo "Processing $file_name from $file_url"

    # Download the file only if it doesn't exist or has a different size
    if [ -f "$file_name" ]; then
        REMOTE_SIZE=$(curl -sI "$file_url" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
        LOCAL_SIZE=$(stat -c%s "$file_name")

        if [ "$REMOTE_SIZE" -eq "$LOCAL_SIZE" ]; then
            echo "$file_name already exists and matches the remote file size. Skipping download."
        else
            echo "$file_name size mismatch or incomplete. Re-downloading..."
            wget -O "$file_name" "$file_url"
        fi
    else
        echo "Downloading $file_name..."
        wget -O "$file_name" "$file_url"
    fi

    # Unzip the file in the current directory, maintaining its internal folder structure
    if [ -f "$file_name" ]; then
        echo "Unzipping $file_name..."
        unzip -o "$file_name"
        echo "$file_name unzipped successfully."
    else
        echo "Download failed or $file_name not found."
    fi
}

# Loop over each file in the list and process it
for file in "${FILES[@]}"; do
    # Split URL and filename
    download_and_unzip $file
done
