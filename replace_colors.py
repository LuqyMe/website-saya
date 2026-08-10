import os

replacements = {
    '#030305': '#2b0f54',
    '#07080e': '#38156e',
    '#090a10': '#38156e',
    'rgba(10, 12, 22, 0.85)': 'rgba(43, 15, 84, 0.85)',
    'rgba(5, 5, 8, 0.9)': 'rgba(43, 15, 84, 0.9)',
    '#050508': '#1e0a3c',
    '#121420': '#441b82',
    'rgba(3, 4, 8, 0.95)': 'rgba(20, 7, 40, 0.95)',
    '#00f0ff': '#ffd460',
    'rgba(0, 240, 255': 'rgba(255, 212, 96',
    'cyan-400': 'yellow-400',
    '#ff0077': '#ff6f61',
    '#ff0055': '#ff6f61',
    'rgba(255, 0, 119': 'rgba(255, 111, 97',
    'pink-500': 'orange-500',
    'pink-400': 'orange-400',
    '#a855f7': '#ab2e91',
    'purple-400': 'fuchsia-600'
}

for filename in ['index.html', 'karya.html', 'style.css']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Colors updated successfully!")
