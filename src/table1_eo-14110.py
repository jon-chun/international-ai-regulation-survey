import matplotlib.pyplot as plt
import numpy as np

data = [
    ['H\nI\nG\nH', 'Federal use of AI', '29 requirements\n40 entities', 'OMB, OPM, CFO, GSA, etc.'],
    ['H\nI\nG\nH', 'Safety and security', '27 requirements\n30 entities', 'NIST, DOE, DOC, SRMA,\nTreasury, DHS, DOD, etc.'],
    ['H\nI\nG\nH', 'Innovation and competition', '21 requirements\n10 entities', 'DOS, DHS, DOL, NSF, USPTO,\nHHS, VA, DOE, PCAST, OSTP+'],
    ['M\nE\nD\nI\nU\nM', 'Consideration of AI bias and\ncivil rights', '9 requirements\n8 entities', 'DOJ, OPM, HHS, USDA, DOL,\nHUD, DHS, OSTP'],
    ['M\nE\nD\nI\nU\nM', 'Consumer protection', '9 requirements\n5 entities', 'HHS, DOT, ED, DOD, VA'],
    ['M\nE\nD\nI\nU\nM', 'Privacy', '8 requirements\n9 entities', 'OMB, NIST, NSF, FPC, ICSP,\nDOJ, CEA, OSTP, DOE'],
    ['L\nO\nW', 'International leadership', '6 requirements\n7 entities', 'DOC, DOS, USAID, DHS, NIST,\nDOE, NSF'],
    ['L\nO\nW', 'Worker support', '4 requirements\n2 entities', 'CEA, DOL']
]

fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=data,
                 colLabels=['Relevance', 'Policy Area', 'Requirements/Entities', 'Federal Entities'],
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 1.5)

# Style the table
for i in range(len(data) + 1):
    for j in range(4):
        cell = table[i, j]
        cell.set_edgecolor('black')
        cell.set_linewidth(1)
        if i == 0:  # Header row
            cell.set_text_props(weight='bold')
            cell.set_facecolor('#f0f0f0')
        else:
            cell.set_facecolor('white')
        
        # Align text
        if j == 0:  # Relevance column
            cell.set_text_props(ha='center', va='center')
        elif j == 1:  # Policy Area column
            cell.set_text_props(ha='left', va='center')
        else:
            cell.set_text_props(ha='left', va='center')

# Remove cell padding
table.PAD = 0.02

plt.title('', pad=0)  # Remove title
plt.tight_layout(pad=0)
plt.savefig('ai_policy_table.png', dpi=300, bbox_inches='tight', pad_inches=0)
plt.close()

print("Table saved as 'ai_policy_table.png'")