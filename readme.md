## requerimientos
python 3.10

# crea un ambiente
>py -3.10 -m venv venv
# o tambien
>python -m venv venv

# activalo en windows
>venv\Scripts\activate.bat
# en linux es más facil pero no me acuerdo
>activate

# instala
>pip install --upgrade pip
>pip install -r requeriments.txt

# crea un .env con las variables a nivel de .env.example
# corre django con
>python manage.py runserver