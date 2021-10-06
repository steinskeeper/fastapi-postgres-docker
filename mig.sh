echo "Enter the Migration File name"
read name
docker exec -it {container name} alembic revision --autogenerate -m "$name"
echo "Migration File Created. Don't Forget to Commit it"