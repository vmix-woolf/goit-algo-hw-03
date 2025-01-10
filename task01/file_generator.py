from pathlib import Path
import random

# Define file extensions and their respective counts
file_extensions = ['.txt', '.jpg', '.svg', '.js', '.php']
min_files_per_extension = 3
max_files_per_extension = 7
total_files = 20

# Directory to save files
output_dir = Path('source')
output_dir.mkdir(parents=True, exist_ok=True)

# Generate random content for different file types
def generate_content(extension):
    match extension:
        case '.txt':
            return "This is a sample text file."
        case '.jpg':
            return bytes([random.randint(0, 255) for _ in range(100)])  # Small binary data
        case '.svg':
            return """<svg height="100" width="100"><circle cx="50" cy="50" r="40" fill="blue"/></svg>"""
        case '.js':
            return "console.log('Hello, World!');"
        case '.php':
            return "<?php echo 'Hello, PHP World!'; ?>"
        case _:
            return ""

# Create files
file_counts = {ext: 0 for ext in file_extensions}
created_files = 0

while created_files < total_files:
    ext = random.choice(file_extensions)
    if file_counts[ext] < random.randint(min_files_per_extension, max_files_per_extension):
        file_counts[ext] += 1
        created_files += 1
        filename = output_dir / f"file_{created_files}{ext}"
        content = generate_content(ext)

        if isinstance(content, bytes):
            filename.write_bytes(content)
        else:
            filename.write_text(content)
