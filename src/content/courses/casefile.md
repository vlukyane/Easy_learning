---
section: ai
order: 2
title: Casefile
skill: Оркестрация агентов с типизированными хендоффами, потолком стоимости и человеком на необратимом действии.
goal: 0 выплат без human-approval, 0 превышений cost ceiling, 0 ошибок парсинга хендоффа; известна средняя стоимость заявки.
metric: 0 payouts w/o approval · ¢ / claim
pilot: Триаж синтетических insurance claims — intake, classifier, fraud, assessor, HITL на выплате.
stack:
  - Python 3.12
  - Pydantic
  - Claude API
  - ручной tool-loop
projectDir: projects/casefile
dod:
  - "Заявка проходит весь путь; трасса видна."
  - "Выплата выше порога физически невозможна без approval."
  - "Есть число: средняя стоимость и доля заявок, упёршихся в потолок."
---

Триаж страховых претензий с типизированными хендоффами, потолком стоимости и человеком перед любой выплатой.
