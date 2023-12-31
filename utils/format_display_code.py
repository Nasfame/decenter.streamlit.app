import logging

import black


def format_python_code(code) -> str:
    output: str
    try:
        output = black.format_str(code, mode=black.FileMode())
        # print(output)

    except Exception as e:
        output = f'Error formatting code: {str(e)}'
        logging.error(output)

    return output


def format_python_code_v1(code) -> str:
    output: str
    try:
        output = black.format_str(code, mode=black.FileMode())
        # print(output)

    except Exception as e:
        output = f'Error formatting code: {str(e)}'
        logging.error(output)

    return output


def format_python_code_v2(code) -> str:
    output: str
    try:
        output = black.format_str(code, mode=black.FileMode())
        # print(output)

    except Exception as e:
        output = f'Error formatting code: {str(e)}'
        logging.error(output)

    return output


if __name__ == '__main__':
    python_code = """
def hello_world():
    print("Hello, World!")
hello_world()
    """

    format_python_code_v1(python_code)
