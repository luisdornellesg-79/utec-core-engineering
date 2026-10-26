# Crear la carpeta del módulo si no existe
mkdir -p python_advanced/file_handling
# Crear el archivo read_file.py desde cero con su contenido exacto
cat << 'EOF' > python_advanced/file_handling/read_file.py
#!/usr/bin/env python3

"""Módulo que contiene la función read_file."""


def read_file(filename=""):
    """Lee un archivo de texto en UTF-8 y lo imprime en stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
EOF

# Darle permisos de ejecución al archivo
chmod +x python_advanced/file_handling/read_file.py
# Crear una copia en la raíz del repositorio (por si el validador automático busca el archivo ahí)
cp python_advanced/file_handling/read_file.py .
chmod +x read_file.py
# Crear el archivo de texto de prueba
cat << 'EOF' > my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
EOF

# Crear el script de prueba main.py
cat << 'EOF' > main.py
#!/usr/bin/env python3

read_file = __import__('read_file').read_file

read_file("my_file_0.txt")
EOF

# Dar permisos y ejecutar main.py
chmod +x main.py
./main.py
pycodestyle python_advanced/file_handling/read_file.py
git add .
git commit -m "Add read_file.py from scratch for File I/O module"
git push origin master
# 1. Asegúrate de estar dentro de tu carpeta del repositorio utec-core-engineering 
# (si no la tienes clonada aquí, inicialízala o muévete a ella):
cd ~
# Si ya tienes la carpeta clonada, entra en ella:
cd utec-core-engineering
# (Si por alguna razón la carpeta no existe aquí en este sandbox nuevo, inicializa git aquí mismo):
# git init
# git remote add origin https://github.com/luisdornellesg-79/utec-core-engineering.git
# 2. Asegúrate de que los archivos estén en la ruta correcta: python_advanced/file_handling/read_file.py
mkdir -p python_advanced/file_handling
# (Copia tu archivo read_file.py ahí si hiciste los cambios fuera)
# 3. Añade, haz commit y empuja a tu repositorio remoto
git add .
git commit -m "Complete exercise 0. Read file"
git push -u origin master
# 1. Inicializar Git en esta carpeta
git init
# 2. Configurar tu identidad (ajusta tus datos si es necesario)
git config --global user.email "luis.dornelles.g@gmail.com"
git config --global user.name "luisdornellesg-79"
# 3. Vincular con tu repositorio remoto de GitHub
git remote add origin https://github.com/luisdornellesg-79/utec-core-engineering.git
# 4. Asegurarnos de que el archivo read_file.py esté en la ruta correcta
mkdir -p python_advanced/file_handling
# (Si ya lo habías creado, muévelo o créalo aquí mismo con el contenido correcto)
cat << 'EOF' > python_advanced/file_handling/read_file.py
#!/usr/bin/env python3

"""Módulo que contiene la función read_file."""


def read_file(filename=""):
    """Lee un archivo de texto en UTF-8 y lo imprime en stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
EOF

chmod +x python_advanced/file_handling/read_file.py
# 5. Añadir, hacer commit y enviar los cambios a GitHub
