from typing import Any


def inquirer_input(message: str, valueType: Any = None) -> Any:
    result = input(f'{message}: ') if message[-1] != ' ' and message[-2] != ':' else input(message)

    if len(result) == 0:
        print('No Answer was provided. Please provide one.')
        inquirer_input(message)

    if valueType == None:
        return result

    try:
        output = valueType(result)
        return output

    except:
        print('Invalid value. Please try again.')
        inquirer_input(message)
