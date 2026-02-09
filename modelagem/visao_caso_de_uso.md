# CDU 001 - Login

Atores: Funcionário / Interessado

Descrição: o usuário faz login no QSEVA para ter acesso às suas funcionalidades.

Fluxo principal:

1. O usuário preenche os campos (email, senha, perfil);
2. O usuário clica em “Entrar”;
3. O usuário é redirecionado à página inicial respectiva a seu perfil.

Fluxo alternativo (2) - credenciais inválidas:

1. O sistema mostra a mensagem de erro: “Senha ou Email inválidos”;
2. O CDU volta à etapa 1.

Fluxo alternativo (3)

1. O sistema mostra a mensagem de erro: “Você não tem permissão para entrar como “perfil”. Tente outro”;
2. O CDU volta à etapa 1.

Pré-condições:

O usuário deve estar cadastrado.

Pós-condições:

O usuário deve ter sessão ativa.

# CDU 002 - Registrar Objeto

Atores: Funcionário

Descrição: O funcionário registra um objeto entregue no QSEVA

Fluxo principal:

1. Na tela inicial o funcionário clica em "Adicionar objeto"
2. O sistema redireciona o funcionário para tela de registro de objeto
3. Preencher os campos de descrição e data
4. Clica em "registrar objeto"
5. Aparece mensagem de sucesso...

Fluxo alternativo - (2):

1. O sistema mostra uma mensagem de erro “data selecionada inválida”
2. O CDU volta ao passo 3

Pré condição:

O funcionário deve estar logado

Pós condição:

O objeto é adicionado ao EVA.

# CDU 003 - Registrar usuário

Atores: Funcionário

Descrição: O funcionário registra um novo usuário no sistema

Fluxo principal:

1. Na tela inicial o funcionário clica em "Registrar usuário"
2. O sistema redireciona o funcionário para tela de criação de usuário
3. Preencher os campos de nome, email, telefone, senha e as permissões (interessado ou funcionário)
4. Clica em "Registrar usuário"
5. Aparece mensagem de sucesso...

Fluxo alternativo - (2):

1. O sistema mostra uma mensagem de erro “email já cadastrado”
2. O CDU volta ao passo 3

Fluxo alternativo - (3):

1. O sistema mostra uma mensagem de erro “usuário não pode possuir ambas permissões”
2. O CDU volta ao passo 3

Pré condição:

O funcionário deve estar logado

Pós condição:

Um novo usuário é adicionado ao EVA.
