#!/usr/bin/env python3
"""
Convert JSONL annotation files to JavaScript format for web viewing
"""

import json
import os
from pathlib import Path

def convert_jsonl_to_js(input_dir, output_dir):
    """Convert all JSONL files in input_dir to JS files in output_dir"""
    
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Create an index of all files
    file_index = {}
    
    for jsonl_file in input_path.glob('*.jsonl'):
        print(f"Processing {jsonl_file.name}...")
        
        # Read JSONL file
        with open(jsonl_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # Parse each line as JSON
        data = []
        for line in lines:
            if line.strip():
                try:
                    data.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Error parsing line in {jsonl_file.name}: {e}")
                    continue
        
        # Extract annotation_set from the data
        if data and 'annotation_set' in data[0]:
            annotation_set = data[0]['annotation_set']
        else:
            annotation_set = data
        
        # Create JavaScript file
        js_filename = jsonl_file.stem + '.js'
        js_filepath = output_path / js_filename
        
        # Write as JavaScript variable
        with open(js_filepath, 'w', encoding='utf-8') as f:
            f.write(f"// Annotations for {jsonl_file.stem}\n")
            f.write(f"const {jsonl_file.stem.replace('-', '_').replace(' ', '_')} = ")
            f.write(json.dumps(annotation_set, indent=2, ensure_ascii=False))
            f.write(";\n")
        
        file_index[jsonl_file.name] = {
            'filename': jsonl_file.name,
            'js_var': jsonl_file.stem.replace('-', '_').replace(' ', '_'),
            'js_file': js_filename,
            'count': len(annotation_set)
        }
        
        print(f"  → Created {js_filename} with {len(annotation_set)} stories")
    
    # Create index file
    index_file = output_path / 'index.js'
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write("// Index of all annotation files\n")
        f.write("const ANNOTATION_INDEX = ")
        f.write(json.dumps(file_index, indent=2))
        f.write(";\n")
    
    print(f"\n✓ Conversion complete! Created {len(file_index)} files")
    print(f"✓ Index file created: {index_file}")
    
    return file_index

if __name__ == '__main__':
    script_dir = Path(__file__).parent
    input_dir = script_dir / 'data'
    output_dir = script_dir / 'annotations_js'
    
    if not input_dir.exists():
        print(f"Error: Input directory not found: {input_dir}")
        print("Please make sure the 'data' folder exists with JSONL files")
        exit(1)
    
    convert_jsonl_to_js(input_dir, output_dir)
    print("\nYou can now use these JS files in your HTML by including them as <script> tags!")

