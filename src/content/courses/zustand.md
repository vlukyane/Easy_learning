---
section: web
order: 6
title: Zustand
skill: Клиентский стор вне дерева, селекторы, persist.
goal: Карточки в Zustand; без прокидывания массива через четыре уровня props; persist в localStorage; селектор колонки не ререндерит соседей зря.
metric: persist + selector
pilot: Миграция доски на стор. Код в projects/web/zustand или в том же Vite-приложении.
stack:
  - Zustand
  - React
  - persist
projectDir: projects/web/zustand
dod:
  - Стор переживает F5.
  - Колонка подписана на свой срез, не на весь store.
---

Не Context на каждый чих и не Redux «потому что так принято».
