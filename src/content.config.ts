import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const sections = defineCollection({
  loader: glob({ pattern: "*.md", base: "./src/content/sections" }),
  schema: z.object({
    order: z.number(),
    title: z.string(),
    tagline: z.string(),
    goal: z.string(),
    stack: z.array(z.string()),
  }),
});

const courses = defineCollection({
  loader: glob({ pattern: "*.md", base: "./src/content/courses" }),
  schema: z.object({
    section: z.enum(["ai", "web"]),
    order: z.number(),
    title: z.string(),
    skill: z.string(),
    goal: z.string(),
    metric: z.string(),
    pilot: z.string(),
    stack: z.array(z.string()),
    projectDir: z.string(),
    dod: z.array(z.string()),
  }),
});

const chapters = defineCollection({
  loader: glob({ pattern: "**/*.mdx", base: "./src/content/chapters" }),
  schema: z.object({
    course: z.string(),
    order: z.number(),
    title: z.string(),
    summary: z.string(),
    estMinutes: z.number(),
  }),
});

export const collections = { sections, courses, chapters };
