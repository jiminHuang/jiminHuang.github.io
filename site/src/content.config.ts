import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const projects = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/projects" }),
  schema: z.object({
    name: z.string(),
    tagline: z.string(),
    status: z.enum(["Active", "Completed", "Paused"]),
    domain: z.enum(["Biomedicine", "Public health", "Biodiversity", "Industry", "Other"]),
    yearStart: z.number().int(),
    yearEnd: z.number().int().optional(),
    funder: z.string().optional(),
    partners: z.array(z.string()).default([]),
    lead: z.string().optional(),
    tools: z.array(z.string()).default([]),
    publications: z
      .array(
        z.object({
          title: z.string(),
          venue: z.string().optional(),
          year: z.number().int().optional(),
          url: z.string().url().optional(),
        }),
      )
      .default([]),
    website: z.string().url().optional(),
  }),
});

const tools = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/tools" }),
  schema: z.object({
    name: z.string(),
    tag: z.string(),
    tagline: z.string(),
    status: z.enum(["Available", "Beta", "Archived"]).default("Available"),
    url: z.string().url().optional(),
    repo: z.string().url().optional(),
  }),
});

const people = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/people" }),
  schema: z.object({
    name: z.string(),
    title: z.string().optional(),
    group: z.enum([
      "Director",
      "Deputy",
      "Scientific Advisor",
      "Staff",
      "Visiting",
      "Associated",
      "PhD",
      "MPhil",
      "Alumni",
    ]),
    affiliation: z.string().optional(),
    email: z.string().optional(),
    topics: z.array(z.string()).default([]),
    supervisor: z.string().optional(),
    coSupervisor: z.string().optional(),
    funding: z.string().optional(),
    /** Alumni only */
    yearGraduated: z.number().int().optional(),
    degree: z.string().optional(),
    currentPosition: z.string().optional(),
    /** Display ordering inside a group (lower = earlier) */
    order: z.number().int().default(100),
    /** Path under /public, e.g. /photos/sophia_2023.jpg */
    photo: z.string().optional(),
  }),
});

export const collections = { projects, tools, people };
