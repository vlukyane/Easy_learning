import { getCollection, getEntry, render, type CollectionEntry } from "astro:content";

export type Section = CollectionEntry<"sections">;
export type Course = CollectionEntry<"courses">;
export type Chapter = CollectionEntry<"chapters">;

export async function getSections(): Promise<Section[]> {
  const sections = await getCollection("sections");
  return sections.sort((a, b) => a.data.order - b.data.order);
}

export async function getSection(slug: string): Promise<Section | undefined> {
  return getEntry("sections", slug);
}

export async function getCourses(section?: string): Promise<Course[]> {
  const courses = await getCollection("courses", (entry) =>
    section ? entry.data.section === section : true,
  );
  return courses.sort((a, b) => a.data.order - b.data.order);
}

export async function getCourse(slug: string): Promise<Course | undefined> {
  return getEntry("courses", slug);
}

export async function getChapters(course: string): Promise<Chapter[]> {
  const chapters = await getCollection("chapters", (entry) => entry.data.course === course);
  return chapters.sort((a, b) => a.data.order - b.data.order);
}

export function chapterId(chapter: Chapter): string {
  return `${chapter.data.course}/${chapter.id.replace(`${chapter.data.course}/`, "")}`;
}

export function chapterSlug(chapter: Chapter): string {
  const id = chapter.id;
  const prefix = `${chapter.data.course}/`;
  return id.startsWith(prefix) ? id.slice(prefix.length) : id;
}

export async function renderChapter(chapter: Chapter) {
  return render(chapter);
}

export function trackHref(track: string): string {
  return `/tracks/${track}`;
}

export function courseHref(track: string, course: string): string {
  return `/tracks/${track}/${course}`;
}

export function chapterHref(track: string, course: string, slug: string): string {
  return `/tracks/${track}/${course}/${slug}`;
}
