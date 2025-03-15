import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib as mpl
from pathlib import Path
import os


def generate_code_snippet_image(
        code=None,
        filename='code_snippet.png',
        title="LLM Integration with Error Handling and Testing",
        theme="monokai",
        show_line_numbers=True,
        dpi=300):
    """
    Generate a visually appealing code snippet image

    Args:
        code: List of code lines. If None, uses default example
        filename: Output filename
        title: Title of the code snippet
        theme: Color theme ('monokai', 'dracula', 'github-dark')
        show_line_numbers: Whether to display line numbers
        dpi: Image resolution
    """
    # Sample Python code for LLM integration if no code is provided
    if code is None:
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

    # Color themes
    themes = {
        "monokai": {
            "background": "#000000",
            "border": "#333333",
            "text": "#f8f8f2",
            "keyword": "#ff79c6",
            "function": "#50fa7b",
            "string": "#f1fa8c",
            "comment": "#6272a4",
            "builtin": "#ffb86c",
            "normal": "#f8f8f2",
            "decorator": "#bd93f9",
            "glow": "#8be9fd"
        },
        "dracula": {
            "background": "#000000",
            "border": "#282a36",
            "text": "#f8f8f2",
            "keyword": "#ff79c6",
            "function": "#8be9fd",
            "string": "#f1fa8c",
            "comment": "#6272a4",
            "builtin": "#bd93f9",
            "normal": "#f8f8f2",
            "decorator": "#50fa7b",
            "glow": "#bd93f9"
        },
        "github-dark": {
            "background": "#000000",
            "border": "#161b22",
            "text": "#c9d1d9",
            "keyword": "#ff7b72",
            "function": "#d2a8ff",
            "string": "#a5d6ff",
            "comment": "#8b949e",
            "builtin": "#ffa657",
            "normal": "#c9d1d9",
            "decorator": "#79c0ff",
            "glow": "#58a6ff"
        }
    }

    colors = themes.get(theme, themes["monokai"])

    # Figure setup with extremely tight proportions
    code_length = len(code)

    # Adjust height calculation to account for the legend size
    height = min(7, max(3.5, code_length * 0.025 + 1.2))
    width = 12

    # Create only one figure with proper dimensions
    fig = plt.figure(figsize=(width, height))
    ax = fig.add_subplot(111)

    # Remove axis
    ax.axis('off')

    # Set black background
    fig.patch.set_facecolor(colors["background"])
    ax.set_facecolor(colors["background"])

    # Create fancy border with glow effect
    border_pad = 0.05
    border_width = 2.0

    # Add glowing border with rounded corners
    fancy_box = FancyBboxPatch(
        (-border_pad, -border_pad),
        1 + 2 * border_pad, 1 + 2 * border_pad,
        boxstyle=f"round,pad={border_pad},rounding_size=0.2",
        ec=colors["glow"], fc="none",
        transform=ax.transAxes,
        linewidth=border_width,
        alpha=0.8,
        zorder=1000
    )
    ax.add_patch(fancy_box)

    # Define code parsing variables
    keywords = [
        'def', 'class', 'import', 'from', 'try', 'except', 'raise',
        'while', 'if', 'elif', 'else', 'for', 'return', 'async',
        'await', 'as', 'with', 'in', 'not', 'and', 'or', 'pass', 'None'
    ]

    builtins = [
        'str', 'int', 'float', 'bool', 'list', 'dict', 'set', 'tuple',
        'Dict', 'List', 'Optional', 'Union', 'Exception', 'True', 'False',
        'self', 'cls', 'super', 'object', 'len', 'print'
    ]

    # Set line height to approximately 1em (basically the height of the font
    # itself)
    line_height = 0.08 if code_length > 40 else 0.09 if code_length > 25 else 0.1
    # Move starting position down to account for legend and title
    top_margin = 0.88
    left_margin = 0.1
    # Use a more readable font size
    font_size = 9 if code_length > 40 else 10 if code_length > 25 else 11

    # Render code with improved syntax highlighting
    for i, line in enumerate(code):
        # Use an extremely tight line spacing calculation
        y_pos = top_margin - i * line_height

        # Add line numbers if enabled
        if show_line_numbers:
            line_num = ax.text(
                left_margin - 0.05,
                y_pos,
                f"{i + 1}",
                color=colors["comment"],
                fontfamily='DejaVu Sans Mono',
                fontsize=font_size - 1,
                ha='right',
                va='center',
                fontweight='light',
                alpha=0.7
            )

        # Basic indentation
        indent = len(line) - len(line.lstrip())
        line_content = line.lstrip()
        x_pos = left_margin + indent * 0.02

        # Process line based on content
        if not line_content:  # Empty line
            continue

        if line_content.startswith('#'):
            # Comment line
            ax.text(
                x_pos,
                y_pos,
                line_content,
                color=colors["comment"],
                fontfamily='DejaVu Sans Mono',
                fontsize=font_size,
                va='center'  # Keep vertical alignment at center
            )
        elif '"""' in line_content or "'''" in line_content:
            # Docstring
            ax.text(
                x_pos,
                y_pos,
                line_content,
                color=colors["string"],
                fontfamily='DejaVu Sans Mono',
                fontsize=font_size,
                va='center'
            )
        else:
            # Process code with syntax highlighting
            parts = []
            remaining = line_content
            pos = 0

            # Process strings first (both single and double quotes)
            for quote in ['"', "'"]:
                while quote in remaining:
                    start_idx = remaining.find(quote)
                    if start_idx == -1:
                        break

                    # Add content before the string
                    if start_idx > 0:
                        parts.append((remaining[:start_idx], None))

                    # Find the closing quote
                    content_start = start_idx + 1
                    end_idx = remaining.find(quote, content_start)

                    # If no closing quote, treat the rest as a string
                    if end_idx == -1:
                        parts.append((remaining[start_idx:], colors["string"]))
                        remaining = ""
                        break

                    # Add the string with quotes
                    string_content = remaining[start_idx:end_idx + 1]
                    parts.append((string_content, colors["string"]))

                    # Update remaining text
                    remaining = remaining[end_idx + 1:]

            # Process remaining parts by words
            if remaining:
                words = remaining.split()
                current = ""

                for word in words:
                    if word in keywords:
                        if current:
                            parts.append((current + " ", None))
                            current = ""
                        parts.append((word, colors["keyword"]))
                        parts.append((" ", None))
                    elif word in builtins:
                        if current:
                            parts.append((current + " ", None))
                            current = ""
                        parts.append((word, colors["builtin"]))
                        parts.append((" ", None))
                    elif "(" in word and not word.startswith("("):
                        # Function calls
                        func_name = word.split("(")[0]
                        if current:
                            parts.append((current + " ", None))
                            current = ""
                        parts.append((func_name, colors["function"]))
                        parts.append((word[len(func_name):], None))
                        parts.append((" ", None))
                    else:
                        current += word + " "

                if current:
                    parts.append((current, None))

            # Render the parts with improved spacing
            current_x = x_pos
            for text, color in parts:
                if not color:
                    color = colors["normal"]

                ax.text(
                    current_x,
                    y_pos,
                    text,
                    color=color,
                    fontfamily='DejaVu Sans Mono',
                    fontsize=font_size,
                    va='center',
                    fontweight='medium'
                )
                # FIX: Adjust word spacing to be more natural
                # Use a constant that scales better with font size
                current_x += len(text) * (0.0125 * font_size / 10)

    # Add title with subtle background
    # Adjust title position to account for extremely tight spacing
    title_y = 0.94
    title_box = FancyBboxPatch(
        (0.2, title_y - 0.03),
        0.6, 0.06,
        boxstyle="round,pad=0.02,rounding_size=0.02",
        ec=colors["border"],
        fc=colors["background"],
        alpha=0.8,
        transform=fig.transFigure
    )
    fig.add_artist(title_box)

    plt.figtext(
        0.5,
        title_y,
        title,
        ha="center",
        fontsize=14,
        color=colors["text"],
        fontweight='bold'
    )

    # Add improved syntax highlight legend
    # Adjust legend position and spacing for better readability
    legend_x = 0.03
    legend_y = 0.06
    legend_spacing = 0.025  # Increase spacing between legend items

    legends = [
        ("Keywords", colors["keyword"]),
        ("Functions", colors["function"]),
        ("Strings", colors["string"]),
        ("Comments", colors["comment"]),
        ("Built-ins", colors["builtin"]),
        ("Variables", colors["normal"])
    ]

    # Create legend box with more appropriate size
    legend_width = 0.18
    legend_height = legend_spacing * (len(legends) + 0.5)
    legend_box = FancyBboxPatch(
        (legend_x - 0.02, legend_y - 0.01),
        legend_width, legend_height,
        boxstyle="round,pad=0.02,rounding_size=0.02",
        ec=colors["border"],
        fc=colors["background"],
        alpha=0.8,
        transform=fig.transFigure
    )
    fig.add_artist(legend_box)

    # Render legend text with better spacing
    for i, (text, color) in enumerate(legends):
        plt.figtext(
            legend_x,
            legend_y + i * legend_spacing,
            f"■ {text}",
            color=color,
            fontsize=9,  # Slightly smaller but still readable
            fontweight='medium'
        )

    # Save with high quality and ultra-tight layout
    output_dir = os.path.dirname(filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Adjust tight_layout parameters for better overall spacing
    plt.tight_layout(pad=0.3, rect=[0.01, 0.01, 0.99, 0.99])
    plt.savefig(
        filename,
        dpi=dpi,
        facecolor=colors["background"],
        bbox_inches='tight',
        pad_inches=0.05  # Minimal padding
    )
    plt.close()
    print(f"Code snippet image saved as '{filename}'")


if __name__ == "__main__":
    # Example usage with various themes
    generate_code_snippet_image(
        filename='code_snippet_monokai.png',
        theme='monokai')
    generate_code_snippet_image(
        filename='code_snippet_dracula.png',
        theme='dracula')
    generate_code_snippet_image(
        filename='code_snippet_github.png',
        theme='github-dark')
