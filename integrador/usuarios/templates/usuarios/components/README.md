# Componentes do Sistema

Esta pasta contém os componentes reutilizáveis do sistema de usuários.

## Estrutura

```
components/
├── _navbar.html      # Barra de navegação principal
├── _messages.html    # Sistema de mensagens/alerts
├── _footer.html      # Rodapé da aplicação
└── README.md         # Esta documentação
```

## Como usar

### Incluir no template base
```html
{% include 'usuarios/components/_navbar.html' %}
{% include 'usuarios/components/_messages.html' %}
{% include 'usuarios/components/_footer.html' %}
```

### Componentes disponíveis

#### _navbar.html
- Barra de navegação responsiva
- Mostra links diferentes para usuários logados/não logados
- Logo que redireciona para dashboard ou login

#### _messages.html
- Sistema de mensagens do Django
- Suporte a diferentes tipos (success, error, warning, info)
- Auto-dismiss com botão de fechar

#### _footer.html
- Rodapé da aplicação
- Informações sobre o sistema
- Links para tecnologias utilizadas

## Convenções

- Todos os arquivos de componentes começam com `_` (underscore)
- Usar classes Bootstrap para estilização
- Manter responsividade em todos os componentes
- Incluir ícones Font Awesome quando apropriado


