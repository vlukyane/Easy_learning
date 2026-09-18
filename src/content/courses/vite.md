---
section: web
order: 5
title: Vite
skill: Dev-сервер и бандл — настройка, а не только npm run dev.
goal: В vite.config.js есть alias @, понятен import.meta.env, build и preview отдают доску.
metric: npm run build + preview
pilot: Донастройка projects/web/react. Заметки — projects/web/vite.
stack:
  - Vite
  - ESM
  - env
projectDir: projects/web/vite
dod:
  - build проходит без ошибок.
  - preview открывает рабочую доску.
  - Есть alias @ на src.
---

Тот же SPA, что в теме React. Create React App не используем.
