[CmdletBinding()]
param(
    [string[]]$Root = @(
        'Z:\[Vibe Coded (AI)]\ANTIGRAVITY',
        'Z:\[Vibe Coded (AI)]\CODEX',
        'Z:\[Vibe Coded (AI)]\CLAUDECODE'
    ),
    [string]$JsonPath
)

$ErrorActionPreference = 'Stop'
$skip = @('node_modules', '.venv', 'venv', 'dist', 'build', 'target', '.git')
$queue = [System.Collections.Generic.Queue[string]]::new()
$seen = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
$repos = [System.Collections.Generic.List[object]]::new()
foreach ($r in $Root) {
    if (Test-Path -LiteralPath $r -PathType Container) { $queue.Enqueue((Resolve-Path -LiteralPath $r).Path) }
}

while ($queue.Count -gt 0) {
    $dir = $queue.Dequeue()
    if (-not $seen.Add($dir)) { continue }
    $git = Join-Path $dir '.git'
    if (Test-Path -LiteralPath $git) {
        $status = (& git -C $dir status --porcelain 2>$null | Out-String).Trim()
        $unmerged = (& git -C $dir diff --name-only --diff-filter=U 2>$null | Out-String).Trim()
        $null = & git -C $dir diff --check 2>&1
        $whitespace = ($LASTEXITCODE -ne 0)
        $repos.Add([pscustomobject]@{
            path = $dir
            dirty = [bool]$status
            unmerged = [bool]$unmerged
            diff_check_failure = [bool]$whitespace
        })
        # A worktree's .git directory is metadata; do not descend into it.
        continue
    }
    foreach ($child in [System.IO.Directory]::EnumerateDirectories($dir)) {
        $name = [System.IO.Path]::GetFileName($child)
        if ($skip -notcontains $name) { $queue.Enqueue($child) }
    }
}

$report = [pscustomobject]@{
    generated_utc = [DateTime]::UtcNow.ToString('o')
    roots = $Root
    repository_count = $repos.Count
    dirty_count = @($repos | Where-Object dirty).Count
    unmerged_count = @($repos | Where-Object unmerged).Count
    diff_check_failure_count = @($repos | Where-Object diff_check_failure).Count
    repositories = @($repos | Sort-Object path)
}
if ($JsonPath) {
    $report | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $JsonPath -Encoding utf8
}
$report | Select-Object generated_utc, repository_count, dirty_count, unmerged_count, diff_check_failure_count | Format-List
if ($report.unmerged_count -gt 0 -or $report.diff_check_failure_count -gt 0) { exit 2 }
