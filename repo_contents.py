#!/usr/bin/env python3

import os
import sys
from pathlib import Path

def read_repoignore(directory):
    """Read .repoignore file if it exists and return list of patterns to ignore"""
    default_ignores = [
        'node_modules',
        'vendor',
        '.vscode',
        'bootstrap/cache',
        'storage',
        'public/vendor',
        'public/.htaccess',
        'public/favicon.ico',
        'public/hot',
        'public/robots.txt',
        'database/data',
        'tests',
        '.env',
        '.git',
        'repo_contents.py',
        'repository_contents.txt',
        'artisan',
        'package-lock.json',
        'composer.lock',
        'phpunit.xml',
    ]
    
    ignore_file = os.path.join(directory, '.repoignore')
    
    # Prepend the working directory to each pattern
    ignore_patterns = [os.path.join(directory, pattern) for pattern in default_ignores]
    
    if os.path.exists(ignore_file):
        with open(ignore_file, 'r') as f:
            # Add custom patterns from .repoignore, strip whitespace and prepend directory
            custom_patterns = [os.path.join(directory, line.strip()) 
                             for line in f.readlines() 
                             if line.strip()]
            ignore_patterns.extend(custom_patterns)
    
    return ignore_patterns

def should_ignore(path, ignore_patterns):
    """Check if path should be ignored based on ignore patterns"""
    path_str = str(path)
    for pattern in ignore_patterns:
        if pattern in path_str:
            return True
    return False

def process_directory(directory, output_file, ignore_patterns):
    """Recursively process directory and write contents to output file"""
    try:
        for root, dirs, files in os.walk(directory):
            # Convert to Path objects for easier handling
            root_path = Path(root)
            
            # Skip ignored directories
            dirs[:] = [d for d in dirs if not should_ignore(root_path / d, ignore_patterns)]
            
            for file in files:
                file_path = root_path / file
                
                # Skip ignored files
                if should_ignore(file_path, ignore_patterns):
                    continue
                    
                # Skip binary files and the output file itself
                if file_path.name == output_file.name:
                    continue
                    
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # Try to read the file as text
                        content = f.read()
                        
                        # Write the file path and contents to output
                        output_file.write(f"File: {file_path}\n")
                        output_file.write(content)
                        output_file.write("\n\n")
                except (UnicodeDecodeError, IOError):
                    # Skip files that can't be read as text
                    continue

    except Exception as e:
        print(f"Error processing directory: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python repo_contents.py <directory_path>", file=sys.stderr)
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory", file=sys.stderr)
        sys.exit(1)
    
    output_filename = "repository_contents.txt"
    output_path = os.path.join(directory, output_filename)
    
    # Get ignore patterns
    ignore_patterns = read_repoignore(directory)
    
    try:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            process_directory(directory, output_file, ignore_patterns)
        print(f"Successfully created {output_path}")
    except Exception as e:
        print(f"Error creating output file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 