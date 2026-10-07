python3
git init
git add .
git commit -m "Add Python fundamentals structured_output script"
git branch -M main
git remote add origin https://github.com/luisdornellesg-79/utec-core-engineering.git
git push -u origin main
git config --global user.email "tu_correo@example.com"
git config --global user.name "luisdornellesg-79"
git config --global user.email "luis.dornelles.g@gmail.com"
git config --global user.name "luisdornellesg-79"
git add .
git commit -m "Add Python fundamentals structured_output script"
git branch -M main
git push -u origin main
git add .
git commit -m "Add Python fundamentals structured_output script"
git branch -M main
git push -u origin main
#!/usr/bin/env python3
print("Language: Python")
print("Version: 3")
print(f"Pi approx: {3.14159:.2f}")
print(f"Computation valid: {10 == 10}")
mkdir -p python_fundamentals/hello_world
cat << 'EOF' > python_fundamentals/hello_world/structured_output.py
#!/usr/bin/env python3


print("Language: Python")
print("Version: 3")
print(f"Pi approx: {3.14159:.2f}")
print(f"Computation valid: {10 == 10}")
EOF

chmod +x python_fundamentals/hello_world/structured_output.py
./python_fundamentals/hello_world/structured_output.py
