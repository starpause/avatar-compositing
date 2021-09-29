# avatar-compositing
 tools for generating avatars by combining several layers/components/traits.

# Artist instructions for Setup

1. Setup
    - Download https://code.visualstudio.com/
    - Download https://desktop.github.com/
    - Clone this repository 
    - Open in Visual Studio Code
2. Run example
    - Open CauseOfDeath\causes-of-death.py
    - Ctrl-Shift-P -> Extensions: Install Extensions -> Python -> Install
        - Install Python 3.* if you don't have it already
        - Install PIL
            - `python3 -m pip install --upgrade pip`
            - `python3 -m pip install --upgrade pillow`
    - Ctrl-Shift-P -> Python: Run Python File in Terminal
3. Make your own project
    - Create a folder
    - Make a sub-folder for each layer/trait 
    - Put every option for each layer/trait in it's respective folder
        - Images need to be PNG, all the same dimensions, with the trait positioned correctly
    - Copy CauseOfDeath\causes-of-death.py to your project folder
    - Modify the python to use your layers/traits
    - Ctrl-Shift-P -> Python: Run Python File in Terminal

