#!/bin/bash

# check if source and destination directories were provided as arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <source_directory> <destination_directory>"
    exit 1
fi

source_directory="$1"
destination_directory="$2"

if [ ! -d "$source_directory" ]; then
    echo "Error: $source_directory is not a valid directory."
    exit 1
fi

if [ ! -d "$destination_directory" ]; then
    echo "Error: $destination_directory is not a valid directory."
    exit 1
fi

# move all files of the sub directories of passed `source_directory``
# to `source_directory`
find "$source_directory"/* -type f -exec mv {} "$source_directory/" \;

# delete all empty sub directories
find "$source_directory" -type d -empty -delete

# if there are multiple csv files, take the new one
for file in "$source_directory"/*.csv; do
    base=$(basename "$file" .csv)
    if [ -e "$base.csv_new.csv" ]; then
        rm "$file"
        echo "removed $file"
    fi
done

# rename all .csv_new.csv files to .csv
for file in "$source_directory"/*.csv_new.csv; do
    mv "$file" "${file%.csv_new.csv}.csv"
done

# find and delete files without both .csv and .flac files with the same name
for file in "$source_directory"/*; do
    base_name="${file%.*}"
    if [ ! -e "$base_name.csv" ] || [ ! -e "$base_name.flac" ]; then
        rm "$file"
        echo "removed $file"
    fi
done

# clear all files that are not .csv or .flac
for file in "$source_directory"/*; do
    if [ "${file##*.}" != "csv" ] && [ "${file##*.}" != "flac" ]; then
        rm "$file"
        echo "removed $file"
    fi
done

# move everything to `destination_directory``
mv "$source_directory"/* "$destination_directory"/

# delete source directory
rm -rf "$source_directory"
