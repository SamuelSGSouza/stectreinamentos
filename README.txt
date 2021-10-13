O presente projeto foi desenvolvido para execução e entrega como trabalho por contrato.
Trata-se de um site desenvolvido em bootstrap para linguagem front-end e django como linguagem back-end.

O projeto final pode ser encontrado em www.stectreinamentos.com.br

O projeto possui 4 páginas no front-end (incluindo a django admin) e 4 serviços principais no back-end

As páginas são: 

	- index: Página inicial para apresentação do produto, videos e etc (pagina de chamada)
	- django-admin
	- email_clientes: pagina para receber uma mensagem e assunto e redirecionar essas informações para o servidor.
	- login: pagina de login caso não esteja logado no django-admin


Os serviços no back-end são:

	- atualização de partes da página através da django-admin: Algumas partes da página se tornaram alteráveis através da django-admin. O preço antigo, preço atualizado,
video de apresentação da pagina, videos de depoimento e seus respectivos titulos são todas seções da página que podem ser modificadas a partir da django-admin, forcendo assim maior controle
à usuária.

	- cadastro de interessados: Na página de index há uma seção para que um usuário se cadastre para receber emails e atualizações dos cursos oferecidos na stectreinamentos. Ao inserir os
dados e clicar em se cadastrar, os dados do usuário são inseridos em um banco de dados e ficam armazenados para usos futuros.

	- Email automatico: Ao clicar no botao de cadastro na pagina de index, ao mesmo tempo que cadastro é realizado um email de confirmação é enviado para o endereço informado.

	- Envio automatico multiplo: Na pagina email_clientes o assunto e a mensagem informadas vão para o servidor e enviam o email para cada cliente cadastrado no banco de dados