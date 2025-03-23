import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.gridspec import GridSpec


def generate_performance_dashboard():
    # Set the style
    plt.style.use('dark_background')
    sns.set_style("darkgrid")

    # Create figure with grid
    fig = plt.figure(figsize=(14, 8))
    gs = GridSpec(2, 3, figure=fig)

    # Create axes for different charts
    ax1 = fig.add_subplot(gs[0, 0])  # Throughput
    ax2 = fig.add_subplot(gs[0, 1])  # Latency
    ax3 = fig.add_subplot(gs[0, 2])  # Accuracy
    ax4 = fig.add_subplot(gs[1, :2])  # Timeline
    ax5 = fig.add_subplot(gs[1, 2])  # Resource usage

    # Generate sample data
    # Dates for X-axis
    dates = pd.date_range(start='2023-01-01', periods=14, freq='D')

    # 1. Throughput Metrics
    before_throughput = 200 + np.random.normal(0, 10, size=7)
    after_throughput = 350 + np.random.normal(0, 15, size=7)
    throughput = np.concatenate([before_throughput, after_throughput])

    ax1.plot(dates, throughput, marker='o', linewidth=2, color='#2ecc71')
    ax1.axvline(
        pd.Timestamp('2023-01-08'),
        color='red',
        linestyle='--',
        alpha=0.7)
    ax1.fill_between(dates[:7], before_throughput, alpha=0.3, color='#2ecc71')
    ax1.fill_between(dates[7:], after_throughput, alpha=0.3, color='#2ecc71')
    ax1.set_title('Requests Per Minute')
    ax1.set_ylim(bottom=0)
    ax1.set_xticks([dates[0], dates[7], dates[-1]])
    ax1.set_xticklabels(['Jan 1', 'Jan 8', 'Jan 14'])
    ax1.text(
        dates[3],
        max(before_throughput),
        'Before Optimization',
        ha='center')
    ax1.text(
        dates[10],
        max(after_throughput),
        'After Optimization',
        ha='center')

    # 2. Latency Metrics
    before_latency = 450 + np.random.normal(0, 30, size=7)
    after_latency = 180 + np.random.normal(0, 20, size=7)
    latency = np.concatenate([before_latency, after_latency])

    ax2.plot(dates, latency, marker='o', linewidth=2, color='#3498db')
    ax2.axvline(
        pd.Timestamp('2023-01-08'),
        color='red',
        linestyle='--',
        alpha=0.7)
    ax2.fill_between(dates[:7], before_latency, alpha=0.3, color='#3498db')
    ax2.fill_between(dates[7:], after_latency, alpha=0.3, color='#3498db')
    ax2.set_title('Response Time (ms)')
    ax2.set_xticks([dates[0], dates[7], dates[-1]])
    ax2.set_xticklabels(['Jan 1', 'Jan 8', 'Jan 14'])
    ax2.set_ylim(bottom=0)

    # 3. Accuracy Metrics
    accuracy_data = {
        'Model': ['Baseline', 'Optimized'],
        'Precision': [0.82, 0.91],
        'Recall': [0.79, 0.89],
        'F1 Score': [0.80, 0.90]
    }

    df_accuracy = pd.DataFrame(accuracy_data)
    df_melted = pd.melt(
        df_accuracy,
        id_vars=['Model'],
        var_name='Metric',
        value_name='Score')

    sns.barplot(x='Metric', y='Score', hue='Model', data=df_melted, ax=ax3)
    ax3.set_title('Model Performance Metrics')
    ax3.set_ylim(0, 1)
    ax3.legend(loc='lower right')

    # 4. Timeline of Improvements
    improvements = {
        'Date': [
            pd.Timestamp('2023-01-03'),
            pd.Timestamp('2023-01-08'),
            pd.Timestamp('2023-01-12')],
        'Event': [
            'Baseline',
            'Optimization',
            'Fine-tuning'],
        'Position': [
            1,
            2,
            3]}

    ax4.scatter(
        improvements['Date'],
        [1] * 3,
        s=120,
        color=[
            '#e74c3c',
            '#2ecc71',
            '#3498db'])
    for i, txt in enumerate(improvements['Event']):
        ax4.annotate(
            txt, (improvements['Date'][i], 1.1), xytext=(
                0, 10), textcoords='offset points', ha='center', fontsize=12, bbox=dict(
                boxstyle="round,pad=0.3", fc='#34495e', alpha=0.7))

    # Add improvement details
    details = [
        'Initial deployment\n82% accuracy\n450ms latency',
        'Architecture optimization\n91% accuracy\n180ms latency',
        'Model fine-tuning\n95% uptime\n59% resource usage'
    ]

    for i, detail in enumerate(details):
        ax4.annotate(detail, (improvements['Date'][i], 0.9),
                     xytext=(0, -30), textcoords='offset points',
                     ha='center', va='top', fontsize=9,
                     bbox=dict(boxstyle="round,pad=0.3", fc='#2c3e50', alpha=0.7))

    ax4.axhline(y=1, color='gray', linestyle='-', alpha=0.3)
    ax4.set_title('Project Milestones and Improvements')
    ax4.set_ylim(0.5, 1.5)
    ax4.set_xlim(dates[0], dates[-1])
    ax4.set_yticks([])

    # 5. Resource Usage Pie Chart
    resource_data = [59, 41]  # Used, Available
    labels = ['In Use', 'Available']
    colors = ['#3498db', '#2c3e50']
    explode = (0.1, 0)

    ax5.pie(resource_data, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    ax5.set_title('Resource Utilization')

    # Adjust layout
    plt.suptitle('System Performance Dashboard', fontsize=16, y=0.98)
    plt.figtext(
        0.5,
        0.01,
        'Optimized LLM Application Performance Metrics',
        ha='center',
        fontsize=12)
    plt.figtext(
        0.99,
        0.01,
        'After optimization: +75% throughput, -60% latency',
        ha='right',
        fontsize=10,
        color='#2ecc71')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('performance_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Performance dashboard saved as 'performance_dashboard.png'")


if __name__ == "__main__":
    generate_performance_dashboard()
