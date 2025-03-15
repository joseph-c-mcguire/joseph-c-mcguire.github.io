import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path
import matplotlib.gridspec as gridspec


def generate_mlops_workflow():
    # Create figure and axes
    fig = plt.figure(figsize=(14, 8))
    gs = gridspec.GridSpec(1, 1)
    ax = plt.subplot(gs[0])

    # Set background color
    fig.patch.set_facecolor('#1a1a1a')
    ax.set_facecolor('#1a1a1a')

    # Define component colors
    colors = {
        'code': '#3498db',       # Blue
        'build': '#2ecc71',      # Green
        'test': '#e74c3c',       # Red
        'deploy': '#f39c12',     # Orange
        'monitor': '#9b59b6',    # Purple
        'data': '#1abc9c',       # Teal
        'model': '#e67e22',      # Dark Orange
        'feedback': '#34495e'    # Dark Blue
    }

    # Define box positions
    boxes = {
        # CI/CD Pipeline
        'code': (1, 5, 1.5, 1),
        'build': (3.5, 5, 1.5, 1),
        'test': (6, 5, 1.5, 1),
        'deploy': (8.5, 5, 1.5, 1),
        'monitor': (11, 5, 1.5, 1),

        # ML Pipeline
        'data_prep': (1, 2, 1.5, 1),
        'train': (3.5, 2, 1.5, 1),
        'evaluate': (6, 2, 1.5, 1),
        'register': (8.5, 2, 1.5, 1),
        'serve': (11, 2, 1.5, 1)
    }

    # Draw boxes
    for name, (x, y, width, height) in boxes.items():
        if name.startswith('data'):
            color = colors['data']
            label = 'Data Preparation'
        elif name == 'train':
            color = colors['model']
            label = 'Model Training'
        elif name == 'evaluate':
            color = colors['test']
            label = 'Model Evaluation'
        elif name == 'register':
            color = colors['build']
            label = 'Model Registry'
        elif name == 'serve':
            color = colors['deploy']
            label = 'Model Serving'
        else:
            color = colors[name]
            label = name.capitalize()

        rect = mpatches.Rectangle(
            (x,
             y),
            width,
            height,
            linewidth=2,
            edgecolor='white',
            facecolor=color,
            alpha=0.7)
        ax.add_patch(rect)
        ax.text(x + width / 2, y + height / 2, label, ha='center', va='center',
                color='white', fontweight='bold', fontsize=11)

    # Add arrows for CI/CD
    for i in range(4):
        x1 = boxes['code'][0] + boxes['code'][2] + (i * 2.5)
        y1 = boxes['code'][1] + boxes['code'][3] / 2
        x2 = x1 + 1
        y2 = y1

        arrow = mpatches.FancyArrowPatch((x1, y1), (x2, y2),
                                         connectionstyle="arc3,rad=0.0",
                                         arrowstyle="-|>", color='white',
                                         linewidth=2, mutation_scale=20)
        ax.add_patch(arrow)

    # Add arrows for ML Pipeline
    for i in range(4):
        x1 = boxes['data_prep'][0] + boxes['data_prep'][2] + (i * 2.5)
        y1 = boxes['data_prep'][1] + boxes['data_prep'][3] / 2
        x2 = x1 + 1
        y2 = y1

        arrow = mpatches.FancyArrowPatch((x1, y1), (x2, y2),
                                         connectionstyle="arc3,rad=0.0",
                                         arrowstyle="-|>", color='white',
                                         linewidth=2, mutation_scale=20)
        ax.add_patch(arrow)

    # Add feedback loops
    # From monitoring to code
    arrow = mpatches.FancyArrowPatch(
        (boxes['monitor'][0] + boxes['monitor'][2] / 2, boxes['monitor'][1]),
        (boxes['code'][0] + boxes['code'][2] / 2, boxes['code'][1] + boxes['code'][3]),
        connectionstyle="arc3,rad=-0.5",
        arrowstyle="-|>", color='white', linewidth=2, linestyle='--', mutation_scale=20
    )
    ax.add_patch(arrow)

    # From model serving to data prep
    arrow = mpatches.FancyArrowPatch(
        (boxes['serve'][0] +
         boxes['serve'][2] /
         2,
         boxes['serve'][1] +
         boxes['serve'][3]),
        (boxes['data_prep'][0] +
         boxes['data_prep'][2] /
         2,
         boxes['data_prep'][1]),
        connectionstyle="arc3,rad=0.5",
        arrowstyle="-|>",
        color='white',
        linewidth=2,
        linestyle='--',
        mutation_scale=20)
    ax.add_patch(arrow)

    # Connect CI/CD to ML Pipeline
    arrow1 = mpatches.FancyArrowPatch(
        (boxes['deploy'][0] +
         boxes['deploy'][2] /
         2,
         boxes['deploy'][1]),
        (boxes['register'][0] +
         boxes['register'][2] /
         2,
         boxes['register'][1] +
         boxes['register'][3]),
        connectionstyle="arc3,rad=0.0",
        arrowstyle="-|>",
        color='white',
        linewidth=2,
        mutation_scale=20)
    ax.add_patch(arrow1)

    # Connect ML to CI/CD Pipeline
    arrow2 = mpatches.FancyArrowPatch(
        (boxes['train'][0] +
         boxes['train'][2] /
         2,
         boxes['train'][1] +
         boxes['train'][3]),
        (boxes['build'][0] +
         boxes['build'][2] /
         2,
         boxes['build'][1]),
        connectionstyle="arc3,rad=0.0",
        arrowstyle="-|>",
        color='white',
        linewidth=2,
        mutation_scale=20)
    ax.add_patch(arrow2)

    # Add labels
    plt.text(
        7,
        6.5,
        'CI/CD Pipeline',
        color='white',
        fontsize=14,
        ha='center',
        fontweight='bold')
    plt.text(
        7,
        3.5,
        'MLOps Pipeline',
        color='white',
        fontsize=14,
        ha='center',
        fontweight='bold')
    plt.text(
        3,
        4,
        'Test Artifacts',
        color='white',
        fontsize=10,
        ha='center',
        rotation=90)
    plt.text(
        9.5,
        4,
        'Deployment Triggers',
        color='white',
        fontsize=10,
        ha='center',
        rotation=90)
    plt.text(
        13,
        3.5,
        'Production Feedback',
        color='white',
        fontsize=10,
        ha='center',
        rotation=-40)
    plt.text(
        1,
        3.5,
        'Data Iteration',
        color='white',
        fontsize=10,
        ha='center',
        rotation=40)

    # Add title
    plt.suptitle('MLOps & DevOps Integration Workflow',
                 fontsize=18, color='white', y=0.98)
    plt.figtext(
        0.5,
        0.01,
        'Continuous Integration, Delivery, and Model Training Pipeline',
        ha='center',
        color='white',
        fontsize=12)

    # Add key metrics
    metrics = [
        "99.9% Uptime",
        "15 min Deployment",
        "100% Test Coverage",
        "Auto-scaling"
    ]

    for i, metric in enumerate(metrics):
        plt.figtext(0.06 + (i * 0.22),
                    0.06,
                    metric,
                    color='#2ecc71',
                    fontsize=12,
                    bbox=dict(facecolor='#34495e',
                              alpha=0.7,
                              edgecolor='none',
                              boxstyle='round,pad=0.5'))

    # Configure plot
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.set_aspect('equal')
    ax.axis('off')

    # Save the diagram
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig(
        'mlops_workflow.png',
        dpi=300,
        bbox_inches='tight',
        facecolor='#1a1a1a')
    plt.close()
    print("MLOps workflow diagram saved as 'mlops_workflow.png'")


if __name__ == "__main__":
    generate_mlops_workflow()
