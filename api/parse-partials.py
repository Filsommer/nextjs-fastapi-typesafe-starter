import re

# Define the pattern to match lines containing the word "Optional"
pattern = re.compile(r'Optional\[')
patternList = re.compile(r'Optional\[List\[')

# Define the text to add at the end of matching lines
text_to_add = " = None"
text_to_add_list = " = []"

# Open the input file for reading
with open('./prisma_client/models.py', 'r') as input_file:
    # Read the content of the input file
    lines = input_file.readlines()

# Open a new file for writing
with open('./prisma_client/models.py', 'w') as output_file:
    # Process each line and write it to the output file
    for line in lines:
        # Check if the line contains the word "Optional"
        if re.search(patternList, line) and not "None" in line:
            # Add the desired text to the end of the line
            modified_line = line.rstrip() + text_to_add_list + '\n'
            output_file.write(modified_line)
        elif re.search(pattern, line) and not "None" in line:
            # Add the desired text to the end of the line
            modified_line = line.rstrip() + text_to_add + '\n'
            output_file.write(modified_line)
        else:
            # Write the unmodified line to the output file
            output_file.write(line)