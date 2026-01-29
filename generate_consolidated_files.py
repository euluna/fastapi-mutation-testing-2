"""
Generate consolidated mutation diff file and extract routine source code
"""
import json
from pathlib import Path

def generate_consolidated_diff():
    """Generate a single file with all mutations as unified diffs"""
    with open('mutation_output/mutation_results.json', 'r') as f:
        results = json.load(f)
    
    with open('mutation_output/consolidated_mutations.diff', 'w', encoding='utf-8') as out:
        out.write("=" * 80 + "\n")
        out.write("CONSOLIDATED MUTATION DIFF FILE\n")
        out.write(f"Total Mutants: {len(results)}\n")
        out.write("=" * 80 + "\n\n")
        
        for mutant in results:
            out.write(f"Mutant #{mutant['id']:03d} - {mutant['operator']} - {mutant['status']}\n")
            out.write(f"Description: {mutant['description']}\n")
            out.write(f"Routine: {mutant['routine_name']}\n")
            out.write(f"{mutant['unified_diff']}\n")
            out.write("-" * 80 + "\n\n")
    
    print(f"✅ Generated consolidated_mutations.diff with {len(results)} mutants")

def extract_routine_source_code():
    """Extract source code for each tested routine"""
    with open('fastapi/encoders.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Define routines with their line ranges (manually determined)
    routines = {
        'isoformat': (36, 37),  # Lines 36-37
        'decimal_encoder': (41, 63),  # Lines 41-63
        'generate_encoders_by_class_tuples': (97, 104),  # Lines 97-104
        'jsonable_encoder': (111, 347)  # Lines 111-347 (main function)
    }
    
    with open('mutation_output/tested_routines_source.py', 'w', encoding='utf-8') as out:
        out.write('"""' + '\n')
        out.write("SOURCE CODE FOR TESTED ROUTINES FROM fastapi/encoders.py\n")
        out.write("=" * 80 + '\n')
        out.write('"""' + '\n\n')
        
        for routine_name, (start, end) in routines.items():
            out.write(f"\n{'#' * 80}\n")
            out.write(f"# ROUTINE: {routine_name}\n")
            out.write(f"# Lines: {start}-{end}\n")
            out.write(f"{'#' * 80}\n\n")
            
            for i in range(start - 1, end):  # Convert to 0-indexed
                out.write(lines[i])
            
            out.write("\n")
    
    print("✅ Generated tested_routines_source.py with source code for all tested routines")

if __name__ == "__main__":
    generate_consolidated_diff()
    extract_routine_source_code()
    print("\n✅ All files generated successfully!")
    print("  - mutation_output/consolidated_mutations.diff")
    print("  - mutation_output/tested_routines_source.py")
