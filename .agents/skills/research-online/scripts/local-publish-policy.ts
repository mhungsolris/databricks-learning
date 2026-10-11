import fs from "node:fs";
import path from "node:path";

// Repository adapter: no network, commits, credentials, or publication.
export function getRepoRoot(startDir: string): string {
  let current = path.resolve(startDir);
  while (!fs.existsSync(path.join(current, "AGENTS.md"))) {
    const parent = path.dirname(current);
    if (parent === current) throw new Error("Run from the repository with AGENTS.md.");
    current = parent;
  }
  return current;
}

export function publishScopedArtifacts(options: {
  repoRoot: string; scopePaths: string[]; commitMessage: string; dryRun?: boolean;
}): { branchName: string; commitMessage: string } {
  if (!options.dryRun) {
    throw new Error("Automatic publication is disabled. Use --no-publish and review artifacts locally.");
  }
  return { branchName: "dry-run-only", commitMessage: options.commitMessage };
}
