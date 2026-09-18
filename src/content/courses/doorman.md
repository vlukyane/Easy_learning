---
section: ai
order: 6
title: Doorman
skill: Защита от prompt injection в недоверенном пользовательском контенте.
goal: Attack success rate падает с высокого baseline до низкого после слоёв защиты; false-positive на чистых резюме остаётся низким.
metric: ASR по классам атак до / после · FP на чистых
pilot: Скринер резюме + red-team корпус 30–60 инъекций разных классов.
stack:
  - Python 3.12
  - Claude API
  - Pydantic
projectDir: projects/doorman
dod:
  - Есть уязвимый baseline и защищённая версия.
  - Есть корпус атак и таблица ASR по классам, до и после.
  - False-positive на чистых резюме измерен и низок.
---

Рекрутинг-агент, который выживает при инъекции, спрятанной внутри резюме кандидата.
