psql << EOF
        CREATE USER admin WITH ENCRYPTED PASSWORD 'admin';
        ALTER ROLE admin WITH SUPERUSER;
        CREATE DATABASE "django_projects" OWNER admin ENCODING 'UTF8';
EOF
