#!/bin/bash

# Check if at least one parameter is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <filename> [output_filename]"
    exit 1
fi

# Extract the first parameter
input_file="$1"

# Check if the second parameter is provided
if [ -z "$2" ]; then
    # Get the base name and extension of the input file
    base_name=$(basename "$input_file")
    extension="${base_name##*.}"
    
    # Check if the file has an extension
    if [ "$base_name" == "$extension" ]; then
        # No extension, add .mp3
        output_file="${input_file}.mp3"
    else
        # Replace the extension with .mp3
        output_file="${input_file%.*}.mp3"
    fi
else
    # Use the second parameter as the output file
    output_file="$2"
fi

# Print the result (or perform the desired operation)
echo "Input file: $input_file"
echo "Output file: $output_file"

ffmpeg -i "$input_file" -vn -ab 192k -ar 44100 -y "$output_file"

