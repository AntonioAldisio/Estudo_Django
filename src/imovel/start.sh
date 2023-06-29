#!/bin/bash
echo "Irei esperar 60 segundos"
sleep 60

echo "Iniciando migrate"
python manage.py migrate api

if [ $? -eq 0 ]; then
    echo "Iniciando loaddata"
    python manage.py loaddata seeder.json
else
    echo "Migrate api com erro."
fi

echo "Inicaindo API"
python manage.py runserver 0.0.0.0:8000