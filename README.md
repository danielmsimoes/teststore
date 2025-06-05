# Projeto de Automação de Testes com Selenium

Este projeto tem como objetivo automatizar testes de funcionalidades básicas utilizando Selenium WebDriver com Python.

## Descrição

Atualmente, o foco é criar scripts de automação para realizar login em sites de teste, garantindo que o fluxo básico de autenticação esteja funcionando corretamente.

## Tecnologias Utilizadas

- Python 3.10+
- Selenium WebDriver
- pytest
- webdriver-manager
- Google Chrome

## Como usar

1. Clone este repositório:
   git clone https://github.com/danielmsimoes/teststore.git
   cd teststore

2. Crie e ative um ambiente virtual
   python -m venv venv
   venv\Scripts\activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Execute os testes
   pytest tests/test_login.py

Estrutura do Projeto:
tests/ - Contém os scripts de teste automatizados.
requirements.txt - Lista de pacotes necessários para rodar os testes.
README.md - Documentação do projeto.

Próximos passos
Implementar testes mais complexos envolvendo fluxo de compra.
Tratar mensagens e popups inesperados no navegador para evitar falhas automáticas.
Adicionar geração automática de relatórios.

Contato
Daniel Simões – danielmsimoes77@gmail.com

Observação: Este projeto está em desenvolvimento e funcionalidades como carrinho de compras e testes E2E ainda estão em andamento.
