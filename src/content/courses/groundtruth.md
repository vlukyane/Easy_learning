---
section: ai
order: 4
title: Groundtruth
skill: Эвал как гейт в CI — pull request краснеет, когда падает recall.
goal: PR, ухудшающий recall, автоматически красный; сохраняющий или улучшающий — зелёный; recall@k виден в отчёте.
metric: recall@k gate в CI
pilot: Юридический retrieval + версионированный золотой набор + GitHub Action / локальный ci_eval.
stack:
  - Python 3.12
  - pytest
  - GitHub Actions
projectDir: projects/groundtruth
dod:
  - "Есть версионированный золотой набор и baseline в репо."
  - "CI реально блокирует регресс recall (локально через ненулевой exit, в GitHub — красный job)."
---

Eval-харнесс для юридического ресёрча, который роняет pull request, когда падает recall.
