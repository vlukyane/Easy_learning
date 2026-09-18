import {
  chapterSlugFromId,
  courseStats,
  isChapterComplete,
  loadProgress,
  markChapter,
  resetCourse,
  setChecklistItem,
  setLastVisited,
} from "../lib/progress";

function currentChapterId(): string | null {
  const visit = document.querySelector<HTMLElement>("[data-visit-chapter]");
  if (!visit?.dataset.course || !visit.dataset.slug) return null;
  return `${visit.dataset.course}/${visit.dataset.slug}`;
}

function checklistId(itemId: string): string | null {
  const chapterId = currentChapterId();
  return chapterId ? `${chapterId}::${itemId}` : null;
}

function applyProgress() {
  const state = loadProgress();

  document.querySelectorAll<HTMLElement>("[data-section-card]").forEach((el) => {
    const prefixes = (el.dataset.prefixes ?? "").split(",").filter(Boolean);
    const total = Number(el.dataset.total ?? "0");
    if (!prefixes.length || !total) return;
    const completed = Object.entries(state.chapters).filter(
      ([key, value]) =>
        value.completed && prefixes.some((prefix) => key.startsWith(`${prefix}/`)),
    ).length;
    const count = el.querySelector("[data-section-count]");
    if (count) count.textContent = `${completed}/${total}`;
    const fill = el.querySelector<HTMLElement>("[data-progress-fill]");
    if (fill) fill.style.width = `${Math.round((completed / total) * 100)}%`;
  });

  document.querySelectorAll<HTMLElement>("[data-course-card]").forEach((el) => {
    const course = el.dataset.course;
    const total = Number(el.dataset.total ?? "0");
    if (!course || !total) return;
    const completed = Object.entries(state.chapters).filter(
      ([key, value]) => key.startsWith(`${course}/`) && value.completed,
    ).length;
    const count = el.querySelector("[data-course-count]");
    if (count) count.textContent = `${completed}/${total}`;
    const fill = el.querySelector<HTMLElement>("[data-progress-fill]");
    if (fill) fill.style.width = `${Math.round((completed / total) * 100)}%`;
  });

  document.querySelectorAll<HTMLElement>("[data-hub-progress]").forEach((el) => {
    const course = el.dataset.course;
    const ids = (el.dataset.ids ?? "").split(",").filter(Boolean);
    if (!course) return;
    const stats = courseStats(state, course, ids);
    const count = el.querySelector("[data-hub-count]");
    if (count) count.textContent = `${stats.completed} / ${stats.total}`;
    const fill = el.querySelector<HTMLElement>("[data-progress-fill]");
    if (fill && stats.total) {
      fill.style.width = `${Math.round((stats.completed / stats.total) * 100)}%`;
    }
    const link = document.querySelector<HTMLAnchorElement>(
      `[data-continue][data-course="${course}"]`,
    );
    if (link && stats.nextId) {
      const track = link.dataset.track ?? "ai";
      link.href = `/tracks/${track}/${course}/${chapterSlugFromId(stats.nextId)}`;
    }
  });

  document.querySelectorAll<HTMLElement>("[data-progress-bar]").forEach((el) => {
    const course = el.dataset.course;
    const total = Number(el.dataset.total ?? "0");
    if (!course || !total) return;
    const completed = Object.entries(state.chapters).filter(
      ([key, value]) => key.startsWith(`${course}/`) && value.completed,
    ).length;
    const fill = el.querySelector<HTMLElement>("[data-progress-fill]");
    if (fill) fill.style.width = `${Math.round((completed / total) * 100)}%`;
  });

  document.querySelectorAll<HTMLElement>("[data-chapter-nav] [data-chapter-id]").forEach((el) => {
    const id = el.dataset.chapterId;
    const mark = el.querySelector("[data-chapter-mark]");
    if (!id || !mark) return;
    if (isChapterComplete(state, id)) {
      mark.textContent = "✓";
      mark.classList.add("text-ok");
    }
  });

  document.querySelectorAll<HTMLInputElement>("[data-checklist-item]").forEach((input) => {
    const itemId = input.dataset.checklistItem;
    if (!itemId) return;
    const id = checklistId(itemId);
    input.checked = Boolean(id && state.checklists[id]);
  });

  document.querySelectorAll<HTMLButtonElement>("[data-complete-chapter]").forEach((btn) => {
    const id = btn.dataset.completeChapter;
    if (!id) return;
    const done = isChapterComplete(state, id);
    btn.textContent = done ? "Пройдена" : "Отметить пройденной";
    btn.classList.toggle("border-ok", done);
    btn.classList.toggle("text-ok", done);
  });
}

function bindOnce() {
  if (window.__aiLearningBound) return;
  window.__aiLearningBound = true;

  document.addEventListener("change", (event) => {
    const input = event.target;
    if (!(input instanceof HTMLInputElement) || !input.dataset.checklistItem) return;
    const id = checklistId(input.dataset.checklistItem);
    if (id) setChecklistItem(id, input.checked);
  });

  document.addEventListener("click", (event) => {
    const target = event.target;
    if (!(target instanceof Element)) return;

    const complete = target.closest<HTMLButtonElement>("[data-complete-chapter]");
    if (complete?.dataset.completeChapter) {
      const id = complete.dataset.completeChapter;
      const state = loadProgress();
      markChapter(id, !isChapterComplete(state, id));
      return;
    }

    const reset = target.closest<HTMLButtonElement>("[data-reset-course]");
    if (reset?.dataset.resetCourse) {
      if (window.confirm("Сбросить прогресс этого курса?")) {
        resetCourse(reset.dataset.resetCourse);
      }
      return;
    }

    const copy = target.closest<HTMLButtonElement>("[data-copy]");
    if (copy) {
      const root = copy.closest("[data-command]");
      const code = root?.querySelector("code")?.textContent ?? "";
      void navigator.clipboard.writeText(code.trim() + "\n").then(
        () => {
          copy.textContent = "Скопировано";
          setTimeout(() => {
            copy.textContent = "Копировать";
          }, 1200);
        },
        () => {
          copy.textContent = "Не удалось";
        },
      );
    }
  });

  window.addEventListener("keydown", (event) => {
    const target = event.target;
    if (target instanceof HTMLElement && ["INPUT", "TEXTAREA"].includes(target.tagName)) {
      return;
    }
    const footer = document.querySelector<HTMLElement>("[data-chapter-footer]");
    if (!footer) return;
    if (event.key === "ArrowRight" && footer.dataset.next) {
      window.location.href = footer.dataset.next;
    }
    if (event.key === "ArrowLeft" && footer.dataset.prev) {
      window.location.href = footer.dataset.prev;
    }
  });
}

function onPageLoad() {
  bindOnce();
  const visit = document.querySelector<HTMLElement>("[data-visit-chapter]");
  if (visit?.dataset.course && visit.dataset.slug) {
    setLastVisited(visit.dataset.course, visit.dataset.slug);
  }
  applyProgress();
}

declare global {
  interface Window {
    __aiLearningBound?: boolean;
  }
}

document.addEventListener("astro:page-load", onPageLoad);
window.addEventListener("ai-progress", applyProgress);
