import pandas as pd
from pathlib import Path

INPUT_FOLDER = Path("data")
OUTPUT_FOLDER = Path("output")

FILES_DATA = ["armor.csv", "decoration.csv", "skill_tree.csv", "skill.csv"]
FILES_TRANSLATIONS = ['head.csv', 'body.csv', 'arms.csv', 'waist.csv', 'legs.csv', 'decoration.csv', 'skill.csv', 'material.csv']

def change_data_armor(dataframe):
    # Do changes on armor data here
    return dataframe

def change_data_decoration(dataframe):
    # Do changes on decoration data here
    return dataframe

def change_data_skill_tree(dataframe):
    # Do changes on skill tree data here
    return dataframe

def change_data_skill(dataframe):
    # Do changes on skill data here
    return dataframe

def change_data_translation(dataframe):
    # Do changes on translation data here
    return dataframe

def process_file(input_path: Path, output_path: Path, transform_function):
    try:
        data = pd.read_csv(input_path, sep=',', encoding='utf-8', dtype=object)
        data = transform_function(data)
        data.to_csv(output_path, index=False, sep=',', encoding='utf-8')
    except Exception as error:
        print(f"Error processing file '{input_path.name}': {error}")

def main():
    if not INPUT_FOLDER.exists():
        raise FileNotFoundError(f"Input data folder not found.")
    
    (OUTPUT_FOLDER / "translations").mkdir(parents=True, exist_ok=True)

    for file in FILES_DATA:
        input_file_path = INPUT_FOLDER / file
        output_file_path = OUTPUT_FOLDER / file

        match file:
            case "armor.csv":
                process_file(input_file_path, output_file_path, change_data_armor)
            case "decoration.csv":
                process_file(input_file_path, output_file_path, change_data_decoration)
            case "skill_tree.csv":
                process_file(input_file_path, output_file_path, change_data_skill_tree)
            case "skill.csv":
                process_file(input_file_path, output_file_path, change_data_skill)
            case _:
                print(f"Unknown data file: {file}")

    for file in FILES_TRANSLATIONS:
        input_file_path = INPUT_FOLDER / "translations" / file
        output_file_path = OUTPUT_FOLDER / "translations" / file

        process_file(input_file_path, output_file_path, change_data_translation)

if __name__ == '__main__':
    main()
