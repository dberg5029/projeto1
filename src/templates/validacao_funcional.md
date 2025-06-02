## Validação das Funcionalidades do Sistema

### 1. Login e Registro de Usuários

- [ ] **Registro de Novo Usuário:**
  - [ ] O usuário consegue se registrar com sucesso?
  - [ ] Os dados do usuário são salvos corretamente no banco de dados?
  - [ ] A senha é armazenada de forma segura (hashed)?
  - [ ] O tipo de usuário (normal ou gestor) é corretamente atribuído?

- [ ] **Login de Usuário Existente:**
  - [ ] O usuário consegue fazer login com credenciais válidas?
  - [ ] O sistema impede o login com credenciais inválidas?
  - [ ] A sessão do usuário é iniciada corretamente após o login?

- [ ] **Logout de Usuário:**
  - [ ] O usuário consegue fazer logout do sistema?
  - [ ] A sessão do usuário é encerrada corretamente após o logout?

### 2. Funcionalidades do Painel de Tarefas

- [ ] **Visualização de Tarefas:**
  - [ ] O usuário visualiza apenas as tarefas atribuídas a ele (se for usuário normal)?
  - [ ] O gestor visualiza todas as tarefas do seu setor?
  - [ ] As informações das tarefas (descrição, prazo, status, prioridade) são exibidas corretamente?

- [ ] **Criação de Tarefas (apenas para gestores):**
  - [ ] O gestor consegue criar novas tarefas?
  - [ ] Os dados da nova tarefa são salvos corretamente no banco de dados?
  - [ ] É possível atribuir a tarefa a um usuário específico?

- [ ] **Edição de Tarefas (apenas para gestores):**
  - [ ] O gestor consegue editar tarefas existentes?
  - [ ] As alterações são salvas corretamente no banco de dados?

- [ ] **Exclusão de Tarefas (apenas para gestores):**
  - [ ] O gestor consegue excluir tarefas?
  - [ ] A exclusão é refletida corretamente no banco de dados?

- [ ] **Atualização de Status de Tarefas (para usuários normais e gestores):**
  - [ ] O usuário designado consegue atualizar o status de suas tarefas?
  - [ ] As opções de status (pendente, em andamento, concluída, atrasada) estão corretas?
  - [ ] A atualização de status é refletida corretamente no banco de dados?

### 3. Funcionalidades de Documentos

- [ ] **Upload de Documentos:**
  - [ ] O usuário consegue fazer upload de documentos?
  - [ ] Os documentos são armazenados corretamente?
  - [ ] As informações do documento (nome, tipo, data de upload) são salvas?

- [ ] **Visualização de Documentos:**
  - [ ] O usuário consegue visualizar os documentos enviados?
  - [ ] Apenas usuários autorizados têm acesso aos documentos?

- [ ] **Download de Documentos:**
  - [ ] O usuário consegue baixar os documentos enviados?

### 4. Funcionalidades Gerais

- [ ] **Responsividade:**
  - [ ] A interface se adapta a diferentes tamanhos de tela (desktop, tablet, mobile)?

- [ ] **Usabilidade:**
  - [ ] A navegação é intuitiva?
  - [ ] As informações são apresentadas de forma clara e organizada?

- [ ] **Segurança:**
  - [ ] As senhas são tratadas de forma segura?
  - [ ] Há proteção contra ataques comuns (XSS, SQL Injection, etc.)?

- [ ] **Desempenho:**
  - [ ] O sistema responde rapidamente às ações do usuário?
  - [ ] O carregamento de páginas e dados é eficiente?

### 5. Funcionalidades Adicionais (se aplicável)

- [ ] **Notificações:**
  - [ ] O sistema envia notificações relevantes aos usuários (ex: novas tarefas, prazos próximos)?

- [ ] **Relatórios:**
  - [ ] O sistema gera relatórios úteis sobre o progresso das tarefas e documentos?

- [ ] **Integrações:**
  - [ ] O sistema se integra corretamente com outras ferramentas ou serviços, se necessário?

### Observações Gerais:

- [ ] Registrar quaisquer erros, bugs ou comportamentos inesperados encontrados durante os testes.
- [ ] Avaliar a experiência geral do usuário e sugerir melhorias de usabilidade.
- [ ] Verificar se todos os requisitos levantados na fase de análise foram atendidos.

