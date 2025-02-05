import json
import os

def extract_id_and_title_ndjson(input_path, output_path):
    """
    Reads a large JSON file in NDJSON format (one JSON object per line)
    and extracts only the 'id' and 'title' fields from each record.
    
    The output is written as a proper JSON array to the output file.
    
    Args:
        input_path (str): Path to the input NDJSON file.
        output_path (str): Path to the output JSON file.
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        
        outfile.write("[\n")
        first = True
        line_count = 0
        extracted_count = 0
        
        for line in infile:
            line_count += 1
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"JSON decode error at line {line_count}: {e}")
                continue

            new_record = {
                "id": record.get("id"),
                "title": record.get("title")
            }
            
            if new_record["id"] is None or new_record["title"] is None:
                # Skip records that do not contain both fields.
                continue

            if not first:
                outfile.write(",\n")
            else:
                first = False

            outfile.write(json.dumps(new_record))
            extracted_count += 1
        
        outfile.write("\n]")
    
    print(f"Processed {line_count} lines. Extracted {extracted_count} records.")
    print(f"Extraction complete. Output saved to {output_path}")

if __name__ == '__main__':
    # Define your input and output file paths.
    input_file = os.path.join("data", "titles_with_ids.json")
    output_file = os.path.join("output", "id_titles.json")
    
    extract_id_and_title_ndjson(input_file, output_file)
