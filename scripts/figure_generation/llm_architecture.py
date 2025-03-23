import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def generate_architecture_diagram():
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))

    # Define component colors
    colors = {
        'client': '#3498db',
        'api': '#2ecc71',
        'llm': '#9b59b6',
        'database': '#e74c3c',
        'backend': '#f39c12',
        'container': '#95a5a6',
        'cache': '#1abc9c'
    }

    # Background for sections
    ax.add_patch(
        patches.Rectangle(
            (0.5,
             0.5),
            11,
            7,
            fill=True,
            alpha=0.1,
            color='gray'))

    # Client Components
    draw_box(ax, 1, 6, 2, 1, colors['client'], 'User Interface')

    # API Gateway
    draw_box(ax, 4, 6, 2, 1, colors['api'], 'API Gateway')

    # Backend Services
    draw_box(ax, 7, 6, 2, 1, colors['backend'], 'Microservices')

    # LLM Components
    draw_box(ax, 4, 4, 2, 1, colors['llm'], 'LLM Orchestrator')
    draw_box(ax, 2, 2.5, 2, 1, colors['llm'], 'Model A')
    draw_box(ax, 6, 2.5, 2, 1, colors['llm'], 'Model B')

    # Data Storage
    draw_box(ax, 9, 3, 2, 1, colors['database'], 'Database')
    draw_box(ax, 9, 1.5, 2, 1, colors['cache'], 'Cache')

    # MLOps
    draw_box(ax, 1, 4, 2, 1, colors['container'], 'CI/CD Pipeline')

    # Connections
    draw_arrow(ax, 3, 6.5, 4, 6.5)  # User -> API
    draw_arrow(ax, 6, 6.5, 7, 6.5)  # API -> Microservices
    draw_arrow(ax, 5, 6, 5, 5)      # API -> LLM Orchestrator
    draw_arrow(ax, 5, 4, 5, 3.5)    # Orchestrator -> Models
    draw_arrow(ax, 5, 3.5, 3, 3)    # Orchestrator -> Model A
    draw_arrow(ax, 5, 3.5, 7, 3)    # Orchestrator -> Model B
    draw_arrow(ax, 8, 3, 9, 3.5)    # Models -> Database
    draw_arrow(ax, 8, 2.5, 9, 2)    # Models -> Cache
    draw_arrow(ax, 7, 5.5, 9, 3.5)  # Microservices -> Database
    draw_arrow(ax, 3, 4.5, 4, 4.5)  # CI/CD -> LLM

    # Configure plot
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')

    # Add title
    ax.set_title(
        'High-Throughput LLM Application Architecture',
        fontsize=16,
        pad=20)

    # Add legend for components
    add_legend(ax, colors)

    # Save the diagram
    plt.tight_layout()
    plt.savefig('llm_architecture.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Architecture diagram saved as 'llm_architecture.png'")


def draw_box(ax, x, y, width, height, color, label):
    """Draw a component box with label"""
    rect = patches.Rectangle(
        (x,
         y),
        width,
        height,
        linewidth=1,
        edgecolor='black',
        facecolor=color,
        alpha=0.7)
    ax.add_patch(rect)
    ax.text(
        x + width / 2,
        y + height / 2,
        label,
        ha='center',
        va='center',
        color='black',
        fontweight='bold')


def draw_arrow(ax, x1, y1, x2, y2):
    """Draw an arrow between components"""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color="black", linewidth=1.5))


def add_legend(ax, colors):
    """Add legend to diagram"""
    legend_elements = []
    for key, color in colors.items():
        legend_elements.append(
            patches.Patch(
                facecolor=color,
                alpha=0.7,
                label=key.capitalize()))
    ax.legend(
        handles=legend_elements,
        loc='upper right',
        bbox_to_anchor=(
            1.1,
            0.9))


if __name__ == "__main__":
    generate_architecture_diagram()
