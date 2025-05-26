# 📖 Simple Bible Mk2

**Simple Bible Mk2** é um projeto web feito com Django que tem como objetivo ajudar pessoas a encontrarem consolo e direção na Palavra de Deus. O sistema apresenta versículos bíblicos organizados por temas, como ansiedade, medo, solidão e outros sentimentos comuns do cotidiano.

> 🕊️ *"Para quando você estiver buscando conforto nas Escrituras."*

---

## 🚀 Funcionalidades

- Listagem de temas bíblicos na página inicial
- Visualização de versículos relacionados a cada tema
- Design leve, responsivo e confortável para leitura
- Mensagens de alerta estilizadas para feedback ao usuário
- Estrutura preparada para adicionar cadastro, login e administração dos conteúdos

---

## 💻 Tecnologias

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3 (com variáveis CSS), Django Templates
- **Banco de Dados:** MySQL
- **Deploy:** Ainda não realizado

---

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/DRBenedetti/simple-bible-mk2.git
   cd simple-bible-mk2
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados MySQL em `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'nome_do_banco',
           'USER': 'seu_usuario',
           'PASSWORD': 'sua_senha',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. Rode as migrações:
   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

7. Acesse no navegador:
   ```
   http://127.0.0.1:8000/
   ```

---

## 🧩 Estrutura do Projeto

```
simple-bible-mk2/
├── home/
│   ├── models.py       # Modelos de Tema e Versículo
│   ├── views.py        # Lógica das páginas
│   ├── urls.py         # Rotas locais
│   └── templates/      # Templates HTML
├── static/             # Arquivos CSS e imagens
├── simple_bible/       # Configurações do projeto Django
└── manage.py
```

---

## 📌 TODO

- [ ] Sistema de autenticação (login e cadastro)
- [ ] Área de administração customizada
- [ ] Adicionar painel para enviar novos versículos
- [ ] Deploy completo com banco de dados online
- [ ] Versão em inglês e espanhol

---

## 📬 Contato

Criado e mantido por **Diogo Benedetti**  
🔗 [GitHub](https://github.com/DRBenedetti)

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

