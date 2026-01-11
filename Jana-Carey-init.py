import os

def create_project_structure(base_path):
    # Список папок, которые обычно нужны в проекте
    folders = ['src', 'tests', 'docs', 'data']
    
    # Список базовых файлов
    files = {
        'README.md': '# My New Project\n\nProject description goes here.',
        '.gitignore': '__pycache__/\n.env\n.vscode/',
        'requirements.txt': 'requests==2.31.0\npytest==7.4.0',
        'src/main.py': 'def main():\n    print("Hello from project structure!")\n\nif __name__ == "__main__":\n    main()'
    }

    # Создаем папки
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"[+] Created folder: {path}")

    # Создаем файлы
    for file_path, content in files.items():
        full_path = os.path.join(base_path, file_path)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[+] Created file: {full_path}")

if __name__ == "__main__":
    print("🚀 Starting project initialization...")
    create_project_structure('.')
    print("✅ Done! Happy coding.")
