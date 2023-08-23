import os

# Define the name of the directory to be created
project_name = "NadlanDataProject"

# Folders and files to be created
folders_and_files = {
    project_name: [
        "README.md",
        "requirements.txt",
        "config.yaml",
        ".gitignore",
        {
            "data": [
                {
                    "raw": []
                },
                {
                    "processed": []
                },
                {
                    "coordinates": []
                }
            ]
        },
        {
            "notebooks": [
                "data_visualization.ipynb",
                "data_research.ipynb"
            ]
        },
        {
            "src": [
                "__init__.py",
                {
                    "scraper": [
                        "__init__.py",
                        "scraper.py"
                    ]
                },
                {
                    "coordinates": [
                        "__init__.py",
                        "coordinates.py"
                    ]
                },
                {
                    "pipeline": [
                        "__init__.py",
                        "data_pipeline.py"
                    ]
                },
                {
                    "utils": [
                        "__init__.py",
                        "helper_functions.py"
                    ]
                }
            ]
        },
        {
            "visualization": [
                "plot_helpers.py",
                "generate_plots.py"
            ]
        },
        {
            "research": [
                "research_helper.py",
                "conduct_research.py"
            ]
        }
    ]
}

def create_folder_structure(structure, parent_dir=""):
    for folder, content in structure.items():
        folder_path = os.path.join(parent_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        for item in content:
            if isinstance(item, dict):
                create_folder_structure(item, folder_path)
            else:
                file_path = os.path.join(folder_path, item)
                open(file_path, 'a').close()

# Create the project structure
create_folder_structure(folders_and_files)
