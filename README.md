# KMDB

KMDB é uma API de gerenciamento de filmes e reviews.

Deploy da API: https://kmdb-guilopreti.herokuapp.com/api/

## Endpoints do serviço:

POST /users/register/ - Cadastro de um usuário.

POST /users/login/ - Retorna um token de autorização validando email e senha.

GET /users - Lista todos os usuários, necessário estar logado.

GET /users/<user_id>/  - Busca um usuário, necessário estar logado.

POST /movies/ - Cadastro de um filme, necessário estar logado.

GET /movies/ - Lista todos os filmes.

GET /movies/<movie_id>/ - Busca um filme.

PATCH /movies/<movie_id>/ - Atualiza um filme, necessário estar logado.

DELETE /movies/<movie_id>/ - Deleta um filme, necessário estar logado.

POST /movies/<movie_id>/reviews/ - Cria uma review, necessário estar logado.

GET /movies/<movie_id>/reviews/ - Lista todos os reviews de um filme.

GET /reviews/ - Lista todos os reviews.

DELETE /reviews/<review_id>/ - Deleta um review, necessário estar logado e ser dono do review ou ser um super user.
