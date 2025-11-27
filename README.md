# Quadro de Solicitações e Estante Virtual de Achados (QS EVA)

## Integrantes
- **Gabriel Albino Oliveira**
- **Giordanni Gomes Maciel**
- **João Gustavo Alves da Silva**
- **Samuel Andrey Teixeira Rigo**

---

## Problema

### Visão do interessado
Pessoas encontram objetos perdidos no interior de uma instituição e desejam delegar a incumbência a um **Setor de Achados e Perdidos (SAP)**. Há também pessoas que procuram no SAP por objetos de sua posse que foram perdidos.

Existem dois tipos de interessados:

- **Colaborador**: quem entrega o objeto ao SAP.
- **Solicitante**: quem solicita a devolução de um objeto ao SAP.

Ambos têm o mesmo objetivo final: **a devolução dos objetos perdidos aos seus devidos donos**.

---

### Visão do cliente

Para a instituição cliente, é necessário atender eficientemente aos interessados. Isso envolve:

#### Aspectos práticos:
- Facilitar a colaboração e solicitação de objetos;
- Integração entre diferentes SAP’s de uma mesma instituição.

#### Aspectos de segurança:
- Controle no fluxo de objetos;
- Atendimento prévio para registro (coleta de dados relacionados ao objeto);
- Transparência entre os envolvidos (interessado e funcionário).

---

## Solução

A **Estante Virtual de Achados (EVA)** funciona como um catálogo digital onde são registrados os objetos achados e seus históricos.

Os colaboradores e solicitantes **não têm acesso direto** ao sistema, mas interagem com ele **por meio de um funcionário (usuário privilegiado)**.

### Fluxo de Interações

#### 1. Interessado colabora um objeto
1. Encontra o objeto;  
2. Entrega-o a um funcionário em um SAP;  
3. O funcionário realiza perguntas essenciais;  
4. O objeto é registrado na EVA.

#### 2. Interessado solicita um objeto
1. Abre uma solicitação de devolução;  
2. O funcionário pesquisa o objeto descrito na EVA.

##### Se houver resultados:
- O funcionário envia ao solicitante os possíveis objetos encontrados;
- O solicitante confirma qual deles é o seu.

##### Se o objeto for identificado:
O funcionário autoriza a devolução. O solicitante recebe um **relatório confidencial**, contendo:

- Código do objeto;  
- SAP’s onde pode realizar a devolução;  
- Horário de funcionamento dos SAP’s;  
- **Chave de devolução** (essencial para efetivar a retirada).

> Por segurança, o relatório é enviado apenas ao solicitante autorizado.

##### Caso o objeto não seja identificado:
- A solicitação permanece **em aberto**.

### Políticas
- O sistema registra **todas as interações** dos usuários.  
- Todos os objetos ficam registrados na EVA, inclusive os já devolvidos.  
- O sistema oferece **ferramentas de busca avançada por IA**.  
- A instituição **não se envolve juridicamente** em conflitos sobre devolução.  
  - Exemplo: se X solicita um objeto já devolvido a Y, o sistema apenas auxilia na comunicação, sem intervir no conflito.

---

## Usuários

### Solicitante
- Abre solicitações de devolução.

### Funcionário (Usuário Privilegiado)
- Atua em nome da instituição para atender colaboradores e solicitantes.

---

## Funcionalidades

### Funcionalidades de Usuário Privilegiado
- Pesquisa na EVA com filtros (data/hora, local, status);
- Catalogar novo objeto;
- Cadastro de usuário;
- Atender/autorizar solicitação;
- Efetivar devolução.

### Funcionalidades de Usuário Comum
- Solicitação de objeto.
