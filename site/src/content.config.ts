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

export const collections = { projects, tools };
