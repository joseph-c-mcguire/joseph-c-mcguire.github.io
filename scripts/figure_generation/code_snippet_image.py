import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.patches import Rectangle
import os


def generate_code_snippet_image():
    # Sample Python code for LLM integration
    code = [
        "# LLM Service Integration with Error Handling",
        "from typing import Dict, List, Optional, Union",
        "import time",
        "import logging",
        "import httpx",
        "",
        "class LLMProcessor:",
        "    def __init__(self, api_key: str, model: str = 'gpt-4', timeout: int = 30):",
        "        self.api_key = api_key",
        "        self.model = model",
        "        self.timeout = timeout",
        "        self.client = httpx.Client(timeout=timeout)",
        "        self.logger = logging.getLogger(__name__)",
        "",
        "    async def process_text(self, prompt: str, max_retries: int = 3) -> Dict:",
        "        \"\"\"Process text with LLM model with retry logic and error handling\"\"\"",
        "        attempt = 0",
        "        backoff = 2",
        "",
        "        while attempt < max_retries:",
        "            try:",
        "                self.logger.info(f'Sending request to LLM: {self.model}')",
        "                response = await self._send_request(prompt)",
        "                self._validate_response(response)",
        "                return response",
        "            except httpx.TimeoutException:",
        "                attempt += 1",
        "                wait_time = backoff ** attempt",
        "                self.logger.warning(f'Timeout error, retrying in {wait_time}s')",
        "                time.sleep(wait_time)",
        "            except Exception as e:",
        "                self.logger.error(f'Error processing request: {str(e)}')",
        "                raise",
        "",
        "        raise Exception(f'Failed after {max_retries} attempts')",
        "",
        "    # Unit test example",
        "    def test_process_text_retry_success(self, mocker):",
        "        # Mock the send request to fail twice then succeed",
        "        mock_send = mocker.patch.object(LLMProcessor, '_send_request')",
        "        mock_send.side_effect = [",
        "            httpx.TimeoutException('Timeout'),",
        "            httpx.TimeoutException('Timeout'),",
        "            {'result': 'success', 'text': 'response text'}",
        "        ]",
        "",
        "        result = self.process_text('Test prompt')",
        "        assert result['result'] == 'success'",
        "        assert mock_send.call_count == 3"]

    # Figure setup
    plt.figure(figsize=(12, 10))
    ax = plt.gca()
    ax.axis('off')

    # Set background color
    background = '#282c34'
    plt.gca().set_facecolor(background)
    plt.gcf().set_facecolor(background)

    # Colors for syntax highlighting
    keyword_color = '#c678dd'
    function_color = '#61afef'
    string_color = '#98c379'
    comment_color = '#7f848e'
    builtin_color = '#e5c07b'
    normal_color = '#abb2bf'
    decorator_color = '#e06c75'

    # Line height and padding
    line_height = 1
    top_margin = 1
    left_margin = 0.5

    # Text objects for lines
    line_objects = []
    keywords = [
        'def',
        'class',
        'import',
        'from',
        'try',
        'except',
        'raise',
        'while',
        'if',
        'for',
        'return',
        'async',
        'await',
        'as']
    builtins = [
        'str',
        'int',
        'Dict',
        'List',
        'Optional',
        'Union',
        'Exception',
        'self']

    for i, line in enumerate(code):
        text_objects = []
        y_pos = top_margin + i * line_height

        # Basic indentation
        indent = len(line) - len(line.lstrip())
        line = line.lstrip()
        x_pos = left_margin + indent * 0.25

        if line.startswith('#'):
            # Comment line
            text_obj = ax.text(
                x_pos,
                y_pos,
                line,
                color=comment_color,
                fontfamily='monospace',
                fontsize=12)
            text_objects.append(text_obj)
        else:
            # Split line by spaces for syntax highlighting
            parts = []
            in_string = False
            string_start = 0

            # Process strings first
            for j, char in enumerate(line):
                if char in ["'", '"'] and (j == 0 or line[j - 1] != '\\'):
                    if not in_string:
                        # Start of string
                        if j > 0:
                            parts.append((line[:j], normal_color))
                        string_start = j
                        in_string = True
                    else:
                        # End of string
                        parts.append((line[string_start:j + 1], string_color))
                        line = line[j + 1:]
                        break

            if not in_string:
                # No strings or all strings processed
                words = line.split()
                current_pos = x_pos

                for word in words:
                    if word in keywords:
                        color = keyword_color
                    elif word in builtins:
                        color = builtin_color
                    elif '(' in word and not word.startswith('('):
                        color = function_color
                    else:
                        color = normal_color

                    text_obj = ax.text(
                        current_pos,
                        y_pos,
                        word + ' ',
                        color=color,
                        fontfamily='monospace',
                        fontsize=12)
                    text_objects.append(text_obj)
                    current_pos += len(word + ' ') * 0.1
            else:
                # Process the parts with proper colors
                current_pos = x_pos
                for part_text, part_color in parts:
                    text_obj = ax.text(
                        current_pos,
                        y_pos,
                        part_text,
                        color=part_color,
                        fontfamily='monospace',
                        fontsize=12)
                    text_objects.append(text_obj)
                    current_pos += len(part_text) * 0.1

        line_objects.append(text_objects)

    # Add title and border
    plt.figtext(
        0.5,
        0.97,
        "LLM Integration with Error Handling and Testing",
        ha="center",
        fontsize=14,
        color="white")

    # Add syntax highlight legend
    legend_x = 0.02
    legend_y = 0.02
    legend_spacing = 0.03

    legends = [
        ("Keywords", keyword_color),
        ("Functions", function_color),
        ("Strings", string_color),
        ("Comments", comment_color),
        ("Built-ins", builtin_color),
        ("Variables", normal_color)
    ]

    for i, (text, color) in enumerate(legends):
        plt.figtext(
            legend_x,
            legend_y +
            i *
            legend_spacing,
            f"■ {text}",
            color=color,
            fontsize=10)

    # Save the image
    plt.tight_layout(rect=[0.02, 0.02, 0.98, 0.96])
    plt.savefig('code_snippet.png', dpi=300, facecolor=background)
    plt.close()
    print("Code snippet image saved as 'code_snippet.png'")


if __name__ == "__main__":
    generate_code_snippet_image()
