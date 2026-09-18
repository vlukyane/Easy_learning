export const STORAGE_KEY = "ai-learning-progress-v1";

export type ChapterProgress = {
  completed: boolean;
  completedAt?: string;
};

export type ProgressState = {
  version: 1;
  chapters: Record<string, ChapterProgress>;
  checklists: Record<string, boolean>;
  lastByCourse: Record<string, string>;
  lastVisited: string;
};

export const emptyProgress = (): ProgressState => ({
  version: 1,
  chapters: {},
  checklists: {},
  lastByCourse: {},
  lastVisited: "",
});

export function chapterKey(course: string, chapterSlug: string): string {
  return `${course}/${chapterSlug}`;
}

export function checklistKey(chapterId: string, itemId: string): string {
  return `${chapterId}::${itemId}`;
}

export function loadProgress(): ProgressState {
  if (typeof localStorage === "undefined") return emptyProgress();
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return emptyProgress();
    const parsed = JSON.parse(raw) as Partial<ProgressState>;
    if (parsed.version !== 1) return emptyProgress();
    return {
      version: 1,
      chapters: parsed.chapters ?? {},
      checklists: parsed.checklists ?? {},
      lastByCourse: parsed.lastByCourse ?? {},
      lastVisited: parsed.lastVisited ?? "",
    };
  } catch {
    return emptyProgress();
  }
}

export function saveProgress(state: ProgressState): void {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  window.dispatchEvent(new CustomEvent("ai-progress", { detail: state }));
}

export function setLastVisited(course: string, chapterSlug: string): void {
  const state = loadProgress();
  const id = chapterKey(course, chapterSlug);
  state.lastByCourse[course] = id;
  state.lastVisited = id;
  saveProgress(state);
}

export function markChapter(chapterId: string, completed: boolean): void {
  const state = loadProgress();
  if (completed) {
    state.chapters[chapterId] = {
      completed: true,
      completedAt: new Date().toISOString(),
    };
  } else {
    delete state.chapters[chapterId];
  }
  saveProgress(state);
}

export function setChecklistItem(id: string, checked: boolean): void {
  const state = loadProgress();
  if (checked) state.checklists[id] = true;
  else delete state.checklists[id];
  saveProgress(state);
}

export function resetCourse(course: string): void {
  const state = loadProgress();
  const prefix = `${course}/`;
  for (const key of Object.keys(state.chapters)) {
    if (key.startsWith(prefix)) delete state.chapters[key];
  }
  for (const key of Object.keys(state.checklists)) {
    if (key.startsWith(prefix)) delete state.checklists[key];
  }
  delete state.lastByCourse[course];
  if (state.lastVisited.startsWith(prefix)) state.lastVisited = "";
  saveProgress(state);
}

export function isChapterComplete(
  state: ProgressState,
  chapterId: string,
): boolean {
  return Boolean(state.chapters[chapterId]?.completed);
}

export function courseStats(
  state: ProgressState,
  course: string,
  chapterIds: string[],
): { completed: number; total: number; nextId: string | null } {
  const completed = chapterIds.filter((id) =>
    isChapterComplete(state, id),
  ).length;
  const last = state.lastByCourse[course];
  const lastIncomplete =
    last && chapterIds.includes(last) && !isChapterComplete(state, last)
      ? last
      : null;
  const firstIncomplete =
    chapterIds.find((id) => !isChapterComplete(state, id)) ?? null;
  return {
    completed,
    total: chapterIds.length,
    nextId: lastIncomplete ?? firstIncomplete ?? chapterIds[0] ?? null,
  };
}

export function chapterSlugFromId(chapterId: string): string {
  return chapterId.split("/").slice(1).join("/");
}
