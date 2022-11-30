# build_files.sh
pip install psycopg2
pip install psycopg2-binary
pip install -r requirements.txt
python3.6 manage.py collectstatic
