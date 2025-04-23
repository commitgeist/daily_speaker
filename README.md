# 🧠 Daily Speaker API – Estudo de DDD com Flask

Este projeto é uma **API simples** feita em **Python + Flask**, com o objetivo de **praticar Domain-Driven Design (DDD)** na vida real. Aqui, a aplicação simula as falas de um desenvolvedor durante uma **daily meeting** (scrum), com base em suas tarefas realizadas, planejadas e bloqueios.

> Não usamos banco de dados. Tudo roda em memória.
> O foco é **aprender a organizar o código por camadas**, respeitando separação de responsabilidades.

---

## 💡 Objetivo

Aprender como dividir um projeto Flask usando os conceitos de DDD na prática:

- Onde colocar as regras de negócio?
- O que é um caso de uso?
- Por que separar lógica da rota?
- Como deixar o código testável, escalável e sem gambiarra?

---
## 🗂️ Estrutura do Projeto

```text
daily_speaker/
├── api/
│   └── routes.py
├── application/
│   └── use_cases/
│       └── generate_daily_talk.py
├── domain/
│   ├── entities/
│   │   └── developer.py
│   └── services/
│       └── talk_generator.py
├── infrastructure/
│   └── (vazio por enquanto)
├── schemas/
│   └── talk_schema.py
├── main.py

---
## 🧱 Camadas e Responsabilidades

| Camada            | Responsabilidade                                                              |
|-------------------|-------------------------------------------------------------------------------|
| `domain/`         | **Regras de negócio puras**: lógica que gera a fala do dev                    |
| `application/`    | **Use cases**: orquestram o que o sistema faz, usando o domínio               |
| `api/`            | **Entrada HTTP**: recebe requisição, chama o use case, responde               |
| `schemas/`        | **Validação de dados**: entrada e saída usando Pydantic                       |
| `infrastructure/` | **Integrações externas** (vazio por enquanto): banco, APIs de terceiros, etc. |

---