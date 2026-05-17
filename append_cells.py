import json
import os

notebook_path = r'c:\Users\PMLS\Desktop\Cases_FYP\CASE_4.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

markdown_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Visualization of Results\n",
        "The following cells generate graphical representations of the model comparisons, top feature importances, and meta-learner internal weight influences based on the earlier evaluations."
    ]
}

code_cell_1 = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')\n",
        "\n",
        "sns.set_theme(style=\"whitegrid\")\n",
        "\n",
        "# 1. Model Comparison Chart\n",
        "data = {\n",
        "    'Model': ['Naive Bayes', 'KNN', 'Decision Tree', 'Random Forest', 'XGBoost', 'Stacked Ensemble'],\n",
        "    'Macro F1 (Unbalanced)': [0.090479, 0.906522, 0.924598, 0.939648, 0.927382, 0.937463],\n",
        "    'MCC (Unbalanced)': [0.060545, 0.936173, 0.943601, 0.944283, 0.944558, 0.945242],\n",
        "    'Macro F1 (Balanced)': [0.089902, 0.885330, 0.923476, 0.922185, 0.908210, 0.920611],\n",
        "    'MCC (Balanced)': [0.059745, 0.932726, 0.943626, 0.943848, 0.943531, 0.944662]\n",
        "}\n",
        "df = pd.DataFrame(data)\n",
        "df_melt = df.melt(id_vars=['Model'], var_name='Metric', value_name='Score')\n",
        "\n",
        "plt.figure(figsize=(14, 7))\n",
        "ax = sns.barplot(data=df_melt, x='Model', y='Score', hue='Metric', palette='viridis')\n",
        "plt.title(\"CASE 4: Model Evaluation (Balanced vs Unbalanced Pools)\", fontsize=16, fontweight='bold', pad=15)\n",
        "plt.ylabel(\"Performance Score\", fontsize=12)\n",
        "plt.xlabel(\"Algorithm\", fontsize=12)\n",
        "plt.xticks(rotation=0, fontsize=11)\n",
        "plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True, shadow=True)\n",
        "plt.ylim(0, 1.05)\n",
        "\n",
        "for p in ax.patches:\n",
        "    if p.get_height() > 0.1:\n",
        "        ax.annotate(format(p.get_height(), '.3f'), \n",
        "                    (p.get_x() + p.get_width() / 2., p.get_height()), \n",
        "                    ha = 'center', va = 'center', \n",
        "                    xytext = (0, 9), \n",
        "                    textcoords = 'offset points',\n",
        "                    fontsize=8, rotation=90)\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()\n"
    ]
}

code_cell_2 = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# 2. Top Features Chart\n",
        "features = ['act_data_pkt_fwd', 'Subflow Bwd Bytes', 'Destination Port', 'Flow Packets/s', 'Bwd Header Length', 'Flow Bytes/s']\n",
        "importance = [0.062693, 0.046837, 0.039990, 0.035798, 0.029482, 0.027294]\n",
        "\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.barplot(x=importance, y=features, palette='magma', hue=features, legend=False)\n",
        "plt.title(\"Stacked Ensemble: Top Feature Influences\", fontsize=16, fontweight='bold')\n",
        "plt.xlabel(\"Gini Importance Score\", fontsize=12)\n",
        "plt.ylabel(\"Network Feature\", fontsize=12)\n",
        "plt.tight_layout()\n",
        "plt.show()\n"
    ]
}

code_cell_3 = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# 3. Meta Learner Weights Chart\n",
        "weights = {'KNN Base': 0.1998, 'Decision Tree Base': 0.2172, 'Random Forest Base': 0.1306, 'XGBoost Base': 0.2560}\n",
        "plt.figure(figsize=(8, 8))\n",
        "colors = sns.color_palette('husl', len(weights))\n",
        "explode = (0, 0, 0, 0.05)  # slightly explode the biggest influence (XGBoost)\n",
        "\n",
        "plt.pie(weights.values(), labels=weights.keys(), autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True, textprops={'fontsize': 12, 'weight': 'bold'})\n",
        "plt.title(\"Meta-Learner Internal Weight Allocation\", fontsize=16, fontweight='bold', pad=20)\n",
        "plt.tight_layout()\n",
        "plt.show()\n"
    ]
}

nb['cells'].extend([markdown_cell, code_cell_1, code_cell_2, code_cell_3])

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Cells appended successfully to CASE_4.ipynb!")
