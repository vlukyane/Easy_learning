---
section: web
order: 4
title: React
skill: Компоненты, props и state, хуки, когда мемоизация вредна.
goal: Доска как SPA — список из state, контролируемый ввод, хуки по правилам, без memo «на всякий случай».
metric: UI = f(state), без правок DOM руками
pilot: Та же доска на React. Проект создаётся Vite-шаблоном в projects/web/react.
stack:
  - React
  - JSX
  - Vite
projectDir: projects/web/react
dod:
  - Карточки рендерятся из массива state, не из document.createElement.
  - Нет лишнего React.memo на каждом компоненте.
---

JavaScript + JSX. TypeScript — не в этом курсе.
